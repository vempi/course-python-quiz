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

# ── Paket 2 Tasks ─────────────────────────────────────────────────────────────

_P2T1 = {
    "no": 1,
    "title": "Klimatologi Curah Hujan Bulanan",
    "description": """\
## Soal 1 — Klimatologi Curah Hujan Bulanan

**Klimatologi** curah hujan bulanan adalah rata-rata jangka panjang curah hujan
tiap **bulan kalender** (Jan–Des), dihitung dari akumulasi rekaman tahunan.
Ini berbeda dari sekadar tabel bulanan tahun per tahun.

**Kerjakan:**
1. Agregasikan data harian → **total bulanan** per tahun untuk semua sumber
   *(setiap bulan setiap tahun = satu baris, bukan rata-rata harian)*
2. Dari total bulanan tersebut, hitung **rata-rata klimatologi** per bulan kalender:
   rata-rata semua Januari (22 nilai), rata-rata semua Februari (22 nilai), dst.
3. Tampilkan tabel klimatologi (12 baris × 4 kolom sumber) dibulatkan 1 desimal
4. Tambahkan kolom `kontribusi_pct` untuk **GSMAP**: persentase tiap bulan terhadap
   total klimatologi tahunan GSMAP — pastikan 12 nilai menjumlah ≈ 100 %
5. Identifikasi **bulan basah** (nilai GSMAP di atas rata-rata 12 bulan) dan
   **bulan kering** (di bawah rata-rata) — tampilkan dalam dua list terpisah
6. Simpan tabel klimatologi ke `klimatologi_bulanan.csv`

**Hint:**
- Langkah 1: `df['year'] = df['Date'].dt.year; df['month'] = df['Date'].dt.month`
  lalu `groupby(['year','month'])[sources].sum()`
- Langkah 2: dari hasil langkah 1, `groupby('month')[sources].mean()`
- Jangan gunakan `resample` langsung ke rata-rata — itu melewatkan langkah pertama!
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS
sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# 1. Agregasi harian → total bulanan per tahun (tiap year-month)

# 2. Rata-rata klimatologi per bulan kalender (12 baris)

# 3. Tampilkan tabel klimatologi (dibulatkan 1 desimal)

# 4. Kolom kontribusi_pct untuk GSMAP (% terhadap total tahunan)

# 5. Bulan basah dan bulan kering berdasarkan GSMAP

# 6. Simpan ke klimatologi_bulanan.csv
""",
    "rubric": [
        {"no": 1, "kriteria": "Agregasi dua tahap yang benar: harian→total bulanan per year-month, LALU rata-rata per bulan kalender (bukan langsung rata-rata harian per bulan)", "poin": 35},
        {"no": 2, "kriteria": "Tabel klimatologi 12 baris × 4 sumber dengan nilai masuk akal (pola musim hujan terlihat, total GSMAP ± 1800 mm/tahun)", "poin": 20},
        {"no": 3, "kriteria": "Kolom kontribusi_pct dihitung dengan benar dan 12 nilai total ≈ 100 %", "poin": 20},
        {"no": 4, "kriteria": "Bulan basah dan kering diidentifikasi menggunakan threshold rata-rata 12 bulan dengan benar", "poin": 15},
        {"no": 5, "kriteria": "Hasil disimpan ke CSV dengan nama file yang benar", "poin": 10},
    ],
}

_P2T2 = {
    "no": 2,
    "title": "Hujan Tahunan dan Anomali Iklim",
    "description": """\
## Soal 2 — Hujan Tahunan dan Anomali Iklim

**Curah hujan tahunan** adalah akumulasi total dalam satu tahun kalender.
**Anomali** adalah simpangan dari rata-rata jangka panjang:
nilai **positif** → tahun basah, **negatif** → tahun kering.

**Kerjakan:**
1. Hitung **total curah hujan tahunan** (mm/tahun) untuk semua 4 sumber —
   tampilkan tabel lengkap 22 tahun (2001–2022)
2. Hitung **rata-rata jangka panjang** tiap sumber, lalu hitung
   **anomali tahunan**: `anomali = hujan_tahunan − rata_jangka_panjang`
3. Untuk sumber **GSMAP**, buat tabel dengan kolom:
   `year`, `GSMAP`, `anomali`, `status` (isi `'Basah'` jika anomali > 0, `'Kering'` jika ≤ 0)
4. Bandingkan **rata-rata dekade**: 2001–2011 vs 2012–2022 untuk semua sumber.
   Hitung selisih (mm/tahun) dan persentase perubahan antar dekade.
5. Tentukan **3 tahun terkering** dan **3 tahun terbasah** berdasarkan rata-rata ensemble
   (rata-rata 4 sumber per tahun)
6. Simpan tabel hujan tahunan semua sumber ke `hujan_tahunan.csv`

**Hint:**
- `df.groupby(df['Date'].dt.year)[sources].sum()`
- Ensemble per tahun: `df_tahunan[sources].mean(axis=1)`
- Dekade 2001–2011 = 11 tahun, 2012–2022 = 11 tahun
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS
sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# 1. Total curah hujan tahunan semua sumber (tabel 22 tahun)

# 2. Rata-rata jangka panjang dan anomali tahunan

# 3. Tabel GSMAP: year, GSMAP, anomali, status Basah/Kering

# 4. Perbandingan rata-rata dekade 2001-2011 vs 2012-2022 (selisih & % perubahan)

# 5. 3 tahun terkering dan 3 tahun terbasah (berdasarkan ensemble)

# 6. Simpan ke hujan_tahunan.csv
""",
    "rubric": [
        {"no": 1, "kriteria": "Total hujan tahunan per sumber dihitung dengan benar (groupby tahun + sum) dan tabel 22 tahun ditampilkan", "poin": 20},
        {"no": 2, "kriteria": "Anomali dihitung sebagai selisih dari rata-rata jangka panjang (bukan median/mode) dan hasilnya logis (ada positif dan negatif)", "poin": 25},
        {"no": 3, "kriteria": "Tabel GSMAP memiliki kolom year, GSMAP, anomali, status dengan label Basah/Kering yang benar", "poin": 20},
        {"no": 4, "kriteria": "Perbandingan dekade menghasilkan selisih (mm/tahun) DAN persentase perubahan yang benar untuk semua sumber", "poin": 20},
        {"no": 5, "kriteria": "3 tahun terkering dan 3 terbasah diidentifikasi berdasarkan rata-rata ensemble (mean axis=1) dengan benar", "poin": 15},
    ],
}

_P2T3 = {
    "no": 3,
    "title": "AMS/HMT — Restrukturisasi Data & Periode Ulang Weibull",
    "description": """\
## Soal 3 — AMS/HMT: Restrukturisasi Data dan Periode Ulang Weibull

**Annual Maximum Series (AMS)** adalah fondasi analisis frekuensi hidrologi.
Pada soal ini kamu akan menyusun ulang data AMS ke format yang siap
digunakan dalam analisis distribusi frekuensi.

**Kerjakan:**
1. Hitung **AMS** (nilai hujan harian maksimum tiap tahun) untuk semua sumber —
   tampilkan tabel wide (22 baris × 4 sumber)
2. Ubah format tabel AMS dari **wide → long** menggunakan `melt()`:
   hasil harus memiliki kolom `year`, `source`, `HMT`
3. Untuk tiap sumber, tambahkan kolom **rank** (peringkat):
   rank 1 = HMT terbesar, rank 22 = HMT terkecil
   *(gunakan `groupby('source')` + `.rank(ascending=False, method='first')`)*
4. Hitung **periode ulang Weibull**: `T = (n + 1) / m`
   di mana `n = 22` (jumlah tahun) dan `m` = rank
5. Tampilkan **10 baris dengan HMT terbesar** (dari semua sumber gabungan)
6. Tentukan **nilai HMT rancangan T = 10 tahun** untuk tiap sumber:
   pilih baris dengan rank paling mendekati `(22 + 1) / 10 = 2.3` → rank 2
7. Simpan tabel long + rank + periode ulang ke `AMS_weibull.csv`

**Hint:**
- `df_ams.reset_index().melt(id_vars='year', value_vars=sources, var_name='source', value_name='HMT')`
- Setelah rank: `df_long['T'] = (22 + 1) / df_long['rank']`
- T = 10 tahun → rank = 2 (nilai terbesar kedua tiap sumber)
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS
sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# 1. Hitung AMS (max harian per tahun) semua sumber — format wide

# 2. Ubah ke format long dengan melt(): kolom year, source, HMT

# 3. Tambahkan kolom rank per sumber (rank 1 = terbesar)

# 4. Hitung periode ulang Weibull: T = (n+1) / rank

# 5. Tampilkan 10 baris dengan HMT terbesar (semua sumber)

# 6. Nilai HMT rancangan T = 10 tahun per sumber

# 7. Simpan ke AMS_weibull.csv
""",
    "rubric": [
        {"no": 1, "kriteria": "AMS dihitung dengan benar (groupby tahun + max) dan tabel wide 22×4 ditampilkan", "poin": 15},
        {"no": 2, "kriteria": "Konversi wide→long dengan melt() benar: tiga kolom year, source, HMT tanpa baris duplikat atau NaN", "poin": 25},
        {"no": 3, "kriteria": "Rank per sumber dihitung dengan groupby('source') + rank(ascending=False) dan hasilnya 1–22 per sumber", "poin": 20},
        {"no": 4, "kriteria": "Periode ulang Weibull T = (n+1)/m dihitung dengan n=22 yang benar", "poin": 15},
        {"no": 5, "kriteria": "Nilai HMT rancangan T=10 tahun diidentifikasi dengan benar (rank 2 per sumber) dan disajikan untuk semua sumber", "poin": 15},
        {"no": 6, "kriteria": "Tabel disimpan ke CSV dengan nama file yang benar", "poin": 10},
    ],
}

_P2T4 = {
    "no": 4,
    "title": "Visualisasi — Presentasi Data Hujan",
    "description": """\
## Soal 4 — Visualisasi: Presentasi Data Hujan

Visualisasi yang tepat adalah kunci komunikasi data hidrologi.
Buat **tiga grafik** berikut menggunakan `matplotlib`.
Setiap grafik harus disiapkan dari data mentah `df` — bukan nilai hard-coded.

---

### Grafik 1 — Klimatologi Bulanan GSMAP (Bar Chart)
- Hitung klimatologi bulanan GSMAP dengan **dua langkah** (daily→monthly sum, lalu mean per bulan kalender)
- Bar chart: sumbu-x = nama bulan pendek (`Jan`–`Des`), sumbu-y = curah hujan (mm)
- Warnai bar **biru** untuk bulan basah (di atas rata-rata 12 bulan) dan **oranye** untuk bulan kering
- Tambahkan **garis putus-putus horizontal** pada nilai rata-rata 12 bulan

### Grafik 2 — Seri Waktu Hujan Tahunan (Line Plot)
- Hitung total curah hujan tahunan untuk **semua 4 sumber**
- Line plot: sumbu-x = tahun 2001–2022, semua sumber dalam **satu figure**
- Tambahkan **garis putus-putus horizontal** rata-rata ensemble (mean 4 sumber, 22 tahun)

### Grafik 3 — Distribusi AMS per Sumber (Box Plot)
- Hitung AMS semua sumber
- Box plot: **4 sumber berdampingan** dalam satu figure
- Tambahkan label nilai median di atas tiap box menggunakan `ax.text()` atau `annotate()`

---

**Syarat umum semua grafik:**
- `figsize` minimal `(10, 5)`
- Judul (`title`), label sumbu-x dan sumbu-y yang informatif
- Legend (bila ada lebih dari satu seri data)
- `plt.tight_layout()` dan `plt.show()` di akhir tiap grafik
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS
import matplotlib.pyplot as plt
import numpy as np
sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']
bulan = ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agu','Sep','Okt','Nov','Des']

# === Grafik 1: Bar Chart Klimatologi Bulanan GSMAP ===
# (hitung data terlebih dahulu, lalu plot)

# === Grafik 2: Line Plot Hujan Tahunan Semua Sumber ===
# (hitung data terlebih dahulu, lalu plot)

# === Grafik 3: Box Plot Distribusi AMS per Sumber ===
# (hitung data terlebih dahulu, lalu plot)
""",
    "rubric": [
        {"no": 1, "kriteria": "Grafik 1 (bar chart): data klimatologi dihitung dua langkah dengan benar, pewarnaan basah/kering tepat, garis rata-rata ada, label & judul lengkap", "poin": 35},
        {"no": 2, "kriteria": "Grafik 2 (line plot): 4 sumber ditampilkan dalam satu figure dengan legend, garis rata-rata ensemble ada, label sumbu & judul benar", "poin": 30},
        {"no": 3, "kriteria": "Grafik 3 (box plot): 4 sumber berdampingan, anotasi median ditampilkan, label & judul informatif", "poin": 20},
        {"no": 4, "kriteria": "Semua grafik memenuhi syarat teknis: figsize ≥ (10,5), xlabel, ylabel, title, tight_layout(), show()", "poin": 15},
    ],
}

_P2T5 = {
    "no": 5,
    "title": "Eksplorasi Multi-Sumber Satelit: Bias & Konsistensi",
    "description": """\
## Soal 5 — Eksplorasi Multi-Sumber Satelit: Bias dan Konsistensi

Setiap produk satelit memiliki karakteristik unik dalam merekam curah hujan.
Memahami pola bias dan konsistensi antar produk penting sebelum memilih
sumber untuk pemodelan hidrologi DAS.

**Kerjakan:**
1. Hitung **klimatologi bulanan** untuk semua 4 sumber (dua langkah: total bulanan per tahun → rata-rata per bulan kalender).
   Susun sebagai **tabel pivot** 12 baris × 4 kolom sumber (baris = bulan 1–12)
2. Tambahkan kolom `ensemble_mean`: rata-rata 4 sumber per bulan kalender
3. Hitung **bias relatif bulanan** (%) tiap sumber terhadap ensemble:
   `bias_pct = (sumber − ensemble_mean) / ensemble_mean × 100`
   Tampilkan tabel bias 12 × 4 (dibulatkan 1 desimal)
4. Hitung **Koefisien Variasi inter-sumber** per bulan (variabilitas antar-produk):
   `CV (%) = std(4 sumber) / mean(4 sumber) × 100` dihitung per baris (per bulan)
   — Identifikasi **3 bulan paling tidak konsisten** (CV tertinggi)
5. Buat **tabel ringkasan per sumber** dengan kolom:
   `mean_annual` (mm/tahun), `std_annual` (std total tahunan 22 tahun),
   `CV_tahunan` (%), `total_bias_abs` (jumlah nilai absolut bias 12 bulan)
6. Berdasarkan `total_bias_abs` **terkecil**, simpulkan sumber yang paling konsisten
   dengan ensemble — cetak kesimpulan dengan `print()` yang menyebut nama sumber
   dan angka pendukungnya

**Hint:**
- `df_klim[sources].std(axis=1)` → std antar sumber per bulan (1 nilai per baris)
- `df_klim[sources].mean(axis=1)` → ensemble mean per bulan
- `df_tahunan[sources].std()` → std total tahunan tiap sumber (22 data points)
""",
    "starter_code": """\
# Dataset tersedia sebagai variabel `df`
# Kolom: Date, GSMAP, GPM, PERSIANN, CHIRPS
sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# 1. Klimatologi bulanan (dua langkah) → tabel pivot 12×4

# 2. Tambahkan kolom ensemble_mean

# 3. Bias relatif bulanan (%) per sumber terhadap ensemble

# 4. CV inter-sumber per bulan dan 3 bulan paling tidak konsisten

# 5. Tabel ringkasan per sumber: mean_annual, std_annual, CV_tahunan, total_bias_abs

# 6. Kesimpulan sumber paling konsisten berdasarkan total_bias_abs terkecil
""",
    "rubric": [
        {"no": 1, "kriteria": "Klimatologi dihitung dua langkah yang benar dan tabel pivot 12×4 tersusun rapi", "poin": 20},
        {"no": 2, "kriteria": "Bias relatif (%) dihitung dengan rumus yang benar dan ditampilkan sebagai tabel 12×4", "poin": 25},
        {"no": 3, "kriteria": "CV inter-sumber per bulan dihitung dengan std/mean axis=1 yang benar dan 3 bulan paling tidak konsisten teridentifikasi", "poin": 25},
        {"no": 4, "kriteria": "Tabel ringkasan per sumber memiliki semua kolom yang diminta (mean_annual, std_annual, CV_tahunan, total_bias_abs) dengan nilai yang benar", "poin": 15},
        {"no": 5, "kriteria": "Kesimpulan menyebut nama sumber secara eksplisit dan didukung angka total_bias_abs dari data yang dihitung", "poin": 15},
    ],
}

# ── Paket 3: Pemanasan & Soal Sederhana untuk Mahasiswa Pemula ───────────────

_P3T1 = {
    "no": 1,
    "title": "Pemanasan: Lihat Data & Ringkasan Singkat",
    "description": """\
## Soal 1 — Pemanasan: Lihat Data & Ringkasan

Kerjakan:
1. Tampilkan 5 baris pertama dataset (`head()`)
2. Tampilkan 3 baris terakhir dataset (`tail()`)
3. Cetak daftar nama kolom
4. Cetak jumlah baris (n) dalam dataset

Tujuan: latihan dasar penggunaan `pandas` dan pemahaman struktur data.
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`

# 1. head

# 2. tail

# 3. daftar kolom

# 4. jumlah baris
""",
    "rubric": [
        {"no": 1, "kriteria": "Menampilkan 5 baris pertama dengan head()", "poin": 25},
        {"no": 2, "kriteria": "Menampilkan 3 baris terakhir dengan tail()", "poin": 25},
        {"no": 3, "kriteria": "Mencetak daftar kolom (kolom Date + 4 sumber)", "poin": 25},
        {"no": 4, "kriteria": "Mencetak jumlah baris dataset (≈ 8036)", "poin": 25},
    ],
}

_P3T2 = {
    "no": 2,
    "title": "Pemanasan: Tipe Data & Missing Values",
    "description": """\
## Soal 2 — Pemanasan: Tipe Data & Missing Values

Kerjakan:
1. Pastikan kolom `Date` bertipe `datetime` (gunakan `pd.to_datetime` bila perlu)
2. Hitung jumlah missing value per sumber
3. Hitung persentase missing per sumber (round 2 desimal)
4. Isi missing values sementara dengan `fillna(0)` dan tampilkan statistik mean per sumber

Hint: gunakan `df['Date'] = pd.to_datetime(df['Date'])` dan `df.isnull().sum()`
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`

# 1. pastikan Date datetime

# 2. jumlah missing per sumber

# 3. persentase missing per sumber

# 4. fillna(0) lalu tampilkan mean per sumber
""",
    "rubric": [
        {"no": 1, "kriteria": "Kolom Date dipastikan datetime", "poin": 25},
        {"no": 2, "kriteria": "Jumlah missing per sumber dihitung benar", "poin": 25},
        {"no": 3, "kriteria": "Persentase missing per sumber dihitung dan dibulatkan", "poin": 25},
        {"no": 4, "kriteria": "Fillna(0) digunakan sementara dan mean per sumber ditampilkan", "poin": 25},
    ],
}

_P3T3 = {
    "no": 3,
    "title": "Agregasi Bulanan Sederhana",
    "description": """\
## Soal 3 — Agregasi Bulanan (Substansi Dimulai)

Kerjakan:
1. Buat kolom `year` dan `month` dari `Date`
2. Hitung total curah hujan bulanan (`groupby(['year','month']).sum()`) untuk sumber `GSMAP`
3. Tampilkan total bulanan untuk tahun pertama (2001)

Hint: jika kesulitan, gunakan `df.set_index('Date').resample('M').sum()` lalu pilih tahun 2001.
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`

# 1. buat year dan month

# 2. hitung total bulanan GSMAP

# 3. tampilkan total bulanan tahun 2001
""",
    "rubric": [
        {"no": 1, "kriteria": "Kolom year dan month dibuat dengan benar", "poin": 30},
        {"no": 2, "kriteria": "Total bulanan GSMAP dihitung dengan benar", "poin": 40},
        {"no": 3, "kriteria": "Menampilkan 12 baris untuk tahun 2001", "poin": 30},
    ],
}

_P3T4 = {
    "no": 4,
    "title": "HMT Sederhana",
    "description": """\
## Soal 4 — HMT Sederhana

Kerjakan:
1. Hitung HMT (nilai maksimum harian tiap tahun) untuk `GSMAP`
2. Tampilkan 5 tahun dengan HMT tertinggi beserta tahunnya
3. Berikan satu kalimat pendek: tahun mana yang paling ekstrem (print saja)

Hint: `df.groupby(df['Date'].dt.year)['GSMAP'].max()`
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`

# 1. hitung HMT GSMAP

# 2. tampilkan 5 tahun teratas

# 3. print kalimat hasil
""",
    "rubric": [
        {"no": 1, "kriteria": "HMT per tahun untuk GSMAP dihitung benar", "poin": 40},
        {"no": 2, "kriteria": "5 tahun dengan HMT tertinggi ditampilkan benar", "poin": 40},
        {"no": 3, "kriteria": "Kalimat singkat tentang tahun ekstrem diprint", "poin": 20},
    ],
}

_P3T5 = {
    "no": 5,
    "title": "Plot Sederhana: Seri Tahunan GSMAP",
    "description": """\
## Soal 5 — Plot Sederhana

Kerjakan:
1. Hitung total curah hujan tahunan untuk `GSMAP`
2. Buat line plot tahun vs total (gunakan `plt.plot`), beri judul dan label sumbu
3. Simpan plot ke file `plot_gsmap_tahunan.png` (gunakan `plt.savefig`)

Hint: gunakan `matplotlib` bawaan; jika belum terbiasa, lakukan langkah per langkah: hitung data → print → plot.
""",
    "starter_code": """\
import matplotlib.pyplot as plt

# 1. hitung total tahunan GSMAP

# 2. plot line sederhana

# 3. simpan ke file plot_gsmap_tahunan.png
""",
    "rubric": [
        {"no": 1, "kriteria": "Total tahunan GSMAP dihitung benar", "poin": 30},
        {"no": 2, "kriteria": "Line plot dibuat dengan label & judul", "poin": 40},
        {"no": 3, "kriteria": "Plot disimpan dengan nama file yang benar", "poin": 30},
    ],
}

# ── Paket 4: Ujian Praktikum Hidrologi ──────────────────────────────────────

_P4T1 = {
    "no": 1,
    "title": "Pemanasan: Baca Data Hujan & Struktur Dasar",
    "description": """\
## Soal 1 — Pemanasan: Membaca Data Hujan & Struktur Dasar

Dataset curah hujan harian dari **1 stasiun pengukuran** periode **10 tahun** (2013–2022)
sudah tersedia sebagai variabel `df`.

| Kolom | Keterangan |
|-------|-----------|
| `tanggal` | Tanggal pengukuran (datetime) |
| `hujan` | Curah hujan harian (mm/hari) |

**Kerjakan:**
1. Tampilkan **10 baris pertama** data
2. Tampilkan **informasi kolom** (`df.info()`)
3. Cetak **jumlah baris** dataset
4. Hitung **statistik ringkas**: min, max, mean, median, std untuk kolom `hujan`
5. Periksa **jumlah hari dengan hujan = 0** (hari kering)
6. Periksa **jumlah missing values** di kolom `hujan`

**Tujuan**: Memahami struktur data, tipe kolom, dan karakter dasar dataset hujan.
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: tanggal (datetime), hujan (float, mm/hari)

# 1. Tampilkan 10 baris pertama

# 2. Tampilkan df.info()

# 3. Jumlah baris

# 4. Statistik ringkas (min, max, mean, median, std)

# 5. Jumlah hari kering (hujan = 0)

# 6. Missing values
""",
    "rubric": [
        {"no": 1, "kriteria": "Menampilkan 10 baris pertama dengan head()", "poin": 15},
        {"no": 2, "kriteria": "Menampilkan info() dengan tipe data yang benar", "poin": 15},
        {"no": 3, "kriteria": "Mencetak jumlah baris dengan shape atau len()", "poin": 15},
        {"no": 4, "kriteria": "Menampilkan statistik min, max, mean, median, std dengan nilai yang masuk akal", "poin": 30},
        {"no": 5, "kriteria": "Menghitung hari kering dengan query atau boolean masking", "poin": 15},
        {"no": 6, "kriteria": "Memeriksa missing values dengan isnull().sum()", "poin": 10},
    ],
}

_P4T2 = {
    "no": 2,
    "title": "Pemanasan: Tipe Data & Data Cleaning Dasar",
    "description": """\
## Soal 2 — Pemanasan: Tipe Data & Data Cleaning Dasar

Sebelum analisis, dataset hujan harus dipastikan bersih dari error tipe data dan nilai ekstrem.

**Kerjakan:**
1. Pastikan kolom `tanggal` bertipe `datetime` (jika belum, konversi dengan `pd.to_datetime()`)
2. Isi **missing values** di kolom `hujan` dengan **interpolasi linear** (`interpolate(method='linear')`)
   — verifikasi tidak ada NaN tersisa
3. Periksa **nilai negatif** di kolom `hujan` (curah hujan tidak boleh negatif)
   — tampilkan baris yang memiliki nilai negatif (bila ada)
4. Untuk **nilai negatif**, ganti dengan **0** menggunakan `clip(lower=0)`
5. Hitung dan tampilkan **ringkasan cleaning**: jumlah missing original, jumlah negatif original,
   total baris sebelum dan sesudah cleaning

**Tujuan**: Memastikan data hidrologi valid dan siap untuk agregasi dan analisis.
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: tanggal (datetime), hujan (float, mm/hari)

# 1. Pastikan tanggal bertipe datetime

# 2. Isi missing values dengan interpolasi linear

# 3. Periksa nilai negatif (tampilkan baris jika ada)

# 4. Ganti nilai negatif dengan 0 menggunakan clip()

# 5. Ringkasan cleaning (print hasil)
""",
    "rubric": [
        {"no": 1, "kriteria": "Kolom tanggal dikonversi/dipastikan sebagai datetime", "poin": 15},
        {"no": 2, "kriteria": "Missing values diisi dengan interpolasi linear dan verifikasi 0 missing tersisa", "poin": 25},
        {"no": 3, "kriteria": "Nilai negatif dideteksi dan ditampilkan (jika ada)", "poin": 15},
        {"no": 4, "kriteria": "Nilai negatif diganti 0 dengan clip(lower=0)", "poin": 25},
        {"no": 5, "kriteria": "Ringkasan cleaning ditampilkan dengan informasi yang lengkap", "poin": 20},
    ],
}

_P4T3 = {
    "no": 3,
    "title": "Hujan Maksimum Harian Tahunan (HMT) & Analisis Ekstrem",
    "description": """\
## Soal 3 — Hujan Maksimum Harian Tahunan (HMT) & Analisis Ekstrem

**Hujan Maksimum Harian Tahunan (HMT)** adalah nilai curah hujan harian tertinggi tiap tahun.
Ini adalah data dasar untuk analisis banjir dan desain infrastruktur air.

**Kerjakan:**
1. Buat kolom `tahun` dari kolom `tanggal`
2. Hitung **HMT** (nilai maksimum harian tiap tahun) untuk semua 10 tahun (2013–2022)
   — tampilkan tabel dengan kolom `tahun` dan `HMT` (dibulatkan 1 desimal)
3. Tentukan **tahun dengan HMT tertinggi** (banjir terparah) dan **HMT terendah** (tahun teraman)
   — tampilkan tahun dan nilai HMT
4. Hitung **rata-rata HMT** selama 10 tahun dan **deviasi standar HMT**
5. Dari rata-rata HMT, tentukan **tahun ekstrem** (HMT di atas rata-rata + 1 std):
   tampilkan daftar tahun-tahun ekstrem
6. Simpan tabel HMT ke file CSV: `HMT_stasiun.csv` (kolom: tahun, HMT)

**Tujuan**: Memahami variabilitas hujan ekstrem tahunan dan periode banjir kritis.
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: tanggal (datetime), hujan (float, mm/hari)

# 1. Buat kolom tahun dari tanggal

# 2. Hitung HMT per tahun dan tampilkan tabel

# 3. Tahun dengan HMT tertinggi dan terendah

# 4. Rata-rata dan standar deviasi HMT

# 5. Tahun-tahun ekstrem (HMT > mean + 1*std)

# 6. Simpan ke HMT_stasiun.csv
""",
    "rubric": [
        {"no": 1, "kriteria": "Kolom tahun dibuat dengan benar dari tanggal", "poin": 10},
        {"no": 2, "kriteria": "HMT dihitung dengan groupby('tahun').max() yang benar, tabel 10 tahun ditampilkan", "poin": 25},
        {"no": 3, "kriteria": "Tahun ekstrem tertinggi dan terendah diidentifikasi dengan benar", "poin": 20},
        {"no": 4, "kriteria": "Rata-rata dan std HMT dihitung dengan benar", "poin": 15},
        {"no": 5, "kriteria": "Tahun ekstrem (> mean+1std) teridentifikasi dan ditampilkan dengan benar", "poin": 20},
        {"no": 6, "kriteria": "Tabel HMT disimpan ke CSV dengan nama file yang benar", "poin": 10},
    ],
}

_P4T4 = {
    "no": 4,
    "title": "Agregasi Bulanan & Klimatologi untuk Ketersediaan Air",
    "description": """\
## Soal 4 — Agregasi Bulanan & Klimatologi untuk Ketersediaan Air

**Ketersediaan air** dievaluasi melalui pola curah hujan bulanan dan klimatologi bulanan.
Pola ini penting untuk perencanaan irigasi, pasokan air minum, dan manajemen DAS.

**Kerjakan:**
1. Buat kolom `tahun` dan `bulan` dari kolom `tanggal`
2. Hitung **total curah hujan bulanan** (mm/bulan) untuk setiap kombinasi tahun-bulan
   — gunakan `groupby(['tahun','bulan']).sum()`
3. Dari data bulanan, hitung **klimatologi** (rata-rata jangka panjang per bulan kalender):
   ambil rata-rata semua Januari (10 nilai), semua Februari (10 nilai), dst.
   — tabel hasil: 12 baris × 2 kolom (`bulan`, `hujan_klimatologi`)
4. Identifikasi **bulan basah** (di atas rata-rata 12 bulan) dan **bulan kering**
   — tampilkan daftar bulan basah dan bulan kering
5. Hitung **total curah hujan tahunan** (mm/tahun) untuk 10 tahun
   — tentukan **tahun dengan ketersediaan air terbaik** dan **terburuk**
6. Simpan tabel bulanan ke `hujan_bulanan.csv` dan klimatologi ke `klimatologi.csv`

**Tujuan**: Memahami pola ketersediaan air intra-annual dan inter-annual untuk manajemen DAS.

**Hint:**
- Langkah 2: `df.groupby([df['tanggal'].dt.year, df['tanggal'].dt.month])['hujan'].sum()`
- Langkah 3: dari hasil langkah 2, `groupby('bulan')['hujan'].mean()`
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: tanggal (datetime), hujan (float, mm/hari)

# 1. Buat kolom tahun dan bulan

# 2. Hitung total bulanan per tahun-bulan

# 3. Hitung klimatologi (rata-rata per bulan kalender)

# 4. Bulan basah dan bulan kering

# 5. Total tahunan dan tahun terbaik/terburuk ketersediaan air

# 6. Simpan ke hujan_bulanan.csv dan klimatologi.csv
""",
    "rubric": [
        {"no": 1, "kriteria": "Kolom tahun dan bulan dibuat dengan benar", "poin": 10},
        {"no": 2, "kriteria": "Total bulanan dihitung dengan groupby dua kolom yang benar", "poin": 25},
        {"no": 3, "kriteria": "Klimatologi dihitung sebagai rata-rata per bulan (12 baris) dengan nilai yang masuk akal", "poin": 25},
        {"no": 4, "kriteria": "Bulan basah dan kering diidentifikasi dengan threshold rata-rata 12 bulan", "poin": 15},
        {"no": 5, "kriteria": "Total tahunan dihitung dan tahun terbaik/terburuk ketersediaan teridentifikasi", "poin": 15},
        {"no": 6, "kriteria": "Kedua file CSV disimpan dengan nama yang benar", "poin": 10},
    ],
}

_P4T5 = {
    "no": 5,
    "title": "Visualisasi Komprehensif: Presentasi Data Hujan Stasiun",
    "description": """\
## Soal 5 — Visualisasi Komprehensif: Presentasi Data Hujan Stasiun

Buat **tiga grafik** yang merangkum hasil analisis dari Soal 1–4 menggunakan `matplotlib`.
Setiap grafik harus dihitung dari data mentah `df` dan disajikan dengan format profesional.

---

### Grafik 1 — Seri Waktu Hujan Harian (30 hari pertama)
- Plot nilai hujan harian (mm/hari) untuk 30 hari pertama dataset
- Gunakan **line plot** dengan marker kecil (marker='o', markersize=3)
- Warnai sumbu-x dengan label hari-tanggal yang terbaca
- Tambahkan **garis putus-putus horizontal** pada nilai 1 mm (threshold hujan/kering)
- Judul: "Seri Waktu Hujan Harian — 30 Hari Pertama"

### Grafik 2 — Distribusi Hujan Harian (Histogram)
- Buat histogram dari **seluruh data harian** (`df['hujan']`, semua ~8000 hari)
- Gunakan 50 bin untuk menampilkan distribusi detail
- Warna histogram: biru; edge color: gelap
- Tambahkan label: jumlah total hari pengamatan di title
- Judul: "Distribusi Hujan Harian: Frekuensi Kejadian (2001–2022)"

### Grafik 3 — Total Hujan Tahunan (Bar Chart)
- Hitung total hujan per tahun (22 tahun × 1 kolom)
- Buat bar chart tahun vs total (warna: steelblue atau biru tua)
- Tambahkan **garis putus-putus horizontal** pada nilai rata-rata semua tahun
- Highlightkan tahun dengan total **tertinggi** dan **terendah** dengan warna berbeda (merah & hijau)
- Judul: "Total Curah Hujan Tahunan dengan Identifikasi Tahun Ekstrem"

---

**Syarat umum semua grafik:**
- `figsize` minimal `(10, 5)` per grafik (atau `(14, 12)` jika 3 subplot dalam 1 figure)
- Judul (`title`), label sumbu-x, sumbu-y, unit (mm/hari atau mm/tahun) yang informatif
- Legend jika ada lebih dari satu seri
- `plt.tight_layout()` sebelum `plt.show()`
- Simpan setiap grafik ke file PNG: `grafik_1.png`, `grafik_2.png`, `grafik_3.png`
""",
    "starter_code": """\
# Dataset tersedia sebagai `df`
# Kolom: Date (datetime), hujan (float, mm/hari)
import matplotlib.pyplot as plt
import pandas as pd

sources = ['GSMAP', 'GPM', 'PERSIANN', 'CHIRPS']

# === Grafik 1: Seri Waktu Harian (30 hari pertama) ===

# === Grafik 2: Histogram Distribusi Hujan Harian ===

# === Grafik 3: Bar Chart Total Tahunan ===
""",
    "rubric": [
        {"no": 1, "kriteria": "Grafik 1 (seri 30 hari): line plot dengan marker, garis threshold 1mm, label tanggal, judul lengkap", "poin": 25},
        {"no": 2, "kriteria": "Grafik 2 (histogram): 50 bin, distribusi seluruh data (~8000 hari), label frekuensi, judul informatif", "poin": 25},
        {"no": 3, "kriteria": "Grafik 3 (bar chart tahunan): 22 tahun, garis rata-rata, tahun ekstrem diwarnai berbeda (merah/hijau), judul jelas", "poin": 25},
        {"no": 4, "kriteria": "Semua grafik memenuhi syarat: figsize ≥ (10,5), xlabel, ylabel dengan unit, title, tight_layout, disimpan ke PNG", "poin": 25},
    ],
}


# ── Exam Packages ────────────────────────────────────────────────────────────

PACKAGES = {
    1: {
        "id": 1,
        "name": "Paket 1 (Pemula)",
        "subtitle": "Soal Dasar untuk Mahasiswa TSDA",
        "description": "Paket ringan: membaca data, tipe & missing values, agregasi bulanan sederhana, HMT dasar, dan plot sederhana.",
        "tasks": [_P3T1, _P3T2, _P3T3, _P3T4, _P3T5],
    },
    2: {
        "id": 2,
        "name": "Paket 2",
        "subtitle": "Tipe Data Hidrologi & Read/Write Data Hujan",
        "description": "Eksplorasi, agregasi, HMT, perbandingan sumber, dan data cleaning dataset hujan multi-satelit.",
        "tasks": [_T1, _T2, _T3, _T4, _T5],
    },
    3: {
        "id": 3,
        "name": "Paket 3",
        "subtitle": "Klimatologi, Hujan Tahunan, AMS, Visualisasi & Multi-Sumber",
        "description": "Klimatologi bulanan, anomali hujan tahunan, restrukturisasi AMS + periode ulang Weibull, visualisasi data hujan, dan eksplorasi bias multi-sumber satelit.",
        "tasks": [_P2T1, _P2T2, _P2T3, _P2T4, _P2T5],
    },
    4: {
        "id": 4,
        "name": "Paket 4 (Ujian)",
        "subtitle": "Ujian Algoritma & Pemrograman Komputer",
        "description": "Read/write data, data cleaning, analisis HMT, agregasi klimatologi untuk ketersediaan air, dan visualisasi data hujan (seri waktu, histogram, bar chart).",
        "tasks": [_P4T1, _P4T2, _P4T3, _P4T4, _P4T5],
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
