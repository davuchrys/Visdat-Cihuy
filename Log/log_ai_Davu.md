# Log Penggunaan AI — Davu

**Nama:** Adhyatma Chrysostomos Davu  
**NIM:** 103012340479

> Isi setiap kali pakai AI. Satu sesi = satu entri. Prompt ditulis apa adanya (copy-paste), jawaban AI boleh diringkas.
> Screenshot percakapan simpan di folder `Log/` juga, dengan nama `Screenshot_AI_[NIM]` (PNG per gambar atau satu PDF gabungan).

## Ringkasan (untuk tabel deklarasi)

| No | Nama Tools AI | Bagian yang Dibantu | Bentuk Bantuan / Tujuan Prompt | Tingkat Ketergantungan |
|----|---------------|---------------------|--------------------------------|------------------------|
| 1  | Claude (Claude Code) | Perencanaan proyek | Membaca soal, membagi jobdesk, membuat struktur folder & README | Sedang |
| 2  | Claude (Claude Code) | Dataset & kerangka notebook | Script unduh data Yahoo Finance, cleaning, data profiling, kerangka notebook, draf laporan Bab 1–2 | Tinggi |

---

## Entri 1

- **Tanggal:** 2026-11-02
- **Tools AI:** Claude (Claude Code, VS Code)
- **Bagian yang dibantu:** Perencanaan & pembagian tugas
- **Screenshot:** `Screenshot_AI_103012340479.pdf` (hal. 1–3)

**Prompt:**
```
kamu baca dulu kita disuruh apa di pdf itu. kelompokku ada 5 orang dan tolong bagi2 jobdesknya.
anggotanya Davu (aku), Raffa, Tristan, Naufal rafif, Naufal ramadhan. Davu akan memulai. terus nanti
bikinin folder Log yang nantinya akan diisi chat masing2 orang dengan AI ya. tulis di readme juga nanti
agar tidak bingung seperti jpbdesk, folder log, dll yang perlu ditulis
```

**Ringkasan jawaban AI:** AI merangkum isi soal Midterm Project, membagi jobdesk untuk 5 anggota,
membuat folder `Log/` per anggota beserta template log, dan menulis `README.md`.

**Yang aku pakai / ubah dari jawaban AI:**
Pembagian jobdesk dan README dari AI aku pakai. Aku minta AI hapus folder Log per anggota karena tidak perlu, cukup satu folder `Log/` dan tiap anggota menamai file sendiri. Template log juga aku minta dihapus, biar tiap anggota bikin format log sendiri.


---

## Entri 2

- **Tanggal:** 2026-11-02
- **Tools AI:** Claude (Claude Code, VS Code)
- **Bagian yang dibantu:** Dataset, cleaning, kerangka notebook, draf laporan Bab 1–2
- **Screenshot:** `Screenshot_AI_103012340479.pdf` (hal. 4–9)

**Prompt:**
```
baca dulu materi2 ini ya
(lampiran: PDF materi Minggu 01, 02, 03, 04, 06)
```
```
Kelompok cihuy
topik : Pasar Saham & Keuangan
sumber dataset : https://finance.yahoo.com

Pakai semua dataset yang ada dari situ
```
```
lakukan jobdeskku sekarang
```
```
nim ku 103012340479
```
```
anggota :
1. Adhyatma Chrysostomos Davu 103012340479
2. Raffa Anung El Haqqi 103012300163
3. Naufal Rafif Hidayat 103012300403
4. Ahmad Naufal Ramadhan 103012300239
5. Tristan Satria Perdana Hermawan 103012300253
```

**Ringkasan jawaban AI:**
- AI merangkum materi kuliah Minggu 1–6 yang relevan untuk tiap jobdesk.
- AI memilih 9 aset dari 5 kategori Yahoo Finance (IHSG, S&P 500, BBCA, BBRI, BMRI, BBNI, Bitcoin, Emas, USD/IDR), periode 2020–2026.
- AI membuat `data/download_data.py` untuk mengunduh data dengan `yfinance`, lalu menyimpan CSV mentah dan bersih.
- AI membuat `notebook_timeseries.ipynb`:
  - bagian Pendahuluan dan Dataset: load, missing values, cleaning (hari kerja + forward fill libur bursa), variabel turunan, statistik deskriptif, box plot outlier return
  - sel kosong untuk bagian anggota lain, plus template deklarasi AI dan daftar pustaka
- AI menulis draf laporan Bab 1–2 (`laporan/Bab1_2_Davu.md`) dan meng-update README.

**Yang aku pakai / ubah dari jawaban AI:**
Topik (Pasar Saham & Keuangan) dan sumber data (Yahoo Finance) aku yang tentukan. Pilihan 9 aset, script unduh data, cleaning, dan kerangka notebook dari AI aku pakai. Aku cek notebook bisa Run All tanpa error. Screenshot percakapan aku minta digabung jadi satu PDF.

