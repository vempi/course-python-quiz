# ── Task definitions ────────────────────────────────────────────────────────
# Rubrik: list of {"no", "kriteria", "poin"}

# ── Paket Ujian 2026 ──────────────────────────────────────────────────────────

_ET1 = {
    "no": 1,
    "title": "Eksplorasi Dataset & Profil Statistik",
    "description": """\
## Soal 1 — Eksplorasi Dataset & Profil Statistik

Dataset curah hujan harian dari **4 produk satelit** (GSMAP, GPM, PERSIANN, CHIRPS)
periode 2001–2022 tersedia sebagai variabel `df`.

| Kolom | Keterangan |
|-------|-----------|
| `Date` | Tanggal pengukuran (datetime) |
| `GSMAP` | Curah hujan harian GSMAP (mm/hari) |
| `GPM` | Curah hujan harian GPM (mm/hari) |
| `PERSIANN` | Curah hujan harian PERSIANN (mm/hari) |
| `CHIRPS` | Curah hujan harian CHIRPS (mm/hari) |

**Kerjakan:**
1. Import library pandas, matplotlib, dan numpy
2. Tampilkan **10 baris pertama** dan **5 baris terakhir** dataset
3. Cetak informasi kolom menggunakan 
4. Cetak statistik deskriptif semua sumber 
5. Hitung jumlah missing values per kolom
6. Buat **bar chart** rata-rata curah hujan per sumber — tambahkan title, xlabel, ylabel (mm/hari)

*Hint: missing values per kolom*
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS

# 1. import library

# 2. tampilkan 10 baris pertama dan 5 baris terakhir

# 3. cetak info

# 4. cetak describe

# 5. hitung missing values per kolom

# 6. bar chart rata-rata per sumber
""",
    "rubric": [
        {"no": 1, "kriteria": "Import pandas, matplotlib, numpy dengan benar", "poin": 15},
        {"no": 2, "kriteria": "Menampilkan head(10) dan tail(5)", "poin": 15},
        {"no": 3, "kriteria": "Mencetak info() — tipe kolom dan jumlah non-null terlihat", "poin": 20},
        {"no": 4, "kriteria": "Mencetak describe() — nilai min/max/mean masuk akal", "poin": 20},
        {"no": 5, "kriteria": "Missing values per kolom dihitung dengan benar", "poin": 15},
        {"no": 6, "kriteria": "Bar chart mean per sumber dengan title, xlabel, ylabel yang benar", "poin": 15},
    ],
}

_ET2 = {
    "no": 2,
    "title": "Tipe Data, Missing Values & Pembersihan",
    "description": """\
## Soal 2 — Tipe Data, Missing Values & Pembersihan

Sebelum analisis, pastikan dataset bersih dari error tipe data dan nilai kosong.

**Kerjakan:**
1. Periksa tipe data setiap kolom
2. Pastikan kolom `Date` bertipe `datetime` — konversi jika belum
3. Hapus baris yang memiliki **setidaknya satu** nilai NaN
4. Isi sisa missing values dengan **0**
5. Verifikasi tidak ada NaN tersisa setelah pembersihan
6. Buat **bar chart horizontal** jumlah missing values per sumber **sebelum** pembersihan
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS

# 1. periksa tipe data setiap kolom

# 2. pastikan Date bertipe datetime

# simpan jumlah missing values sebelum cleaning (untuk plot di langkah 6)

# 3. hapus baris dengan setidaknya satu NaN

# 4. isi sisa missing values dengan 0

# 5. verifikasi tidak ada NaN tersisa

# 6. bar chart horizontal missing values per sumber (sebelum cleaning)
""",
    "rubric": [
        {"no": 1, "kriteria": "Tipe data setiap kolom ditampilkan dengan benar", "poin": 15},
        {"no": 2, "kriteria": "Date dikonversi/dipastikan sebagai datetime", "poin": 20},
        {"no": 3, "kriteria": "Baris dengan minimal satu NaN dihapus dengan benar", "poin": 25},
        {"no": 4, "kriteria": "Sisa missing values diisi dengan 0", "poin": 20},
        {"no": 5, "kriteria": "Verifikasi tidak ada NaN tersisa ditampilkan", "poin": 10},
        {"no": 6, "kriteria": "Bar chart horizontal missing values per sumber dengan label benar", "poin": 10},
    ],
}

_ET3 = {
    "no": 3,
    "title": "Agregasi Bulanan & Pola Musiman",
    "description": """\
## Soal 3 — Agregasi Bulanan & Pola Musiman

Data bulanan dan klimatologi bulanan digunakan untuk memahami pola musiman
curah hujan dalam setahun.

**Kerjakan:**
1. Buat kolom `year` dan `month` dari kolom `Date`
2. Hitung **total curah hujan bulanan** untuk semua sumber dengan `groupby(['year','month']).sum()`
3. Tampilkan total bulanan untuk tahun **2015** (semua kolom)
4. Hitung **klimatologi bulanan** CHIRPS: rata-rata semua Januari (22 nilai),
   semua Februari (22 nilai), dst. — hasil berupa 12 baris
5. Buat **bar chart** klimatologi bulanan CHIRPS (Jan–Des) — title, xlabel (Bulan), ylabel (mm/bulan)

*Hint: `groupby('month')['CHIRPS'].mean()`*
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS

# 1. buat kolom year dan month dari Date

# 2. hitung total bulanan semua sumber dengan groupby

# 3. tampilkan total bulanan tahun 2015

# 4. hitung klimatologi bulanan CHIRPS (rata-rata per bulan kalender)

# 5. bar chart klimatologi bulanan CHIRPS
""",
    "rubric": [
        {"no": 1, "kriteria": "Kolom year dan month dibuat dengan benar dari Date", "poin": 15},
        {"no": 2, "kriteria": "Total bulanan semua sumber dihitung dengan groupby dua kolom yang benar", "poin": 30},
        {"no": 3, "kriteria": "12 baris untuk tahun 2015 semua kolom ditampilkan", "poin": 20},
        {"no": 4, "kriteria": "Klimatologi bulanan CHIRPS dihitung dua langkah: total bulanan → mean per bulan kalender", "poin": 20},
        {"no": 5, "kriteria": "Bar chart klimatologi CHIRPS dengan title, xlabel, ylabel yang benar", "poin": 15},
    ],
}

_ET4 = {
    "no": 4,
    "title": "Hujan Maksimum Tahunan (HMT)",
    "description": """\
## Soal 4 — Hujan Maksimum Tahunan (HMT)

**Hujan Maksimum Tahunan (HMT)** adalah nilai curah hujan harian tertinggi
setiap tahun. HMT merupakan input utama analisis frekuensi banjir.

**Kerjakan:**
1. Buat kolom `year` dari kolom `Date`
2. Hitung **HMT** (nilai harian maksimum tiap tahun) untuk **semua sumber** —
   tampilkan tabel lengkap 22 tahun
3. Hitung **rata-rata HMT** per sumber sepanjang tahun
4. Tentukan sumber dengan **rata-rata HMT tertinggi** —
   print nama sumber dan nilainya
5. Untuk sumber **GPM**: identifikasi **tahun paling ekstrem** (HMT tertinggi) —
   cetak: `"Tahun paling ekstrem GPM: XXXX"`
6. Buat **line plot** HMT semua sumber dalam satu figure —
   legend, title, xlabel (Tahun), ylabel (mm/hari)
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS
sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# 1. buat kolom year dari Date

# 2. hitung HMT per tahun semua sumber, tampilkan tabel 22 tahun

# 3. hitung rata-rata HMT per sumber

# 4. print sumber dengan rata-rata HMT tertinggi

# 5. print tahun paling ekstrem GPM

# 6. line plot HMT semua sumber
""",
    "rubric": [
        {"no": 1, "kriteria": "Kolom year dibuat dengan benar dari Date", "poin": 5},
        {"no": 2, "kriteria": "HMT per tahun semua sumber dihitung dengan groupby benar, tabel 22 tahun ditampilkan", "poin": 25},
        {"no": 3, "kriteria": "Rata-rata HMT per sumber dihitung dengan benar", "poin": 20},
        {"no": 4, "kriteria": "Sumber dengan mean HMT tertinggi diidentifikasi dan diprint dengan nilainya", "poin": 20},
        {"no": 5, "kriteria": "Tahun paling ekstrem GPM diprint dengan format yang benar", "poin": 15},
        {"no": 6, "kriteria": "Line plot HMT semua sumber dengan legend, title, xlabel, ylabel, show()", "poin": 15},
    ],
}

_ET5 = {
    "no": 5,
    "title": "Hujan Tahunan & Anomali",
    "description": """\
## Soal 5 — Hujan Tahunan & Anomali

**Curah hujan tahunan** adalah akumulasi total dalam satu tahun kalender.
**Anomali** mengukur simpangan setiap tahun dari rata-rata jangka panjang —
nilai positif menunjukkan tahun basah, negatif menunjukkan tahun kering.

**Kerjakan:**
1. Hitung **total curah hujan tahunan** untuk semua sumber —
   tampilkan tabel 22 tahun (2001–2022)
2. Hitung **rata-rata jangka panjang** tiap sumber
3. Hitung **anomali tahunan** GSMAP dan tampilkan tabel dengan kolom
   `year`, `GSMAP`, `anomali`
4. Tentukan **tahun dengan total GSMAP tertinggi** (tahun terbasah) —
   cetak tahun dan nilai totalnya
5. Buat **bar chart** total tahunan GSMAP (2001–2022) — tambahkan garis
   putus-putus rata-rata jangka panjang, title, xlabel (Tahun), ylabel (mm/tahun)

*Hint: `anomali = hujan_tahunan − rata_jangka_panjang`*
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS
sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# 1. hitung total curah hujan tahunan semua sumber, tampilkan tabel 22 tahun

# 2. hitung rata-rata jangka panjang tiap sumber

# 3. hitung anomali tahunan GSMAP, tampilkan tabel year + GSMAP + anomali

# 4. print tahun dengan total GSMAP tertinggi

# 5. bar chart total tahunan GSMAP dengan garis rata-rata
""",
    "rubric": [
        {"no": 1, "kriteria": "Total tahunan per sumber dihitung dengan groupby benar, tabel 22 tahun ditampilkan", "poin": 20},
        {"no": 2, "kriteria": "Rata-rata jangka panjang tiap sumber dihitung dengan benar", "poin": 20},
        {"no": 3, "kriteria": "Anomali GSMAP dihitung dengan formula yang benar, tabel year+GSMAP+anomali ditampilkan", "poin": 25},
        {"no": 4, "kriteria": "Tahun dengan total GSMAP tertinggi diidentifikasi dan diprint dengan nilainya", "poin": 15},
        {"no": 5, "kriteria": "Bar chart total tahunan GSMAP dengan garis rata-rata, title, xlabel, ylabel", "poin": 20},
    ],
}


# ── Exam Packages ────────────────────────────────────────────────────────────

PACKAGES = {
    1: {
        "id": 1,
        "name": "Paket Ujian 2026",
        "subtitle": "Ujian Akhir Algoritma dan Pemrograman Komputer",
        "description": "Eksplorasi data, tipe & missing values, agregasi bulanan, HMT multi-sumber, dan analisis hujan tahunan.",
        "tasks": [_ET1, _ET2, _ET3, _ET4, _ET5],
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
