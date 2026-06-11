import os
import sqlite3
from pathlib import Path

DB_PATH = Path(os.environ.get("DB_PATH", str(Path(__file__).parent / "hydrolab.db")))


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS sessions (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            nim          TEXT NOT NULL,
            name         TEXT NOT NULL,
            package_id   INTEGER DEFAULT NULL,
            current_task INTEGER DEFAULT 1,
            run_count    INTEGER DEFAULT 0,
            started_at   TEXT DEFAULT (datetime('now', '+7 hours'))
        );
        CREATE TABLE IF NOT EXISTS runs (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id  INTEGER NOT NULL,
            task_no     INTEGER NOT NULL,
            code        TEXT NOT NULL,
            stdout      TEXT,
            stderr      TEXT,
            ran_at      TEXT DEFAULT (datetime('now', '+7 hours'))
        );
        CREATE TABLE IF NOT EXISTS submissions (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id    INTEGER NOT NULL,
            task_no       INTEGER NOT NULL,
            code          TEXT NOT NULL,
            output        TEXT,
            explanation   TEXT,
            ai_score      INTEGER DEFAULT 0,
            submitted_at  TEXT DEFAULT (datetime('now', '+7 hours'))
        );
        CREATE TABLE IF NOT EXISTS drafts (
            session_id  INTEGER NOT NULL,
            task_no     INTEGER NOT NULL,
            code        TEXT,
            saved_at    TEXT DEFAULT (datetime('now', '+7 hours')),
            PRIMARY KEY (session_id, task_no)
        );
    """)
    conn.commit()
    try:
        conn.execute("ALTER TABLE sessions ADD COLUMN package_id INTEGER DEFAULT NULL")
        conn.commit()
    except Exception:
        pass
    try:
        conn.execute("ALTER TABLE submissions ADD COLUMN explanation TEXT")
        conn.commit()
    except Exception:
        pass
    try:
        conn.execute("ALTER TABLE submissions ADD COLUMN ai_score INTEGER DEFAULT 0")
        conn.commit()
    except Exception:
        pass
    conn.close()


def create_session(nim: str, name: str) -> int:
    conn = get_db()
    cur = conn.execute(
        "INSERT INTO sessions (nim, name) VALUES (?, ?)",
        (nim.strip(), name.strip()),
    )
    sid = cur.lastrowid
    conn.commit()
    conn.close()
    return sid


def set_package(session_id: int, package_id: int):
    conn = get_db()
    conn.execute(
        "UPDATE sessions SET package_id = ? WHERE id = ?", (package_id, session_id)
    )
    conn.commit()
    conn.close()


def get_session(session_id: int):
    conn = get_db()
    row = conn.execute("SELECT * FROM sessions WHERE id = ?", (session_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def save_run(session_id: int, task_no: int, code: str, stdout: str, stderr: str):
    conn = get_db()
    conn.execute(
        "INSERT INTO runs (session_id, task_no, code, stdout, stderr) VALUES (?, ?, ?, ?, ?)",
        (session_id, task_no, code, stdout, stderr),
    )
    conn.execute(
        "UPDATE sessions SET run_count = run_count + 1 WHERE id = ?", (session_id,)
    )
    conn.commit()
    conn.close()


def save_submission(session_id: int, task_no: int, code: str, output: str, explanation: str = "", ai_score: int = 0):
    conn = get_db()
    conn.execute(
        "INSERT INTO submissions (session_id, task_no, code, output, explanation, ai_score) VALUES (?, ?, ?, ?, ?, ?)",
        (session_id, task_no, code, output, explanation, ai_score),
    )
    conn.commit()
    conn.close()


def update_current_task(session_id: int, task_no: int):
    conn = get_db()
    conn.execute(
        "UPDATE sessions SET current_task = ? WHERE id = ?", (task_no, session_id)
    )
    conn.commit()
    conn.close()


def get_all_sessions():
    conn = get_db()
    rows = conn.execute("""
        SELECT
            s.id, s.nim, s.name, s.package_id, s.current_task, s.run_count, s.started_at,
            r.stdout  AS last_output,
            r.stderr  AS last_error,
            r.ran_at  AS last_run_at,
            (SELECT COUNT(*) FROM submissions WHERE session_id = s.id) AS submitted_count
        FROM sessions s
        LEFT JOIN runs r ON r.id = (
            SELECT id FROM runs WHERE session_id = s.id ORDER BY ran_at DESC LIMIT 1
        )
        ORDER BY s.started_at DESC
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_session_detail(session_id: int):
    conn = get_db()
    session = dict(conn.execute("SELECT * FROM sessions WHERE id = ?", (session_id,)).fetchone())
    submissions = [
        dict(r) for r in conn.execute(
            "SELECT * FROM submissions WHERE session_id = ? ORDER BY task_no",
            (session_id,),
        ).fetchall()
    ]
    conn.close()
    return {"session": session, "submissions": submissions}


def save_draft(session_id: int, task_no: int, code: str):
    conn = get_db()
    conn.execute(
        """INSERT INTO drafts (session_id, task_no, code, saved_at)
           VALUES (?, ?, ?, datetime('now', '+7 hours'))
           ON CONFLICT(session_id, task_no) DO UPDATE SET
             code=excluded.code, saved_at=excluded.saved_at""",
        (session_id, task_no, code),
    )
    conn.commit()
    conn.close()


def get_draft(session_id: int, task_no: int):
    conn = get_db()
    row = conn.execute(
        "SELECT code FROM drafts WHERE session_id=? AND task_no=?",
        (session_id, task_no),
    ).fetchone()
    conn.close()
    return row["code"] if row else None


def clean_all():
    conn = get_db()
    conn.executescript("""
        DELETE FROM submissions;
        DELETE FROM runs;
        DELETE FROM sessions;
        DELETE FROM drafts;
    """)
    conn.commit()
    conn.close()
