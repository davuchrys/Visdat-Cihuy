# Log Penggunaan AI — Naufal Rafif

**Nama:** Naufal Rafif Hidayat  
**NIM:** 103012300403

> Isi setiap kali pakai AI. Satu sesi = satu entri. Prompt ditulis apa adanya (copy-paste), jawaban AI boleh diringkas.
> Screenshot percakapan simpan di folder `Log/` juga, dengan nama `Screenshot_AI_[NIM]` (PNG per gambar atau satu PDF gabungan).

## Ringkasan (untuk tabel deklarasi)

| No | Nama Tools AI | Bagian yang Dibantu | Bentuk Bantuan / Tujuan Prompt | Tingkat Ketergantungan |
|----|---------------|---------------------|--------------------------------|------------------------|
| 1  | Claude (Claude Code) | Analisis Tren (bagian 4) | Clone repo & membaca README, menulis kode Moving Average (20 & 200 hari) dan fitting model (`numpy.polyfit` linear, polinomial derajat 3, eksponensial Emas & Bitcoin), tabel trade-off window, draf interpretasi | Tinggi |

---

## Entri 1

- **Tanggal:** 2026-11-04
- **Tools AI:** Claude (Claude Code, aplikasi desktop)
- **Bagian yang dibantu:** Moving Average (4.1) dan Fitting Model (4.2) di `notebook_timeseries.ipynb`
- **Screenshot:** `Screenshot_AI_103012300403.pdf`

**Prompt:**
```
clone github ini https://github.com/davuchrys/Visdat-Cihuy.git kemudian kerjakan sesuai readme nya
```
(AI bertanya aku anggota yang mana, aku pilih: **Naufal Rafif**)

**Ringkasan jawaban AI:**
- AI meng-clone repository, membaca README dan seluruh notebook, lalu menemukan sel `# TODO Naufal Rafif` di bagian 4.1 dan 4.2.
- AI menginstal library sesuai README (`pandas numpy matplotlib seaborn jupyter`) di Python 3.11.
- AI menulis kode:
  - **Moving Average (4.1):** MA 20 hari dan MA 200 hari di atas harga asli IHSG (`rolling(window).mean()`), dengan direct labeling di ujung garis. Panel atas seluruh periode + daerah abu-abu untuk 199 hari NaN MA 200; panel bawah zoom Jun 2025 – Okt 2026 yang menandai puncak harga, puncak MA 20, dan puncak MA 200. Disimpan ke `figures/05_moving_average_ihsg.png`.
  - **Tabel trade-off window:** jumlah NaN di awal, tanggal mulai ada nilai, std perubahan harian (kehalusan), dan keterlambatan puncak (hari bursa), plus hitungan persilangan MA 20 & MA 200 (*golden/death cross*).
  - **Fitting IHSG (4.2):** `np.polyfit` linear (derajat 1) dan polinomial (derajat 3), sumbu x = hari bursa ke-n, dengan R². Disimpan ke `figures/06_fitting_ihsg.png`.
  - **Tabel perbandingan derajat 1–6** (R², RMSE, nilai fit hari terakhir) untuk alasan memilih derajat 3.
  - **Fitting eksponensial Emas & Bitcoin:** `np.polyfit` pada `log(harga)`, pertumbuhan per tahun = e^(b·260) − 1, grafik skala log. Disimpan ke `figures/07_fitting_eksponensial.png`.
- AI menulis interpretasi Moving Average (trade-off NaN vs kehalusan vs keterlambatan, death cross 11 Mar 2026) dan interpretasi fitting (R² rendah untuk IHSG, Emas +16,5%/tahun, Bitcoin +35%/tahun tapi fit buruk, batasan ekstrapolasi).
- AI menjalankan **Restart & Run All** seluruh notebook: tidak ada error, dan sel anggota lain tidak berubah. AI juga memperbaiki tampilan grafik (label puncak yang bertumpuk, label sumbu log) dan mencocokkan semua angka di interpretasi dengan output notebook.
- AI membuat file log ini dan mencentang status di README.

**Yang aku pakai / ubah dari jawaban AI:**
- **Kode Moving Average, tabel trade-off, fitting linear/polinomial, dan fitting eksponensial:** ditulis AI.
- **Pilihan parameter:** window 20 & 200 hari mengikuti saran Davu di notebook. Derajat polinomial 3 dan aset Emas & Bitcoin untuk fit eksponensial dipilih AI, dengan alasan di tabel perbandingan derajat dan di interpretasi.
- **Interpretasi 4.1 dan 4.2:** draf dari AI. Angka-angkanya diambil dari output notebook.
- **Pengecekan:** notebook sudah dijalankan ulang (Restart & Run All) tanpa error.


---
