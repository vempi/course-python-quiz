import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd

DATA_PATH        = Path(__file__).parent / "data" / "rainfall.csv"
DATA_PATH_SINGLE = Path(__file__).parent / "data" / "rainfall_single.csv"

# Common head for every run: matplotlib backend + helpers
_COMMON_HEAD = (
    "import matplotlib\n"
    "matplotlib.use('Agg')\n"
    "import matplotlib.pyplot as plt\n"
    "import pandas as pd\n"
    "import numpy as np\n"
    "import warnings\n"
    "warnings.filterwarnings('ignore')\n"
    "pd.set_option('display.max_columns', 10)\n"
    "pd.set_option('display.width', 100)\n"
    "pd.set_option('display.max_rows', 60)\n"
    "def _hl_show(*_a, **_kw):\n"
    "    import base64, io as _io\n"
    "    buf = _io.BytesIO()\n"
    "    plt.savefig(buf, format='png', bbox_inches='tight', dpi=110)\n"
    "    buf.seek(0)\n"
    "    print('__HLPLOT__' + base64.b64encode(buf.read()).decode() + '__HLPLOT__')\n"
    "    plt.close()\n"
    "plt.show = _hl_show\n\n"
)

# Multi-source satellite dataset (Paket 1, 2, 3 — and Paket 4 task 5)
_PREAMBLE_MULTI = (
    _COMMON_HEAD
    + "df = pd.read_csv(r'" + str(DATA_PATH) + "', parse_dates=['Date'])\n\n"
)

# Single-station dataset (Paket 4 tasks 1-4)
_PREAMBLE_SINGLE = (
    _COMMON_HEAD
    + "df = pd.read_csv(r'" + str(DATA_PATH_SINGLE) + "', parse_dates=['tanggal'])\n\n"
)

# Paket 4, task 5 reuses multi-source data (see starter_code with sources=[...])
_P4_SINGLE_TASKS = {1, 2, 3, 4}


def get_preamble(package_id: int | None, task_no: int | None) -> str:
    if package_id == 4 and task_no in _P4_SINGLE_TASKS:
        return _PREAMBLE_SINGLE
    return _PREAMBLE_MULTI


def ensure_data():
    """Generate multi-source satellite rainfall dataset (2001-2022).

    Columns: Date, GSMAP, GPM, PERSIANN, CHIRPS
    Includes ~2% missing values and artificial outliers for Soal 5 (data cleaning).
    """
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DATA_PATH.exists():
        return

    np.random.seed(42)
    dates = pd.date_range("2001-01-01", "2022-12-31", freq="D")
    doy = dates.dayofyear
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

    rng = np.random.default_rng(99)
    for col in ["GSMAP", "GPM", "PERSIANN", "CHIRPS"]:
        mask = rng.random(len(df)) < 0.02
        df.loc[mask, col] = None

    for col in ["GSMAP", "GPM", "PERSIANN", "CHIRPS"]:
        idx = rng.choice(len(df), size=15, replace=False)
        df.loc[idx, col] = rng.uniform(180, 300, size=15).round(1)

    df.to_csv(DATA_PATH, index=False)
    print(f"[HydroLab] Dataset multi-sumber dibuat: {len(df)} baris -> {DATA_PATH}")


def ensure_data_single():
    """Generate single-station rainfall dataset (2013-2022) for Paket 4 tasks 1-4.

    Columns: tanggal, hujan
    Includes missing values and negative values for data-cleaning exercises.
    """
    DATA_PATH_SINGLE.parent.mkdir(parents=True, exist_ok=True)
    if DATA_PATH_SINGLE.exists():
        return

    np.random.seed(123)
    dates = pd.date_range("2013-01-01", "2022-12-31", freq="D")
    doy = dates.dayofyear
    seasonal = np.maximum(0.5, 8 + 7 * np.cos(2 * np.pi * (doy - 15) / 365))
    raw = np.random.exponential(scale=seasonal * 0.9)
    hujan = np.maximum(0, raw).round(1)

    df = pd.DataFrame({
        "tanggal": dates.strftime("%Y-%m-%d"),
        "hujan"  : hujan,
    })

    rng = np.random.default_rng(77)

    # ~1.5% missing values for interpolation exercise
    mask = rng.random(len(df)) < 0.015
    df.loc[mask, "hujan"] = None

    # A few negative values for clip() exercise
    idx_neg = rng.choice(len(df), size=8, replace=False)
    df.loc[idx_neg, "hujan"] = rng.uniform(-5, -0.5, size=8).round(1)

    df.to_csv(DATA_PATH_SINGLE, index=False)
    print(f"[HydroLab] Dataset single-station dibuat: {len(df)} baris -> {DATA_PATH_SINGLE}")


_PLOT_PATTERN = re.compile(r"__HLPLOT__([A-Za-z0-9+/=]+)__HLPLOT__\n?")


def run_code(code: str, package_id: int | None = None,
             task_no: int | None = None, timeout: int = 20) -> dict:
    preamble = get_preamble(package_id, task_no)
    full_code = preamble + code

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

        plots = _PLOT_PATTERN.findall(result.stdout)
        clean_stdout = _PLOT_PATTERN.sub("", result.stdout)

        return {
            "stdout"    : clean_stdout[:5000],
            "stderr"    : result.stderr[:2000],
            "returncode": result.returncode,
            "plots"     : plots[:6],
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout"    : "",
            "stderr"    : f"Timeout: eksekusi melebihi {timeout} detik.",
            "returncode": -1,
            "plots"     : [],
        }
    except Exception as exc:
        return {"stdout": "", "stderr": str(exc), "returncode": -1, "plots": []}
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass
