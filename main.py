import io
import json
import os
import secrets
from datetime import datetime
from typing import List

import pandas as pd
from fastapi import Depends, FastAPI, Form, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates

import database
import runner
import tasks
import ai_detector

app = FastAPI(title="HydroLab")
templates = Jinja2Templates(directory="templates")
_security = HTTPBasic()

# Credentials — override via env vars HYDROLAB_USER and HYDROLAB_PASS in start.bat
_DASH_USER = os.environ.get("HYDROLAB_USER", "instruktur")
_DASH_PASS = os.environ.get("HYDROLAB_PASS", "hydrolab2026")


def require_instructor(credentials: HTTPBasicCredentials = Depends(_security)):
    ok_user = secrets.compare_digest(credentials.username.encode(), _DASH_USER.encode())
    ok_pass = secrets.compare_digest(credentials.password.encode(), _DASH_PASS.encode())
    if not (ok_user and ok_pass):
        raise HTTPException(
            status_code=401,
            detail="Login instruktur diperlukan.",
            headers={"WWW-Authenticate": "Basic"},
        )


# ── WebSocket manager ────────────────────────────────────────────────────────

class DashboardManager:
    def __init__(self):
        self._connections: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self._connections.append(ws)

    def disconnect(self, ws: WebSocket):
        if ws in self._connections:
            self._connections.remove(ws)

    async def broadcast(self, payload: dict):
        msg = json.dumps(payload)
        dead = []
        for ws in self._connections:
            try:
                await ws.send_text(msg)
            except Exception:
                dead.append(ws)
        for ws in dead:
            self.disconnect(ws)


manager = DashboardManager()


# ── Startup ──────────────────────────────────────────────────────────────────

@app.on_event("startup")
async def startup():
    database.init_db()
    runner.ensure_data()


# ── Student: join ────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def join_page(request: Request):
    return templates.TemplateResponse(request, "join.html")


@app.post("/join")
async def join(nim: str = Form(...), name: str = Form(...)):
    sid = database.create_session(nim, name)
    return RedirectResponse(f"/select-package/{sid}", status_code=303)


# ── Student: package selection ───────────────────────────────────────────────

@app.get("/select-package/{session_id}", response_class=HTMLResponse)
async def select_package_page(request: Request, session_id: int):
    session = database.get_session(session_id)
    if not session:
        return RedirectResponse("/")
    return templates.TemplateResponse(request, "select_package.html", {
        "session": session,
        "packages": tasks.PACKAGES,
    })


@app.post("/select-package/{session_id}")
async def select_package(session_id: int, package_id: int = Form(...)):
    session = database.get_session(session_id)
    if not session:
        return RedirectResponse("/")
    if package_id not in tasks.PACKAGES:
        return RedirectResponse(f"/select-package/{session_id}", status_code=303)
    database.set_package(session_id, package_id)
    return RedirectResponse(f"/student/{session_id}", status_code=303)


# ── Student: coding page ─────────────────────────────────────────────────────

@app.get("/student/{session_id}", response_class=HTMLResponse)
async def student_page(request: Request, session_id: int):
    session = database.get_session(session_id)
    if not session:
        return RedirectResponse("/")
    if not session["package_id"]:
        return RedirectResponse(f"/select-package/{session_id}")

    pkg_id = session["package_id"]
    total = tasks.get_package_total(pkg_id)
    all_done = session["current_task"] > total
    task = tasks.get_task_from_package(pkg_id, session["current_task"])
    if not task:
        task = tasks.get_task_from_package(pkg_id, total)

    return templates.TemplateResponse(request, "student.html", {
        "session": session,
        "task": task,
        "total_tasks": total,
        "all_done": all_done,
        "package": tasks.PACKAGES[pkg_id],
    })


@app.post("/run/{session_id}/{task_no}")
async def run_code(session_id: int, task_no: int, request: Request):
    body = await request.json()
    code = body.get("code", "")
    result = runner.run_code(code)
    database.save_run(session_id, task_no, code, result["stdout"], result["stderr"])
    await manager.broadcast({"type": "run", "session_id": session_id})
    return result


@app.post("/submit/{session_id}/{task_no}")
async def submit_task(session_id: int, task_no: int, request: Request):
    body = await request.json()
    code = body.get("code", "")
    explanation = body.get("explanation", "").strip()
    result = runner.run_code(code)

    # Run AI detection
    ai_analysis = ai_detector.detect_ai_patterns(code)
    ai_score = ai_analysis["score"]

    database.save_submission(
        session_id, task_no, code, result["stdout"],
        explanation=explanation, ai_score=ai_score
    )

    session = database.get_session(session_id)
    total = tasks.get_package_total(session["package_id"])
    next_task = task_no + 1

    if next_task <= total:
        database.update_current_task(session_id, next_task)
        await manager.broadcast({"type": "submit", "session_id": session_id})
        return {
            "next_task": next_task,
            "done": False,
            "ai_analysis": ai_analysis,
        }
    else:
        database.update_current_task(session_id, next_task)
        await manager.broadcast({"type": "done", "session_id": session_id})
        return {
            "next_task": None,
            "done": True,
            "ai_analysis": ai_analysis,
        }


# ── Instructor dashboard ──────────────────────────────────────────────────────

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request, _=Depends(require_instructor)):
    return templates.TemplateResponse(request, "dashboard.html", {
        "packages": tasks.PACKAGES,
    })


@app.get("/api/sessions")
async def api_sessions(_=Depends(require_instructor)):
    return database.get_all_sessions()


@app.get("/api/session/{session_id}")
async def api_session_detail(session_id: int, _=Depends(require_instructor)):
    data = database.get_session_detail(session_id)
    # Attach rubric for each submitted task
    pkg_id = data["session"].get("package_id")
    if pkg_id:
        for sub in data["submissions"]:
            t = tasks.get_task_from_package(pkg_id, sub["task_no"])
            sub["rubric"] = t["rubric"] if t else []
            sub["task_title"] = t["title"] if t else ""
    return data


@app.post("/api/clean-db")
async def clean_db(_=Depends(require_instructor)):
    database.clean_all()
    await manager.broadcast({"type": "cleaned"})
    return {"status": "ok", "message": "Semua data sesi berhasil dihapus."}


@app.get("/export")
async def export_excel(_=Depends(require_instructor)):
    import sqlite3
    conn = sqlite3.connect(database.DB_PATH)

    # Sheet 1: Rekap per mahasiswa
    summary = pd.read_sql("""
        SELECT
            s.nim, s.name,
            (SELECT COUNT(*) FROM submissions WHERE session_id=s.id) AS total_submit,
            s.run_count AS total_run,
            s.started_at
        FROM sessions s
        ORDER BY s.nim
    """, conn)

    # Sheet 2: Detail submission dengan explanation & AI score
    detail = pd.read_sql("""
        SELECT
            s.nim, s.name, sub.task_no,
            sub.explanation,
            sub.ai_score AS 'AI_Risk_Score(0-100)',
            sub.output,
            sub.submitted_at
        FROM submissions sub
        JOIN sessions s ON s.id = sub.session_id
        ORDER BY s.nim, sub.task_no
    """, conn)

    # Sheet 3: Rubrik assessment per mahasiswa per soal
    submissions = pd.read_sql("""
        SELECT s.id, s.nim, s.name, s.package_id, sub.task_no, sub.code
        FROM submissions sub
        JOIN sessions s ON s.id = sub.session_id
        ORDER BY s.nim, sub.task_no
    """, conn)

    # Sheet 4: Kode lengkap per submission
    codes = pd.read_sql("""
        SELECT
            s.nim, s.name, sub.task_no, sub.code,
            sub.submitted_at
        FROM submissions sub
        JOIN sessions s ON s.id = sub.session_id
        ORDER BY s.nim, sub.task_no
    """, conn)

    conn.close()

    # Build rubrik sheet
    rubrik_rows = []
    for _, row in submissions.iterrows():
        pkg_id = row["package_id"]
        task_no = row["task_no"]
        task = tasks.get_task_from_package(pkg_id, task_no)
        if not task or "rubric" not in task:
            continue

        for rubric_item in task["rubric"]:
            rubrik_rows.append({
                "NIM": row["nim"],
                "Nama": row["name"],
                "Soal": task_no,
                "Kriteria": rubric_item["kriteria"],
                "Poin": rubric_item["poin"],
                "Catatan_Instruktur": "",  # Empty untuk instruktur isi manual
            })

    rubrik_df = pd.DataFrame(rubrik_rows) if rubrik_rows else pd.DataFrame(columns=[
        "NIM", "Nama", "Soal", "Kriteria", "Poin", "Catatan_Instruktur"
    ])

    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        summary.to_excel(writer, sheet_name="1_Rekap", index=False)
        detail.to_excel(writer, sheet_name="2_Submission", index=False)
        rubrik_df.to_excel(writer, sheet_name="3_Rubrik_Assessment", index=False)
        codes.to_excel(writer, sheet_name="4_Kode_Lengkap", index=False)

        # Format columns
        for sheet_name in writer.sheets:
            ws = writer.sheets[sheet_name]
            for col_idx, col in enumerate(ws.columns, 1):
                max_len = 50
                for cell in col:
                    try:
                        if cell.value:
                            max_len = max(max_len, len(str(cell.value)))
                    except:
                        pass
                ws.column_dimensions[cell.column_letter].width = min(max_len + 2, 80)

            # Wrap text untuk kolom panjang
            for row in ws.iter_rows():
                for cell in row:
                    if cell.column_letter in ['C', 'D', 'E', 'F']:  # explanation, output, code, dll
                        cell.alignment = cell.alignment.copy(wrap_text=True)

    buf.seek(0)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    return StreamingResponse(
        buf,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename=HydroLab_Hasil_{timestamp}.xlsx"},
    )


@app.websocket("/ws/dashboard")
async def dashboard_ws(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
