# Log Penggunaan AI — Tristan

**Nama:** Tristan Satria Perdana Hermawan  
**NIM:** 103012300253

> Isi setiap kali pakai AI. Satu sesi = satu entri. Prompt ditulis apa adanya (copy-paste), jawaban AI boleh diringkas.
> Screenshot percakapan simpan di folder `Log/` juga, dengan nama `Screenshot_AI_[NIM]` (PNG per gambar atau satu PDF gabungan).

## Ringkasan (untuk tabel deklarasi)

| No | Nama Tools AI | Bagian yang Dibantu | Bentuk Bantuan / Tujuan Prompt | Tingkat Ketergantungan |
|----|---------------|---------------------|--------------------------------|------------------------|
| 1  | Antigravity (Google Deepmind) | Multiple Time Series & Calendar Heatmap (bagian 3.3–3.4) | Membaca README dan notebook, mempelajari struktur proyek, menulis kode Multiple Time Series (direct labeling, skala log) dan Calendar Heatmap (return IHSG), beserta interpretasi | Tinggi |

---

## Entri 1

- **Tanggal:** 2026-11-03
- **Tools AI:** Antigravity (Google Deepmind, VS Code)
- **Bagian yang dibantu:** Multiple Time Series (3.3) dan Seasonal Plot / Calendar Heatmap (3.4) di `notebook_timeseries.ipynb`
- **Screenshot:** `Screenshot_AI_103012300253.pdf` (TODO: ambil screenshot lalu simpan di folder `Log/`; harus terlihat nama platform, prompt, dan jawaban)

**Prompt:**
```
pelajari folder Visdat-Cihuy ini, baca juga README nya
```
```
lanjutkan pengerjaan Bagian 3.3 dan 3.4, sesuaikan dengan pengerjaan teman teman saya seperti pembuatan log_ai nya dll
```

**Ringkasan jawaban AI:**
- AI mempelajari seluruh isi repository: README, notebook (44 sel), data CSV, log AI Davu dan Raffa, serta draf laporan Bab 1–2.
- AI merangkum struktur proyek, pembagian tugas, dan status masing-masing anggota.
- AI menemukan sel `# TODO Tristan` pada bagian 3.3 dan 3.4 di notebook.
- AI menulis kode:
  - **Multiple Time Series (3.3):** membandingkan 5 aset lintas kategori (IHSG, S&P 500, Bitcoin, Emas, USD/IDR) menggunakan data `norm` (basis 100) dengan skala logaritmik. Menggunakan **direct labeling** di ujung kanan garis (tanpa legend). Label yang berdekatan (Emas & S&P 500) diberi offset vertikal agar tidak bertumpuk. Grafik disimpan ke `figures/03_multi_timeseries.png`.
  - **Calendar Heatmap (3.4):** heatmap rata-rata return harian IHSG per bulan dan tahun menggunakan `seaborn.heatmap` dengan colormap diverging `RdBu` dan `center=0`. Angka return ditampilkan di setiap sel. Grafik disimpan ke `figures/04_heatmap_return_ihsg.png`.
- AI menulis interpretasi untuk kedua grafik di sel markdown setelah masing-masing kode.
- AI membuat file log AI ini (`Log/log_ai_Tristan.md`).
- AI menjalankan kode secara terpisah untuk memastikan grafik dihasilkan tanpa error sebelum memasukkan ke notebook.

**Yang aku pakai / ubah dari jawaban AI:**
- **Kode Multiple Time Series dan Calendar Heatmap:** ditulis AI dan aku pakai. Aku mempelajari penjelasan kode dan grafik yang dihasilkan.
- **Interpretasi 3.3 dan 3.4:** ditulis AI berdasarkan data dan grafik. Angka-angka (indeks basis 100, return per bulan) diambil langsung dari data `close_clean.csv`.
- **Pilihan aset untuk grafik 3.3:** mengikuti saran dari Davu di notebook (IHSG, S&P 500, Bitcoin, Emas, USD/IDR — mewakili 5 kategori).
- **Pilihan variabel untuk heatmap:** return harian IHSG dipilih karena paling relevan dan sudah disarankan di notebook.
- **Pengecekan:** grafik sudah dihasilkan tanpa error, angka di interpretasi sesuai dengan data.

---

