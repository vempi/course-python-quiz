# ── Task definitions ────────────────────────────────────────────────────────
# Rubrik: list of {"no", "kriteria", "poin"}
# starter_code: hanya "#  N." agar mahasiswa mulai dari kosong

_T1 = {
    "no": 1,
    "title": "Eksplorasi Dataset Hujan Multi-Sumber Satelit",
    "description": """\
## Soal 1 — Eksplorasi Dataset Hujan Multi-Sumber Satelit

Dataset curah hujan harian dari **4 produk satelit** (GSMAP, GPM, PERSIANN, CHIRPS)
periode **2001–2022** sudah tersedia sebagai variabel `df`.

| Kolom | Keterangan |
|-------|-----------|
| `Date` | Tanggal pengukuran (datetime) |
| `GSMAP` | Curah hujan harian GSMAP (mm/hari) |
| `GPM` | Curah hujan harian GPM (mm/hari) |
| `PERSIANN` | Curah hujan harian PERSIANN (mm/hari) |
| `CHIRPS` | Curah hujan harian CHIRPS (mm/hari) |

**Kerjakan:**
1. Tampilkan **10 baris pertama** dan **5 baris terakhir** data
2. Tampilkan **informasi kolom** dan tipe datanya (`df.info()`)
3. Tampilkan **statistik deskriptif** semua sumber (`df.describe()`)
4. Tampilkan **jumlah baris dan kolom** dataset
5. Tampilkan **rentang tanggal** (tanggal pertama dan terakhir)
6. Periksa jumlah **missing values** per kolom
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.
""",
    "rubric": [
        {"no": 1, "kriteria": "Menampilkan 10 baris pertama dan 5 baris terakhir dengan head() dan tail()", "poin": 10},
        {"no": 2, "kriteria": "Menampilkan info() kolom dan tipe data yang benar (Date=datetime, sumber=float)", "poin": 15},
        {"no": 3, "kriteria": "Menampilkan statistik deskriptif (min, max, mean, std) untuk semua sumber", "poin": 20},
        {"no": 4, "kriteria": "Menampilkan jumlah baris dan kolom dataset dengan shape atau len()", "poin": 15},
        {"no": 5, "kriteria": "Menampilkan tanggal pertama dan terakhir dengan benar (2001-01-01 s.d. 2022-12-31)", "poin": 20},
        {"no": 6, "kriteria": "Menampilkan jumlah missing values per kolom dengan isnull().sum()", "poin": 20},
    ],
}

_T2 = {
    "no": 2,
    "title": "Read & Write — Agregasi Data Bulanan",
    "description": """\
## Soal 2 — Read & Write: Agregasi Data Bulanan

Data bulanan digunakan untuk studi ketersediaan air, neraca air,
dan kalibrasi model hidrologi DAS.

**Kerjakan:**
1. Buat kolom `year` dan `month` dari kolom `Date`
2. Hitung **total curah hujan bulanan** (mm/bulan) untuk setiap sumber
3. Tampilkan 12 baris pertama hasil agregasi (satu tahun penuh)
4. Temukan **bulan terpaling basah** (rata-rata total tertinggi dari semua sumber)
5. Temukan **bulan terkering** (rata-rata total terendah dari semua sumber)
6. Simpan hasil agregasi bulanan ke file CSV: `hasil_bulanan.csv`

**Hint:** `groupby(['year','month']).sum()` atau `resample('ME', on='Date').sum()`
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.
""",
    "rubric": [
        {"no": 1, "kriteria": "Membuat kolom year dan month yang benar dari kolom Date (dt.year, dt.month)", "poin": 10},
        {"no": 2, "kriteria": "Menghitung total bulanan per sumber dengan groupby atau resample yang tepat", "poin": 30},
        {"no": 3, "kriteria": "Menampilkan 12 baris pertama hasil agregasi dengan format yang rapi", "poin": 15},
        {"no": 4, "kriteria": "Mengidentifikasi bulan terpaling basah dengan benar menggunakan idxmax() atau sort_values()", "poin": 20},
        {"no": 5, "kriteria": "Mengidentifikasi bulan terkering dengan benar menggunakan idxmin() atau sort_values()", "poin": 15},
        {"no": 6, "kriteria": "Menyimpan hasil ke CSV dengan to_csv() dan nama file yang benar", "poin": 10},
    ],
}

_T3 = {
    "no": 3,
    "title": "Hujan Harian Maksimum Tahunan (HMT)",
    "description": """\
## Soal 3 — Hujan Harian Maksimum Tahunan (HMT)

**Annual Maximum Series (AMS)** atau HMT adalah nilai curah hujan harian tertinggi
setiap tahun. Ini merupakan input utama dalam analisis frekuensi banjir.

**Kerjakan:**
1. Buat kolom `year` dari kolom `Date`
2. Hitung **HMT** (nilai maksimum harian per tahun) untuk semua sumber
3. Tampilkan seluruh tabel HMT (tahun 2001–2022)
4. Tentukan **tahun dengan HMT tertinggi** untuk masing-masing sumber
5. Hitung **rata-rata HMT** selama 2001–2022 per sumber
6. Bandingkan: sumber mana yang memberikan HMT **tertinggi** dan **terendah** secara rata-rata?
7. Simpan HMT ke file CSV: `HMT_multi_sumber.csv`
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.

# 7.
""",
    "rubric": [
        {"no": 1, "kriteria": "Membuat kolom year yang benar dari kolom Date", "poin": 5},
        {"no": 2, "kriteria": "Menghitung HMT dengan groupby('year')[sources].max() yang benar", "poin": 25},
        {"no": 3, "kriteria": "Menampilkan seluruh tabel HMT 22 tahun dengan semua sumber", "poin": 15},
        {"no": 4, "kriteria": "Mengidentifikasi tahun HMT tertinggi per sumber dengan idxmax()", "poin": 20},
        {"no": 5, "kriteria": "Menghitung rata-rata HMT per sumber dengan mean()", "poin": 15},
        {"no": 6, "kriteria": "Menyimpulkan sumber dengan HMT tertinggi dan terendah berdasarkan data", "poin": 10},
        {"no": 7, "kriteria": "Menyimpan HMT ke CSV dengan nama file yang benar", "poin": 10},
    ],
}

_T4 = {
    "no": 4,
    "title": "Perbandingan Antar Sumber Satelit",
    "description": """\
## Soal 4 — Perbandingan Antar Sumber Satelit

Setiap produk satelit memiliki bias dan ketidakpastian berbeda.
Membandingkan antar sumber adalah langkah penting sebelum digunakan dalam analisis hidrologi.

**Kerjakan:**
1. Hitung **korelasi Pearson** antar semua sumber — sumber mana yang paling mirip?
2. Hitung **bias relatif** setiap sumber terhadap rata-rata ensemble (%):
   `bias = (sumber − ensemble) / ensemble × 100`
3. Buat **tabel statistik ringkasan** (mean, std, min, max, median) per sumber dalam satu tabel
4. Hitung **persentase hari hujan** (hujan > 1 mm) per sumber
5. Berikan **kesimpulan tertulis** (dengan `print()`): sumber mana paling representatif dan mengapa?

**Hint:** `df[sources].mean(axis=1)` untuk rata-rata ensemble per hari
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS
sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# 1.

# 2.

# 3.

# 4.

# 5.
""",
    "rubric": [
        {"no": 1, "kriteria": "Menghitung dan menampilkan matriks korelasi Pearson antar 4 sumber", "poin": 20},
        {"no": 2, "kriteria": "Menghitung bias relatif (%) tiap sumber terhadap ensemble dengan rumus yang benar", "poin": 25},
        {"no": 3, "kriteria": "Membuat tabel ringkasan statistik (min/max/mean/std/median) untuk semua sumber dalam satu tabel", "poin": 25},
        {"no": 4, "kriteria": "Menghitung persentase hari hujan (>1mm) per sumber dengan benar", "poin": 15},
        {"no": 5, "kriteria": "Memberikan kesimpulan tertulis yang logis dan didukung oleh data yang sudah dihitung", "poin": 15},
    ],
}

_T5 = {
    "no": 5,
    "title": "Data Cleaning — Missing Values & Outlier",
    "description": """\
## Soal 5 — Data Cleaning: Missing Values & Outlier

Data observasi hidrologi sering mengandung **data kosong (missing values)**
dan **nilai tak wajar (outlier)**. Membersihkan data adalah langkah wajib
sebelum analisis lebih lanjut.

### Bagian A — Missing Values
1. Hitung **jumlah dan persentase** missing values per sumber
2. Tampilkan baris yang mengandung missing value (gunakan `dropna()` atau boolean mask)
3. Isi missing values dengan **interpolasi linear** (`interpolate(method='linear')`)
4. Verifikasi tidak ada missing values tersisa setelah interpolasi

### Bagian B — Deteksi & Penanganan Outlier
5. Deteksi outlier dengan metode **IQR**:
   - Q1, Q3, IQR = Q3 − Q1
   - Outlier: nilai < Q1 − 1.5×IQR **atau** > Q3 + 1.5×IQR
   - Tampilkan jumlah outlier per sumber
6. Ganti outlier dengan **batas IQR** (clipping/winsorizing):
   `df[col].clip(lower=batas_bawah, upper=batas_atas)`
7. Tampilkan **perbandingan statistik** (mean, max, std) sebelum dan sesudah cleaning
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS
sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# === Bagian A: Missing Values ===

# A1.

# A2.

# A3.

# A4.

# === Bagian B: Outlier ===

# B5.

# B6.

# B7.
""",
    "rubric": [
        {"no": "A1", "kriteria": "Menghitung jumlah dan persentase missing values per sumber dengan isnull().sum()", "poin": 10},
        {"no": "A2", "kriteria": "Menampilkan baris yang mengandung missing value dengan cara yang benar", "poin": 10},
        {"no": "A3", "kriteria": "Mengisi missing values dengan interpolasi linear dan kode yang benar", "poin": 20},
        {"no": "A4", "kriteria": "Memverifikasi tidak ada missing values tersisa setelah interpolasi", "poin": 10},
        {"no": "B5", "kriteria": "Menghitung Q1, Q3, IQR dan mengidentifikasi outlier per sumber dengan rumus yang benar", "poin": 20},
        {"no": "B6", "kriteria": "Melakukan clipping/winsorizing outlier dengan clip() dan batas yang benar", "poin": 15},
        {"no": "B7", "kriteria": "Menampilkan perbandingan statistik sebelum dan sesudah cleaning yang informatif", "poin": 15},
    ],
}

# ── Exam Packages ────────────────────────────────────────────────────────────

PACKAGES = {
    1: {
        "id": 1,
        "name": "Paket 1",
        "subtitle": "Tipe Data Hidrologi & Read/Write Data Hujan",
        "description": "Pertemuan 8 — Eksplorasi, agregasi, HMT, perbandingan sumber, dan data cleaning dataset hujan multi-satelit.",
        "tasks": [_T1, _T2, _T3, _T4, _T5],
    },
}


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_task_from_package(package_id: int, task_no: int):
    pkg = PACKAGES.get(package_id)
    if not pkg:
        return None
    for t in pkg["tasks"]:
        if t["no"] == task_no:
            return t
    return None


def get_package_total(package_id: int) -> int:
    pkg = PACKAGES.get(package_id)
    return len(pkg["tasks"]) if pkg else 0
