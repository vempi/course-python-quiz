import os
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).parent / "data" / "rainfall.csv"

# Injected before every student code run
PREAMBLE = (
    "import pandas as pd\n"
    "import numpy as np\n"
    "import warnings\n"
    "warnings.filterwarnings('ignore')\n"
    "pd.set_option('display.max_columns', 10)\n"
    "pd.set_option('display.width', 100)\n"
    "pd.set_option('display.max_rows', 60)\n"
    "df = pd.read_csv(r'" + str(DATA_PATH) + "', parse_dates=['Date'])\n\n"
)


def ensure_data():
    """Generate synthetic multi-source satellite rainfall dataset (2001-2022).

    Format: Date, GSMAP, GPM, PERSIANN, CHIRPS — matching the Pertemuan-8 tutorial.
    Includes ~2% missing values so students can practice data cleaning (Soal 5).
    """
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DATA_PATH.exists():
        return

    np.random.seed(42)
    dates = pd.date_range("2001-01-01", "2022-12-31", freq="D")
    doy = dates.dayofyear

    # Seasonal pattern: wetter Jan-Apr & Oct-Dec (Indonesian wet season), drier May-Sep
    seasonal = np.maximum(0.5, 8 + 7 * np.cos(2 * np.pi * (doy - 15) / 365))

    def gen_source(bias=1.0, noise=0.8):
        raw = np.random.exponential(scale=seasonal * noise) * bias
        return np.maximum(0, raw).round(1)

    df = pd.DataFrame({
        "Date"    : dates.strftime("%Y-%m-%d"),
        "GSMAP"   : gen_source(1.00),
        "GPM"     : gen_source(0.95),
        "PERSIANN": gen_source(1.10),
        "CHIRPS"  : gen_source(0.85),
    })

    # Inject ~2% missing values per source for Soal 5 (data cleaning)
    rng = np.random.default_rng(99)
    for col in ["GSMAP", "GPM", "PERSIANN", "CHIRPS"]:
        mask = rng.random(len(df)) < 0.02
        df.loc[mask, col] = None

    # Inject a few artificial outliers per source for Soal 5 (outlier detection)
    for col in ["GSMAP", "GPM", "PERSIANN", "CHIRPS"]:
        idx = rng.choice(len(df), size=15, replace=False)
        df.loc[idx, col] = rng.uniform(180, 300, size=15).round(1)

    df.to_csv(DATA_PATH, index=False)
    print(f"[HydroLab] Dataset dibuat: {len(df)} baris -> {DATA_PATH}")


def run_code(code: str, timeout: int = 20) -> dict:
    full_code = PREAMBLE + code

    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    )
    try:
        tmp.write(full_code)
        tmp.close()

        result = subprocess.run(
            [sys.executable, tmp.name],
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
        )
        return {
            "stdout": result.stdout[:5000],
            "stderr": result.stderr[:2000],
            "returncode": result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": f"Timeout: eksekusi melebihi {timeout} detik.",
            "returncode": -1,
        }
    except Exception as exc:
        return {"stdout": "", "stderr": str(exc), "returncode": -1}
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass
