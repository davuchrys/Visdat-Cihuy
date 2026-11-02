# Log Penggunaan AI — Raffa

**Nama:** Raffa Anung El Haqqi  
**NIM:** 103012300163

> Isi setiap kali pakai AI. Satu sesi = satu entri. Prompt ditulis apa adanya (copy-paste), jawaban AI boleh diringkas.
> Screenshot percakapan simpan di folder `Log/` juga, dengan nama `Screenshot_AI_[NIM]` (PNG per gambar atau satu PDF gabungan).

## Ringkasan (untuk tabel deklarasi)

| No | Nama Tools AI | Bagian yang Dibantu | Bentuk Bantuan / Tujuan Prompt | Tingkat Ketergantungan |
|----|---------------|---------------------|--------------------------------|------------------------|
| 1  | Claude (Claude Code) | Line Plot & Area Plot (bagian 3.1–3.2) | Membaca README dan notebook, menulis kode Line Plot (IHSG) dan Area Plot (volume 4 saham bank), sel cek nilai transaksi, draf interpretasi, dan penjelasan kode | Tinggi |

---

## Entri 1

- **Tanggal:** 2026-11-02
- **Tools AI:** Claude (Claude Code, VS Code)
- **Bagian yang dibantu:** Line Plot (3.1) dan Area Plot (3.2) di `notebook_timeseries.ipynb`
- **Screenshot:** `Screenshot_AI_103012300163_01.png` (TODO: ambil screenshot lalu simpan di folder `Log/`; harus terlihat nama platform, prompt, dan jawaban)

**Prompt:**
```
sekarang saya raffa baca readme yang ada dulu dan pahami
```
```
oke sekarang saya harus ngapain dan gimana bantuin dulu
```
```
ni saya baca dari line berapa
```
```
okeh sekarang bantu saya memahami dong
```
```
1. Volume itu akumulasi, jadi total sebulan = jumlah harian sum. Harga itu nilai di satu titik waktu, kalau dijumlah angkanya nggak bermakna. Makanya pakai last atau mean.

2. Error. Tanpa .T, tiap bulan dianggap satu saham, jadi ukurannya nggak cocok sama sumbu x.
```
```
coba sekarang interpretasi mu gimana setiap hasil tadi
```
```
interpretasi 3.1 gaada apa gimana 3.2 gimana
```
```
kirim sini coba
```
```
kalo dah diperbaiki yang 3.2 jadi gimana kirim sini dulu 3.1 sama 3.2 yang dah diperbaiki
```
```
boleh hitung 3.2
```
```
buatkan drafnya dan untuk interpretasinya kirim sini dulu saya mau pahami
```
```
todo sesuaikan ni emang ada yang kosong apa gimana
```
```
ni interpretasi dengan saya ubah dikit dan masukkan ke interpretasi di code, kemudian perbaiki log saya
```
(prompt terakhir disertai teks interpretasi 3.1 dan 3.2 versiku sendiri, yang sekarang ada di notebook)

**Ringkasan jawaban AI:**
- AI merangkum README: topik, 9 aset, jobdesk, variabel siap pakai (`close`, `volume`, `ret`, `norm`, `close_m`), dan aturan log AI.
- AI membaca notebook dan menemukan sel `# TODO Raffa` pada bagian 3.1 dan 3.2.
- AI menulis kode:
  - Line Plot harga penutupan IHSG 2020–2026 dengan anotasi titik terendah (24 Mar 2020), puncak (20 Jan 2026), dan data terakhir (30 Okt 2026)
  - Area Plot stacked volume bulanan BBCA, BBRI, BMRI, BBNI dengan direct labeling
  - sel kecil yang membandingkan porsi volume lembar dengan perkiraan nilai transaksi (harga × volume)
- AI menyimpan grafik ke `figures/01_line_ihsg.png` dan `figures/02_area_volume_bank.png`, dan menjalankan notebook di salinan untuk memastikan tidak error.
- AI menjelaskan kode baris per baris dan menanyakan dua pertanyaan cek pemahaman (kenapa volume dijumlah per bulan, fungsi `.T` di `stackplot`); jawabanku dikoreksi AI dan dinyatakan benar.
- AI menulis draf interpretasi 3.1 dan 3.2, termasuk catatan bahwa volume lembar bukan nilai transaksi (BBRI tebal di grafik, tetapi BBCA terbesar dalam nilai).
- AI memasukkan versi interpretasiku ke notebook dan memperbaiki log ini.

**Yang aku pakai / ubah dari jawaban AI:**
- **Kode Line Plot, Area Plot, dan sel cek nilai transaksi:** ditulis AI dan aku pakai apa adanya. Aku pelajari penjelasannya baris per baris dan menjawab pertanyaan cek pemahaman, tetapi aku tidak menulis kodenya dari nol.
- **Interpretasi 3.1 dan 3.2:** isi dan angkanya berasal dari draf AI. Aku menyingkat dan mengubah kalimatnya ke gaya bahasaku sendiri, lalu memasukkannya ke notebook. Poin-poin dan angkanya tetap sama dengan draf.
- **Yang tidak aku tambahkan:** penyebab penurunan IHSG 2026. Interpretasi hanya menjelaskan pergerakan grafik.
- **Pengecekan:** angka di interpretasi dicocokkan AI dengan data (`close_clean.csv`, `volume_clean.csv`), dan notebook sudah dijalankan ulang tanpa error.

---
