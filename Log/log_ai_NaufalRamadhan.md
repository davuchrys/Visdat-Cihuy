# Log Penggunaan AI — Naufal Ramadhan

**Nama:** Ahmad Naufal Ramadhan  
**NIM:** 103012300239

> Isi setiap kali pakai AI. Satu sesi = satu entri. Prompt ditulis apa adanya (copy-paste), jawaban AI boleh diringkas.
> Screenshot percakapan simpan di folder `Log/` juga, dengan nama `Screenshot_AI_[NIM]` (PNG per gambar atau satu PDF gabungan).

## Ringkasan (untuk tabel deklarasi)

| No | Nama Tools AI | Bagian yang Dibantu | Bentuk Bantuan / Tujuan Prompt | Tingkat Ketergantungan |
|----|---------------|---------------------|--------------------------------|------------------------|
| 1  | Antigravity (Google DeepMind) | Notebook bagian 5–7, draf awal laporan & slide | Mempelajari repositori, menyusun draf kesimpulan (8 insight, 6 kendala, 5 pengembangan), merekap tabel deklarasi AI semua anggota, melengkapi daftar pustaka, membuat draf laporan PDF awal (5 halaman), dan draf awal slide presentasi (10 slide) | Tinggi |
| 2  | Google Gemini (Gemini Web) | Parafrase & penulisan ulang narasi Laporan (Bab 1–5) | Mengubah bahasa draf laporan agar terdengar lebih natural layaknya tulisan mahasiswa/praktisi data, tidak kaku, dan meminimalkan pola khas AI untuk dokumen Word/PDF final | Sedang |
| 3  | Antigravity (Google DeepMind) | Pembaruan Slide Presentasi (PPTX & PDF) & Sinkronisasi Laporan Final | Menyelaraskan seluruh 10 slide presentasi dengan laporan final hasil editan (Bab 1–5, logo Telkom University, peran anggota, 8 insight utama format 2-kolom, kendala & rencana pengembangan) | Sedang |

---

## Entri 1

- **Tanggal:** 2026-11-05
- **Tools AI:** Antigravity (Google DeepMind) — model Gemini 3.8 Flash Medium
- **Bagian yang dibantu:** Notebook Bagian 5 (Kesimpulan), Bagian 6 (Deklarasi AI), Bagian 7 (Daftar Pustaka); draf awal Laporan PDF; draf awal slide; inisiasi rekap log AI
- **Screenshot:** `Screenshot_AI_103012300239.pdf` (hal. 5–7)

**Prompt:**
```
pelajari folder visdat-cihuy ini, baca juga README nya
```
```
kerjakan
1. Notebook Bagian 5 (Kesimpulan): Menyusun minimal 5 butir insight utama, kendala, dan rencana pengembangan (saat ini sel 46 masih berupa placeholder kosong).
2. Notebook Bagian 6 (Deklarasi AI): Menggabungkan dan melengkapi tabel deklarasi AI dari semua anggota (termasuk Naufal Rafif dan Naufal Ramadhan).
3. Notebook Bagian 7 (Daftar Pustaka): Melengkapi sitasi referensi yang digunakan.
4. Laporan Akhir (PDF): Mengompilasi Bab 1 s.d. Bab 5 menjadi laporan PDF 3–5 halaman.
5. Slide Presentasi (PDF/PPTX): Maksimal 10 slide di folder slide/.
6. Rekap Log AI: rekap log AI termasuk yang kita lakukan.
```

**Ringkasan jawaban AI:**
- AI mempelajari README, notebook (49 sel), draf laporan Bab 1–2 Davu, dan log AI semua anggota.
- **Notebook bagian 5 (Kesimpulan):** Menyusun 8 insight utama yang diambil dari interpretasi semua anggota (Line Plot, Area Plot, Multiple Time Series, Heatmap, Moving Average, Fitting, data profiling), ditambah 6 kendala dan 5 rencana pengembangan.
- **Notebook bagian 6 (Deklarasi AI):** Menyusun tabel rekap gabungan dari log semua anggota (Davu, Raffa, Tristan, Naufal Rafif, Naufal Ramadhan).
- **Notebook bagian 7 (Daftar Pustaka):** Melengkapi sitasi referensi formal (Hyndman & Athanasopoulos, pandas, NumPy, Matplotlib, seaborn, palet Okabe-Ito, materi perkuliahan).
- **Laporan PDF Awal:** Membuat file `laporan/Laporan_Midterm_Kelompok_Cihuy.pdf` (5 halaman A4, Bab 1–5 dengan 7 grafik dari `figures/`).
- **Slide Presentasi Awal:** Membuat `slide/Slide_Midterm_Kelompok_Cihuy.pptx` dan `.pdf` (10 slide, tiap slide diberi nama presenter).
- AI menjalankan ulang seluruh notebook (Restart & Run All via `nbconvert`) untuk memastikan tidak ada error.

**Yang aku pakai / ubah dari jawaban AI:**
- **Kesimpulan, deklarasi, dan daftar pustaka:** Draf dari AI aku masukkan ke sel notebook. Angka-angka di kesimpulan diambil murni dari interpretasi anggota lain di notebook.
- **Laporan dan slide awal:** Draf awal dari AI aku jadikan acuan kasar, kemudian aku tinjau ulang untuk disempurnakan narasinya agar lebih luwes dan alami.
- **Pengecekan:** Notebook lulus Restart & Run All tanpa error; laporan awal 5 halaman; slide 10 buah.

---

## Entri 2

- **Tanggal:** 2026-11-05
- **Tools AI:** Google Gemini (Gemini Web — model Flash)
- **Bagian yang dibantu:** Parafrase dan penulisan ulang narasi Laporan (Bab 1 s.d. Bab 5)
- **Screenshot:** `Screenshot_AI_103012300239.pdf` (hal. 1–4)

**Prompt:**
*(Melampirkan dokumen draf PDF laporan)*
```
ubah laporan tersebut agar terlihat natural
```

**Ringkasan jawaban AI:**
- AI menulis ulang narasi draf laporan agar terdengar lebih natural, mengalir, analitis layaknya tulisan mahasiswa/praktisi data beneran, tidak kaku, dan meminimalkan pola khas AI:
  1. **Menghilangkan gaya listicle kaku:** Mengubah analisis visualisasi dan tren menjadi paragraf analitis yang saling terhubung logikanya secara kohesif.
  2. **Kosakata sains data & finansial yang otentik:** Memperkaya narasi teknis dengan istilah yang tepat (*long/wide format, DatetimeIndex, forward fill, direct labeling, fat tails, kurtosis tinggi, Runge's phenomenon / overfitting, maximum drawdown, lagging indicator, sideways consolidation*).
  3. **Sintaksis & gaya bahasa:** Menghilangkan repetisi kalimat pasif monoton dan menambahkan variasi transisi antargagasan yang dinamis.
- Menyusun teks revisi lengkap mencakup:
  - Judul: *"Laporan Analisis Time Series: Pasar Saham & Portofolio Finansial (2020–2026)"*
  - Bab 1: Latar Belakang (guncangan pasar 2020–2026, 4 komponen time series), Tujuan dan Batasan.
  - Bab 2: Dataset & Preprocessing (yfinance 9 aset dari 5 kategori, pipeline pembersihan, tabel profil return harian).
  - Bab 3: Eksplorasi Visualisasi (narasi analitis komparatif untuk Line Plot, Stacked Area Plot, Multiple Time Series, dan Calendar Heatmap).
  - Bab 4: Analisis Tren (evaluasi Moving Average MA 20 & 200 hari beserta trade-off lag vs kehalusan, serta pencocokan tren polyfit linear, polinomial derajat 3, dan eksponensial).
  - Bab 5: Kesimpulan & Refleksi Proyek (temuan utama, kendala pengolahan, dan arah pengembangan selanjutnya).

**Yang aku pakai / ubah dari jawaban AI:**
- Naskah narasi revisi dari Gemini ini aku salin dan rapikan ke dalam dokumen Microsoft Word (`Laporan_Midterm_Kelompok_Cihuy.docx`).
- Aku menyusun layout resmi laporan: menambahkan cover halaman depan dengan logo Telkom University, memasukkan tabel anggota dan pembagian peran, menyisipkan semua 7 gambar grafik dari folder `figures/`, menata tabel statistik dan dataset, melengkapi sitasi daftar pustaka, lalu mengekspornya menjadi `Laporan_Midterm_Kelompok_Cihuy.pdf` (dokumen final 11 halaman).

---

## Entri 3

- **Tanggal:** 2026-11-05
- **Tools AI:** Antigravity (Google DeepMind) — model Gemini 3.8 Flash (High)
- **Bagian yang dibantu:** Pembaruan Slide Presentasi (`slide/Slide_Midterm_Kelompok_Cihuy.pptx` & `.pdf`) menyesuaikan Laporan Final 11 Halaman, serta Sinkronisasi Dokumen Proyek
- **Screenshot:** `Screenshot_AI_103012300239.pdf` (hal. 5–7 dan riwayat sesi terminal/IDE)

**Prompt:**
*(Melampirkan dokumen PDF laporan final 11 halaman)*
```
perbarui lagi slide presentasinya menyesuaikan dengan laporan yang telah saya buat
```
```
tambahkan percakapan kita sekarang ini dan percakapan yang ada di dalam @[c:\Users\s-riz\Downloads\ss.pdf] file screenshot ke dalam log_ai NaufalRamadhan.md
```

**Ringkasan jawaban AI:**
- AI membaca dokumen laporan final (`Laporan_Midterm_Kelompok_Cihuy.pdf` dan `.docx`), mengekstrak logo Telkom University, tabel anggota & peran, narasi Bab 1–4, 8 insight utama Bab 5.1, 5 kendala Bab 5.2, 5 rencana pengembangan Bab 5.3, serta daftar pustaka.
- AI memperbarui script pembangun slide `slide/build_slide.py`:
  1. **Cover Slide (Slide 1):** Menggunakan judul resmi *"Laporan Analisis Time Series: Pasar Saham & Portofolio Finansial (2020–2026)"*, menyematkan badge logo Telkom University, identitas mata kuliah, dan daftar 5 anggota lengkap dengan NIM serta perannya (Davu: Koordinator & Data, Raffa: Line & Area, Tristan: Multi Series & Heatmap, Naufal Rafif: MA & Fitting, Naufal Ramadhan: Kesimpulan & Slide).
  2. **Slide Bab 1 & 2 (Slide 2):** Format 2 kolom memuat 4 komponen time series, 4 tujuan analisis, ruang lingkup, detail 9 aset dari 5 kategori, tahapan data cleaning, dan profiling fat tails.
  3. **Slide Visualisasi (Slide 3–8):** Menampilkan nama presenter dan peran di navbar atas, menyelaraskan judul bab, mengatur proporsi gambar vs teks secara dinamis, dan memberikan gaya penekanan tebal (*bold lead*) berwarna navy pada butir analisis temuan.
  4. **Slide Kesimpulan (Slide 9):** Menata seluruh **8 insight utama** dari Bab 5.1 ke dalam tata letak 2 kolom (4 insight kiri, 4 insight kanan) agar tidak terjadi penumpukan teks dan nyaman dipresentasikan.
  5. **Slide Kendala & Pengembangan (Slide 10):** Format 3 kolom rapi yang merangkum kendala analisis (Bab 5.2), rencana pengembangan (Bab 5.3), dan deklarasi AI beserta sitasi referensi (Bab 6–7).
- AI mengompilasi ulang dan memverifikasi kualitas rendering visual seluruh 10 slide ke dalam format PPTX (`slide/Slide_Midterm_Kelompok_Cihuy.pptx`) dan PDF (`slide/Slide_Midterm_Kelompok_Cihuy.pdf`).
- AI menyalin file screenshot `ss.pdf` dari Downloads ke `Log/Screenshot_AI_103012300239.pdf` dan menyusun riwayat percakapan lengkap 3 entri ke dalam file log ini.

**Yang aku pakai / ubah dari jawaban AI:**
- Seluruh 10 slide presentasi PPTX dan PDF hasil pembaruan langsung aku gunakan untuk bahan presentasi kelompok.
- Format pembagian peran dan rekap transparansi AI aku pastikan sesuai dengan fakta pengerjaan tugas.

---
