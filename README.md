# Midterm Project — Visualisasi Data (CAK4XBB3) · Kelompok Cihuy

Analisis & visualisasi **data time series nyata** dalam satu Jupyter Notebook (Python, pandas, numpy, matplotlib/seaborn).
Soal lengkap: [Midterm Project.pdf](Midterm%20Project.pdf)

**Topik:** Pasar Saham & Keuangan
**Sumber data:** Yahoo Finance — https://finance.yahoo.com (via library `yfinance`)
**Periode:** 2 Jan 2020 – 30 Okt 2026, harian (hari kerja)
**Aset (9 aset, 5 kategori):** IHSG, S&P 500 (indeks) · BBCA, BBRI, BMRI, BBNI (saham bank) · Bitcoin (kripto) · Emas (komoditas) · USD/IDR (kurs)

## Anggota

| Nama | NIM |
|------|-----|
| Adhyatma Chrysostomos Davu | 103012340479 |
| Raffa Anung El Haqqi | 103012300163 |
| Tristan Satria Perdana Hermawan | 103012300253 |
| Naufal Rafif Hidayat | 103012300403 |
| Ahmad Naufal Ramadhan | 103012300239 |

## Status

- [x] **Davu** — data sudah diunduh & dibersihkan, kerangka notebook siap (lulus Run All), draf Bab 1–2 di [laporan/Bab1_2_Davu.md](laporan/Bab1_2_Davu.md)
- [ ] Raffa — Line & Area Plot (bagian 3.1–3.2 notebook)
- [ ] Tristan — Multiple Time Series & Seasonal/Heatmap (bagian 3.3–3.4)
- [ ] Naufal Rafif — Moving Average & Fitting (bagian 4)
- [ ] Naufal Ramadhan — Kesimpulan, Deklarasi AI, Daftar Pustaka, laporan, slide, video

## Cara mulai (untuk semua anggota)

1. Install library: `pip install pandas numpy matplotlib seaborn yfinance jupyter`
2. Buka [notebook_timeseries.ipynb](notebook_timeseries.ipynb), jalankan **Run All** dulu sampai bagian 2 selesai.
3. Kerjakan **hanya sel bagianmu** (ada tanda `# TODO <nama>`). Variabel siap pakai dari bagian 2:
   - `close` — harga penutupan harian (kolom = aset)
   - `volume` — volume transaksi harian
   - `ret` — return harian (%)
   - `norm` — harga dinormalisasi, hari pertama = 100
   - `close_m` — harga akhir bulan
   - `WARNA["IHSG"]` dst. — warna tetap per aset (palet Okabe-Ito); `simpan("nama")` — simpan grafik ke `figures/`
4. Data sudah ada di `data/` — **tidak perlu unduh ulang**. Kalau mau update data: `python data/download_data.py`.

---

## Yang harus dikumpulkan

1. **Notebook `.ipynb`** — 1 file per kelompok, harus bisa **Run All tanpa error**
2. **Laporan PDF** 3–5 halaman (Pendahuluan, Dataset, Visualisasi, Analisis Tren, Kesimpulan)
3. **Slide** maks. 10 slide (PDF/PPTX)
4. **Video presentasi** maks. 10 menit
5. **Deklarasi penggunaan AI** (PDF) + prompting yang dipakai (file **gambar** dan **MD**) → lihat folder [Log/](Log/)

### Isi wajib notebook

- **Data:** time series nyata, ada kolom waktu eksplisit, cantumkan nama dataset + URL sumber. **Dilarang data dummy** (nilai Data = 0).
- **4 visualisasi wajib:**
  1. Line Plot — pola utama satu variabel sepanjang waktu
  2. Area Plot — volume/akumulasi (boleh stacked)
  3. Multiple Time Series — min. 2 series dalam 1 grafik, pakai **direct labeling di ujung garis** (bukan legend)
  4. Seasonal Plot **atau** Calendar Heatmap — pola musiman/periodik
- **Analisis tren (wajib, min. 1):**
  - Moving Average dengan **min. 2 window** berbeda (mis. 7 & 30 hari), overlay di atas data asli, jelaskan trade-off kehalusan vs NaN di awal periode
  - dan/atau Fitting model (linear/polynomial/exponential, mis. `numpy.polyfit`) overlay di atas data asli
- **Deklarasi AI** di sel markdown (sebelum daftar pustaka) + tabel rincian — per anggota.

---

## Pembagian Jobdesk

| Anggota | Tugas utama | Di notebook | Di laporan & slide |
|---------|-------------|-------------|--------------------|
| **Davu** (mulai duluan) | Koordinator + Data | Pilih topik & dataset, load data, cleaning, set kolom waktu jadi index, buat **kerangka notebook** (judul, sumber data, bagian-bagian kosong untuk tiap anggota). Di akhir: **gabungkan semua bagian & cek Run All** | Bab 1 Pendahuluan, Bab 2 Dataset |
| **Raffa** | Visualisasi 1 & 2 | Line Plot + Area Plot, plus interpretasi singkat di markdown | Bagian Line & Area di Bab 3 |
| **Tristan** | Visualisasi 3 & 4 | Multiple Time Series (direct labeling) + Seasonal Plot / Calendar Heatmap, plus interpretasi | Bagian Multi Series & Seasonal di Bab 3 |
| **Naufal Rafif** | Analisis Tren | Moving Average (≥2 window) + fitting model (`numpy.polyfit`), penjelasan pilihan parameter & trade-off window vs NaN | Bab 4 Analisis Tren |
| **Naufal Ramadhan** | Laporan, Slide, Video, Deklarasi AI | Sel markdown Deklarasi AI + daftar pustaka di notebook | Menyusun laporan PDF final, slide (≤10), Bab 5 Kesimpulan (min. 5 insight, kendala, rencana pengembangan), edit video, rekap deklarasi AI semua anggota jadi 1 PDF |

**Tugas semua anggota:**
- Tulis insight/penjelasan bagian sendiri, kirim ke Naufal Ramadhan untuk laporan & slide.
- Simpan screenshot grafik bagian sendiri (`figures/`).
- Presentasikan bagian sendiri di video (± 2 menit per orang).
- Isi log AI masing-masing di folder `Log/` (wajib, lihat bawah).
- Paham kode bagian sendiri — bisa ditanya dosen kapan saja.

### Urutan kerja

1. **Davu** — pilih dataset, push notebook kerangka + data yang sudah bersih. Yang lain menunggu ini.
2. **Raffa, Tristan, Naufal Rafif** — kerjakan bagian masing-masing **paralel** di notebook kerangka (masing-masing hanya edit bagiannya sendiri biar tidak bentrok).
3. **Davu** — gabungkan jadi 1 notebook, Restart & Run All, perbaiki error.
4. **Naufal Ramadhan** — susun laporan + slide dari hasil semua anggota (bisa mulai Bab 1–2 sejak langkah 1 selesai).
5. **Semua** — rekam video, Naufal Ramadhan edit & gabungkan.

---

## Folder Log (log AI)

Setiap anggota **wajib** mencatat semua penggunaan AI. Semua file ditaruh langsung di folder `Log/`, nama file dibuat sendiri (yang penting ada nama kamu):

```
Log/
├── log_ai_Davu.md            ← contoh: log Davu (file MD)
├── Screenshot_AI_[NIM]_01.png  ← screenshot percakapan (file gambar)
└── ...
```

Cara isi:
1. Buat file log sendiri di `Log/` (mis. `log_ai_Raffa.md`). Format bebas, boleh minta AI kalian bikinin — lihat `log_ai_Davu.md` sebagai contoh.
2. Tiap sesi chat dengan AI → tambah **satu entri**: tanggal, tools AI, bagian yang dibantu, prompt asli, ringkasan jawaban, apa yang dipakai/diubah.
3. Ambil screenshot percakapan. Harus terlihat: **nama platform AI, prompt, dan jawabannya**. Simpan di `Log/` dengan nama `Screenshot_AI_[NIM]_01.png`, `_02.png`, dst., atau gabung jadi satu PDF `Screenshot_AI_[NIM].pdf` (contoh: punya Davu).
4. Update tabel **Ringkasan** di atas file log — ini yang nanti dipindah ke tabel Deklarasi AI di notebook & PDF.
5. Kalau **tidak pakai AI sama sekali**, tetap tulis "Tidak menggunakan AI" di tabel ringkasan.

> Deklarasi yang tidak sesuai bukti (pakai AI tapi tidak dicatat) dihitung **pelanggaran integritas akademik**. Catat semuanya.

---

## Struktur folder

```
tubes visdat/
├── README.md
├── Midterm Project.pdf    ← soal
├── notebook_timeseries.ipynb  ← notebook utama
├── data/                  ← script unduh + data mentah & bersih (CSV)
├── figures/               ← screenshot grafik untuk laporan & slide
├── laporan/               ← laporan PDF + PDF deklarasi AI
├── slide/                 ← slide presentasi
└── Log/                   ← log AI per anggota
```


## Aturan penting

- Jangan pakai data dummy/karangan.
- Jangan menyalin kelompok lain.
- Notebook harus lulus **Restart & Run All** sebelum dikumpulkan.
- Telat = −5 poin per hari (maks. 3 hari).
