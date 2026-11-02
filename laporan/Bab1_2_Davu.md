# Draf Laporan — Bab 1 & Bab 2
*Ditulis oleh Davu (103012340479). Untuk disalin Naufal Ramadhan ke laporan final.*

---

## BAB 1 — Pendahuluan

### 1.1 Latar Belakang
Sejak 2020, pasar keuangan Indonesia dan global beberapa kali mengalami guncangan besar. Contohnya crash akibat pandemi COVID-19 pada Maret 2020, kenaikan suku bunga global pada 2022, dan reli besar Bitcoin dan emas dalam beberapa tahun terakhir. Harga aset keuangan yang dicatat setiap hari adalah contoh *time series* nyata. Data ini memuat empat komponen utama: **tren** jangka panjang, **pola musiman/periodik**, **siklus** naik-turun pasar, dan **noise** (fluktuasi acak harian).

Kalau hanya berupa tabel angka, pola-pola itu sulit dibaca. Karena itu kelompok kami memakai teknik visualisasi time series untuk mengamati, membandingkan, dan menganalisis tren beberapa kelas aset keuangan selama hampir tujuh tahun.

### 1.2 Tujuan
1. Menggambarkan pola pergerakan utama IHSG selama 2020–2026.
2. Membandingkan kinerja beberapa kelas aset (indeks saham Indonesia dan AS, saham bank besar Indonesia, Bitcoin, emas, dan kurs USD/IDR) dalam satu grafik.
3. Mengidentifikasi pola musiman/periodik pada return aset.
4. Menganalisis tren jangka pendek dan jangka panjang dengan Moving Average dan fitting model.

### 1.3 Ruang Lingkup
- Data harian (hari kerja) dari 2 Januari 2020 sampai 30 Oktober 2026.
- 9 aset dari 5 kategori, semuanya diambil dari Yahoo Finance.
- Analisis bersifat deskriptif dan visual, bukan prediksi atau rekomendasi investasi.

---

## BAB 2 — Dataset

### 2.1 Sumber Data
Data harga harian diambil dari **Yahoo Finance** (https://finance.yahoo.com) dengan library Python `yfinance`, diakses pada 2 November 2026. Setiap baris data mentah berisi tanggal, ticker, dan harga **Open, High, Low, Close**, serta **Volume**. Harga sudah disesuaikan (*adjusted*) terhadap stock split dan dividen.

| Kategori | Ticker | Nama | Satuan |
|----------|--------|------|--------|
| Indeks | ^JKSE | IHSG | poin |
| Indeks | ^GSPC | S&P 500 | poin |
| Saham Bank | BBCA.JK | Bank Central Asia | IDR |
| Saham Bank | BBRI.JK | Bank Rakyat Indonesia | IDR |
| Saham Bank | BMRI.JK | Bank Mandiri | IDR |
| Saham Bank | BBNI.JK | Bank Negara Indonesia | IDR |
| Kripto | BTC-USD | Bitcoin | USD |
| Komoditas | GC=F | Emas (futures) | USD/troy ounce |
| Kurs | IDR=X | USD/IDR | IDR per USD |

Data mentah berjumlah **15.936 baris** (format *long*: satu baris per aset per tanggal).

### 2.2 Karakteristik Data
- **Kolom waktu:** `Date` (harian), dijadikan *index* bertipe `DatetimeIndex`.
- **Kalender berbeda-beda:**
  - Bitcoin diperdagangkan 7 hari seminggu (2.496 hari).
  - Saham Indonesia hanya buka di hari bursa BEI (1.645 hari).
  - S&P 500 dan emas mengikuti hari bursa AS (± 1.720 hari).
  - Kurs tersedia setiap hari kerja (1.778 hari).
- **Volume:** kurs USD/IDR tidak memiliki data volume di Yahoo Finance (selalu 0).

### 2.3 Data Cleaning
1. **Format long diubah ke wide.** Setiap aset menjadi satu kolom, tanggal menjadi index.
2. **Kalender disamakan ke hari kerja (Senin–Jumat).** Data Bitcoin di akhir pekan dibuang supaya semua aset bisa dibandingkan pada tanggal yang sama.
3. **Hari libur bursa diisi dengan harga penutupan terakhir** (*forward fill*, maksimal 5 hari). Saat bursa tutup harga memang tidak berubah, jadi ini bukan data karangan.
4. **Volume di hari libur diisi 0**, karena memang tidak ada transaksi.
5. **Cek kualitas data.** Hasilnya: tidak ada tanggal duplikat, index terurut, dan sisa missing value = 0.

**Hasil akhir:** 1.778 hari kerja × 9 aset.

### 2.4 Statistik Deskriptif (Data Profiling)
Return harian (%) dihitung sebagai perubahan harga penutupan dari hari sebelumnya.

| Aset | Rata-rata return harian (%) | Std (%) | Return terburuk (%) | Return terbaik (%) | Return total 2020–2026 (%) |
|------|-----:|-----:|-----:|-----:|-----:|
| IHSG | −0,01 | 1,17 | −11,57 | 10,19 | −19,5 |
| S&P 500 | 0,06 | 1,25 | −11,98 | 9,52 | +132,7 |
| BBCA | 0,01 | 1,73 | −14,81 | 17,33 | −9,5 |
| BBRI | 0,02 | 2,09 | −14,84 | 20,49 | +4,5 |
| BMRI | 0,05 | 2,13 | −14,82 | 15,80 | +49,8 |
| BBNI | 0,03 | 2,17 | −12,90 | 13,65 | +16,8 |
| Bitcoin | 0,20 | 3,70 | −37,17 | 21,11 | +1.005,1 |
| Emas | 0,06 | 1,19 | −10,78 | 6,07 | +155,8 |
| USD/IDR | 0,02 | 0,71 | −5,64 | 7,43 | +32,0 |

**Temuan awal dari data profiling:**
- **Bitcoin** paling volatil (std 3,70% per hari, lebih dari 3× IHSG) sekaligus memberi return total tertinggi (± 11× lipat).
- **IHSG** turun ± 19,5% selama periode ini. Sebaliknya, S&P 500 naik ± 133% dan emas ± 156%.
- **Rupiah melemah ± 32%** terhadap dolar AS (kurs naik dari ± 13.700 ke ± 18.070).
- Semua aset punya **kurtosis tinggi** (5–15): sebagian besar hari pergerakannya kecil, tetapi sesekali terjadi pergerakan ekstrem (*fat tails*).
- Outlier return (lihat box plot `figures/00_boxplot_return.png`) **tidak dibuang**. Outlier ini adalah peristiwa pasar nyata (mis. 26 Maret 2020 saat COVID), bukan kesalahan data.
