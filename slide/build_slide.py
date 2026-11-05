"""Membuat slide presentasi (maks. 10 slide) dalam format PPTX dan PDF.
Menyesuaikan dengan isi dan struktur Laporan Midterm Kelompok Cihuy (Bab 1 s.d. Bab 5,
Deklarasi AI, dan Daftar Pustaka).

Jalankan dari root repo:  python slide/build_slide.py
Hasil: slide/Slide_Midterm_Kelompok_Cihuy.pptx dan .pdf
Butuh: pip install python-pptx reportlab pillow pymupdf
"""
import re
from pathlib import Path

from PIL import Image as PILImage

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
OUT = ROOT / "slide"

NAVY = (0x1F, 0x3A, 0x5F)
NAVY_DARK = (0x13, 0x25, 0x3D)
ACCENT = (0xE6, 0x9F, 0x00)     # oranye Okabe-Ito
ACCENT_LIGHT = (0xF7, 0xD4, 0x88)
GREY = (0x33, 0x33, 0x33)
GREY_MUTED = (0x66, 0x66, 0x66)
LIGHT_BLUE = (0xCF, 0xDB, 0xE8)
CARD_BG = (0xF4, 0xF6, 0xF9)
WHITE = (255, 255, 255)

W_IN, H_IN = 13.333, 7.5

# ------------------------------------------------------------------ Data Anggota
ANGGOTA = [
    ("Adhyatma Chrysostomos Davu", "103012340479", "Koordinator, data & kerangka notebook"),
    ("Raffa Anung El Haqqi", "103012300163", "Line Plot & Area Plot"),
    ("Tristan Satria Perdana Hermawan", "103012300253", "Multiple Time Series & Calendar Heatmap"),
    ("Naufal Rafif Hidayat", "103012300403", "Analisis Tren (Moving Average & Fitting)"),
    ("Ahmad Naufal Ramadhan", "103012300239", "Kesimpulan, Deklarasi AI, laporan, slide"),
]

# ------------------------------------------------------------------ Konten Slide (Maks 10 Slide)
SLIDES = [
    # Slide 1: Cover
    dict(
        kind="cover",
        title="Laporan Analisis Time Series: Pasar Saham & Portofolio Finansial (2020–2026)",
    ),

    # Slide 2: Bab 1 & Bab 2 (Davu)
    dict(
        title="Pendahuluan & Karakteristik Dataset",
        presenter="Adhyatma Chrysostomos Davu",
        role="Koordinator, data & kerangka notebook",
        columns=[
            ("Latar Belakang & Tujuan (Bab 1)", [
                "<b>Dinamika Pasar 2020–2026:</b> Pasar finansial mengalami rentetan guncangan: crash pandemi COVID-19, siklus kenaikan suku bunga global 2022, reli masif Bitcoin & emas, serta koreksi tajam IHSG 2026.",
                "<b>4 Komponen Time Series:</b> Visualisasi ditujukan membedah tren jangka panjang, pola musiman/periodik, siklus naik-turun pasar, dan noise fluktuasi acak harian pada aset riil.",
                "<b>4 Tujuan Analisis:</b> Memetakan pola utama IHSG, komparasi kinerja 5 kelas aset (basis 100 & log), identifikasi kalender musiman return, serta evaluasi tren teknikal (MA & fitting).",
                "<b>Ruang Lingkup:</b> Data harian (hari kerja) 2 Jan 2020 – 30 Okt 2026 (1.778 hari bursa); analisis deskriptif-visual murni (bukan prediksi/rekomendasi investasi).",
            ]),
            ("Sumber Data & Data Cleaning (Bab 2)", [
                "<b>Yahoo Finance (yfinance):</b> 9 aset dari 5 kategori (Indeks: IHSG, S&P 500 · Saham: BBCA, BBRI, BMRI, BBNI · Kripto: Bitcoin · Komoditas: Emas · Kurs: USD/IDR).",
                "<b>Data Cleaning:</b> Format long (15.936 baris) dikonversi ke wide (1.778 hari kerja × 9 aset); kalender diselaraskan ke hari kerja (weekend kripto dibuang).",
                "<b>Penanganan Libur & Kualitas:</b> Forward fill harga penutupan terakhir (maks. 5 hari); volume libur diisi 0; data terurut, 0 duplikat, dan missing value = 0.",
                "<b>Data Profiling:</b> Seluruh aset memiliki fat tails (kurtosis 5–15; outlier nyata tidak dibuang); Bitcoin paling volatil (std 3,70%/hari) & return tertinggi (+1.005,1% / ±11×).",
            ]),
        ],
    ),

    # Slide 3: Bab 3.1 Line Plot (Raffa)
    dict(
        title="Line Plot — Dinamika Harga Penutupan IHSG",
        presenter="Raffa Anung El Haqqi",
        role="Line Plot & Area Plot",
        image="01_line_ihsg.png",
        bullets=[
            "<b>Crash Pandemi COVID-19:</b> Titik nadir tercatat di 3.938 poin pada 24 Maret 2020 akibat kepanikan pasar global (koreksi tajam sekitar 37%).",
            "<b>Konsolidasi Sideways:</b> Memasuki awal 2021 indeks pulih ke level pra-pandemi dan bergerak mendatar di rentang 6.500–7.500 sepanjang 2022–2024.",
            "<b>Reli All-Time High:</b> Terakselerasi sejak April 2025 hingga mencetak rekor tertinggi sepanjang sejarah di level 9.135 poin pada 20 Januari 2026.",
            "<b>Koreksi Ekstrem 2026:</b> Langsung berbalik arah dan anjlok sekitar 45% hingga tertekan ke posisi 5.057 poin per 30 Oktober 2026.",
            "<b>Temuan Kunci:</b> Pelemahan tajam pada 2026 melampaui kejatuhan saat krisis COVID-19, baik dari sisi persentase maupun kedalaman poin.",
        ],
    ),

    # Slide 4: Bab 3.2 Area Plot (Raffa)
    dict(
        title="Area Plot — Volume Transaksi Saham Bank",
        presenter="Raffa Anung El Haqqi",
        role="Line Plot & Area Plot",
        image="02_area_volume_bank.png",
        bullets=[
            "<b>Dominasi Lembar vs Rupiah:</b> BBRI konsisten mendominasi kuantitas lembar saham (rata-rata ±4 miliar lembar/bulan), namun BBCA memimpin nilai rupiah karena harga per lembar ~2× lebih mahal.",
            "<b>Dinamika Siklus Transaksi:</b> Tren aktivitas ramai di pertengahan 2020, lalu menurun dan relatif sepi sepanjang 2021–2023 (titik terendah April 2023).",
            "<b>Panic Selling Juni 2026:</b> Akumulasi volume meledak rekor 24 miliar lembar saham saat gelombang aksi jual besar-besaran ketika indeks anjlok.",
            "<b>Keterbatasan Stacked Area:</b> Layer atas (BBNI & BMRI) sulit dinilai dinamika trennya secara independen karena baseline sangat dipengaruhi fluktuasi layer di bawahnya.",
        ],
    ),

    # Slide 5: Bab 3.3 Multiple Time Series (Tristan)
    dict(
        title="Multiple Time Series — Kinerja Lintas Kelas Aset",
        presenter="Tristan Satria Perdana Hermawan",
        role="Multiple Time Series & Calendar Heatmap",
        image="03_multi_timeseries.png",
        bullets=[
            "<b>Normalisasi Basis 100 & Log:</b> Memungkinkan komparasi objektif laju pertumbuhan proporsional antaraset yang berbeda satuan harga.",
            "<b>Bitcoin (1.105 / ±11× lipat):</b> Apresiasi paling masif (+1.005,1%), kendati sempat tertekan siklus bear market tajam pada 2022.",
            "<b>Emas (256, +156%) & S&P 500 (231, +133%):</b> Tren kenaikan stabil dan konsisten tanpa guncangan ekstrem (safe haven & korporasi AS).",
            "<b>Depresiasi Rupiah (USD/IDR 132):</b> Pelemahan rupiah ±32% (13.700 → 18.070/USD) memperbesar kerugian riil investor domestik dalam denominasi dolar.",
            "<b>IHSG (80, −19,5%):</b> Menjadi satu-satunya instrumen yang terdepresiasi di bawah modal awal.",
            "<b>Direct Labeling:</b> Label langsung di ujung kurva memangkas beban kognitif membaca kode warna legenda konvensional.",
        ],
    ),

    # Slide 6: Bab 3.4 Calendar Heatmap (Tristan)
    dict(
        title="Calendar Heatmap — Pola Musiman Return IHSG",
        presenter="Tristan Satria Perdana Hermawan",
        role="Multiple Time Series & Calendar Heatmap",
        image="04_heatmap_return_ihsg.png",
        bullets=[
            "<b>Skala Diverging (Titik Tengah 0%):</b> Memetakan rata-rata return harian IHSG per bulan dan tahun untuk mendeteksi kecenderungan return musiman.",
            "<b>Kecenderungan Koreksi Maret:</b> Negatif di 5 dari 7 tahun pengamatan, dengan penurunan tertajam Maret 2020 (-0,75%) dan Maret 2026 (-0,69%).",
            "<b>Zona Hijau Juli–Agustus:</b> Relatif konsisten berada di zona positif sebagai fase penguatan pasar pertengahan tahun.",
            "<b>Kontras Siklus Tahunan:</b> Tahun 2025 didominasi warna biru (fase reli solid), sedangkan 2026 didominasi warna merah akibat gelombang koreksi luas.",
            "<b>Calendar Effect Rapuh:</b> Tidak ada bulan yang 100% selalu naik atau turun; pola musiman di BEI mudah patah oleh sentimen makro.",
        ],
    ),

    # Slide 7: Bab 4.1 Moving Average (Naufal Rafif)
    dict(
        title="Moving Average — Evaluasi Tren IHSG (MA 20 & 200)",
        presenter="Naufal Rafif Hidayat",
        role="Analisis Tren (Moving Average & Fitting)",
        image="05_moving_average_ihsg.png",
        bullets=[
            "<b>Trade-off Lag Awal:</b> MA 20 butuh 19 hari bursa (aktif 29 Jan 2020); MA 200 butuh 199 hari (aktif 7 Okt 2020) sehingga crash COVID luput dari garis MA 200.",
            "<b>Kehalusan Sinyal:</b> Volatilitas harian diredam drastis: simpangan baku harian terpangkas dari ±73 poin (aktual) → ±18 poin (MA 20) → ±5 poin (MA 200).",
            "<b>Keterlambatan Deteksi Tren:</b> IHSG memuncak 20 Jan 2026; MA 20 berbalik 5 hari kemudian (27 Jan), sedangkan MA 200 terlambat ±3 bulan (23 Apr 2026).",
            "<b>Death Cross 11 Maret 2026:</b> Mengonfirmasi tren penurunan hingga akhir data (posisi harga 5.057 < MA 20 5.597 < MA 200 6.690).",
            "<b>Konfirmasi Sideways:</b> 16 dari total 18 persilangan terjadi pada 2021–2025, mencerminkan fase konsolidasi pasar yang bergerak mendatar.",
        ],
    ),

    # Slide 8: Bab 4.2 Fitting Model (Naufal Rafif)
    dict(
        title="Fitting Model — Regresi Polinomial & Eksponensial",
        presenter="Naufal Rafif Hidayat",
        role="Analisis Tren (Moving Average & Fitting)",
        images=["06_fitting_ihsg.png", "07_fitting_eksponensial.png"],
        bullets=[
            "<b>Model Linear IHSG:</b> Kemiringan positif +1,11 poin/hari (±288 poin/tahun); namun R² sangat rendah (0,42) dan proyeksi akhir (±7.674) meleset jauh dari harga riil (5.057).",
            "<b>Polinomial Derajat 3 IHSG:</b> R² naik ke 0,62 karena fleksibel menangkap lengkungan siklus (turun-naik-datar-melemah); derajat 5–6 (R² 0,76) diabaikan akibat overfitting.",
            "<b>Eksponensial Emas vs Kripto:</b> Emas tumbuh teratur ±16,5%/tahun dengan kecocokan tren tertinggi (R² log = 0,78); Bitcoin tumbuh pesat ±35,3%/tahun tetapi R² lebih moderat (0,62) akibat deviasi siklus ekstrem.",
            "<b>Peringatan Metodologis:</b> Fitting matematis hanya meringkas historis masa lampau, tidak dapat dipercaya untuk ekstrapolasi/peramalan masa depan.",
        ],
    ),

    # Slide 9: Bab 5.1 Kesimpulan — 8 Insight Utama (Ahmad Naufal Ramadhan)
    dict(
        title="Kesimpulan — 8 Insight Utama Pasar & Portofolio",
        presenter="Ahmad Naufal Ramadhan",
        role="Kesimpulan, Deklarasi AI, laporan, slide",
        insights_2col=[
            # Kolom Kiri: Insight 1 - 4
            [
                ("1. IHSG Satu-Satunya Aset Merugi (−19,5%)",
                 "Terkoreksi dari basis 100 ke 80. Dua guncangan besar: crash COVID-19 (−37% ke 3.938) dan koreksi tajam 2026 (−45% dari 9.135 ke 5.057) yang melampaui kejatuhan saat COVID."),
                ("2. Aset Global Mengungguli (Trade-off Risiko)",
                 "Bitcoin naik ±11× lipat (+1.005%, std 3,70%/hari, terburuk −37%); Emas (+156%) dan S&P 500 (+133%) naik stabil tanpa guncangan ekstrem."),
                ("3. Pelemahan Rupiah ±32% vs Dolar AS",
                 "Kurs terdepresiasi dari 13.700 ke 18.070 (std 0,71%/hari). Menekan nilai riil: kerugian pemegang IHSG semakin membesar dalam denominasi dolar."),
                ("4. Volume Saham Bank Melonjak Saat Panik",
                 "BBRI memimpin jumlah lembar (±4 Miliar/bln), BBCA memimpin perputaran rupiah. Volume meledak rekor 24 miliar lembar (Juni 2026) saat indeks anjlok."),
            ],
            # Kolom Kanan: Insight 5 - 8
            [
                ("5. Pola Musiman IHSG Ada, Namun Rapuh",
                 "Maret cenderung koreksi (merah di 5 dari 7 tahun), Juli–Agustus cenderung positif. Pola musiman mudah patah oleh guncangan sentimen makro."),
                ("6. MA Menegaskan Tren Bearish 2026",
                 "Death cross MA 20 & 200 (11 Mar 2026) mengunci tren penurunan (harga < MA 20 < MA 200). 16 dari 18 persilangan 2021–2025 menandai pasar sideways."),
                ("7. Karakteristik Tren Lintas Aset Berbeda",
                 "IHSG tanpa tren tunggal (R² 0,42), Emas konsisten eksponensial (+16,5%/thn, R² 0,78), Bitcoin tumbuh pesat (+35,3%/thn, R² 0,62) dalam siklus boom-bust."),
                ("8. Distribusi Return Ber-Fat Tails",
                 "Seluruh aset memiliki kurtosis tinggi (5–15). Outlier ekstrem dipertahankan karena merupakan peristiwa pasar nyata (mis. 26 Mar 2020), bukan galat data."),
            ],
        ],
    ),

    # Slide 10: Bab 5.2, 5.3 & Deklarasi AI (Ahmad Naufal Ramadhan)
    dict(
        title="Kendala, Rencana Pengembangan & Deklarasi AI",
        presenter="Ahmad Naufal Ramadhan",
        role="Kesimpulan, Deklarasi AI, laporan, slide",
        columns=[
            ("Kendala Analisis (Bab 5.2)", [
                "<b>Kalender Bursa Berbeda:</b> Kripto 7 hari vs BEI/AS libur berbeda; diselaraskan ke hari kerja & forward fill libur (maks. 5 hari); weekend kripto terpotong.",
                "<b>Disparitas Skala & Satuan:</b> Satuan poin, IDR, dan USD sangat berbeda; diatasi dengan normalisasi basis 100 dan skala logaritmik.",
                "<b>Keterbatasan Data Volume:</b> Kurs tanpa volume; volume lembar saham bias bila dibandingkan antarsaham tanpa perkalian harga nominal.",
                "<b>Trade-off MA & Overfitting:</b> MA 200 kosong 199 hari awal sehingga crash COVID luput; regresi polinomial derajat tinggi rawan overfitting.",
                "<b>Ketergantungan API:</b> yfinance adalah API tidak resmi; data di-cache ke CSV lokal agar hasil analisis sepenuhnya reproducible.",
            ]),
            ("Rencana Pengembangan (Bab 5.3)", [
                "<b>Dekomposisi Time Series:</b> Menerapkan STL / seasonal_decompose formal untuk memisahkan tren, musiman, dan residual.",
                "<b>Korelasi Bergulir:</b> Rolling correlation antaraset (IHSG vs USD/IDR, IHSG vs S&P 500) dan konversi nilai riil IHSG ke dolar AS.",
                "<b>Volatilitas & Drawdown:</b> Rolling standard deviation dan visualisasi kedalaman penurunan (drawdown) dari rekor puncak pasar.",
                "<b>Dashboard Interaktif:</b> Membangun aplikasi interaktif (Plotly / Streamlit) agar pengguna bebas memilih aset dan rentang periode.",
                "<b>Model Peramalan:</b> Evaluasi model ARIMA / Prophet out-of-sample dengan penambahan variabel makroekonomi (suku bunga BI, inflasi).",
            ]),
            ("Deklarasi AI & Pustaka (Bab 6–7)", [
                "<b>Penggunaan AI Transparan:</b> Kolaborasi Claude Code, Antigravity (Google DeepMind), & Google Gemini (revisi narasi) terverifikasi mandiri oleh tim.",
                "<b>Integritas Akademik:</b> Seluruh kode dan interpretasi diverifikasi, dipahami, dan dapat dipertanggungjawabkan mandiri oleh tim.",
                "<b>Dokumentasi & Bukti:</b> Log per anggota di folder <code>Log/</code> dan bukti di <code>Deklarasi_AI_Kelompok_Cihuy.pdf</code>.",
                "<b>Sumber Data & Pustaka:</b> Yahoo Finance; Wilke (2019), Hyndman (2021), Okabe & Ito (CUD 2008), Materi Perkuliahan CAK4XBB3.",
            ]),
        ],
    ),
]

assert len(SLIDES) <= 10, f"Jumlah slide ({len(SLIDES)}) melebihi batas maksimal 10!"


def img_ratio(name):
    w, h = PILImage.open(FIG / name).size
    return h / w


def fit_box(name, max_w, max_h):
    r = img_ratio(name)
    w = max_w
    h = w * r
    if h > max_h:
        h = max_h
        w = h / r
    return w, h


# ======================================================================
# PPTX BUILDER
# ======================================================================
def build_pptx():
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import PP_ALIGN
    from pptx.util import Inches, Pt

    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(W_IN), Inches(H_IN)
    blank = prs.slide_layouts[6]

    def rect(sl, x, y, w, h, rgb):
        s = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        s.fill.solid()
        s.fill.fore_color.rgb = RGBColor(*rgb)
        s.line.fill.background()
        return s

    def add_para_with_runs(tf, text_content, default_size=13, default_color=GREY, space_after=6):
        para = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        para.space_after = Pt(space_after)
        para.font.name = "Calibri"
        parts = re.split(r"(<b>.*?</b>|<code>.*?</code>)", text_content)
        for pt in parts:
            if not pt:
                continue
            run = para.add_run()
            run.font.name = "Calibri"
            run.font.size = Pt(default_size)
            if pt.startswith("<b>") and pt.endswith("</b>"):
                run.text = pt[3:-4]
                run.font.bold = True
                run.font.color.rgb = RGBColor(*NAVY)
            elif pt.startswith("<code>") and pt.endswith("</code>"):
                run.text = pt[6:-7]
                run.font.bold = True
                run.font.color.rgb = RGBColor(*GREY)
            else:
                run.text = pt
                run.font.bold = False
                run.font.color.rgb = RGBColor(*default_color)

    def header(sl, title, presenter, role, n):
        # Navbar navy + garis aksen
        rect(sl, 0, 0, W_IN, 0.95, NAVY)
        rect(sl, 0, 0.95, W_IN, 0.05, ACCENT)

        # Judul slide
        tb = sl.shapes.add_textbox(Inches(0.5), Inches(0.12), Inches(8.5), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)

        # Presenter & Peran di pojok kanan atas
        tb_p = sl.shapes.add_textbox(Inches(8.5), Inches(0.08), Inches(4.35), Inches(0.8))
        tf_p = tb_p.text_frame
        tf_p.word_wrap = True
        p1 = tf_p.paragraphs[0]
        p1.alignment = PP_ALIGN.RIGHT
        r1 = p1.add_run()
        r1.text = "Presenter: "
        r1.font.size = Pt(10)
        r1.font.color.rgb = RGBColor(*LIGHT_BLUE)
        r2 = p1.add_run()
        r2.text = presenter
        r2.font.size = Pt(12)
        r2.font.bold = True
        r2.font.color.rgb = RGBColor(255, 255, 255)

        p2 = tf_p.add_paragraph()
        p2.alignment = PP_ALIGN.RIGHT
        r3 = p2.add_run()
        r3.text = role
        r3.font.size = Pt(9.5)
        r3.font.color.rgb = RGBColor(*ACCENT_LIGHT)

        # Footer
        rect(sl, 0.5, 7.0, W_IN - 1.0, 0.02, (0xDD, 0xDD, 0xDD))
        tb_f = sl.shapes.add_textbox(Inches(0.5), Inches(7.05), Inches(10.0), Inches(0.35))
        tf_f = tb_f.text_frame
        pf = tf_f.paragraphs[0]
        pf.text = "Midterm Project Visualisasi Data (CAK4XBB3) · Kelompok Cihuy · Telkom University"
        pf.font.name = "Calibri"
        pf.font.size = Pt(9.5)
        pf.font.color.rgb = RGBColor(*GREY_MUTED)

        tb_num = sl.shapes.add_textbox(Inches(11.5), Inches(7.05), Inches(1.35), Inches(0.35))
        tf_num = tb_num.text_frame
        pnum = tf_num.paragraphs[0]
        pnum.alignment = PP_ALIGN.RIGHT
        pnum.text = f"{n}/{len(SLIDES)}"
        pnum.font.name = "Calibri"
        pnum.font.size = Pt(10)
        pnum.font.bold = True
        pnum.font.color.rgb = RGBColor(*GREY_MUTED)

    for n, sd in enumerate(SLIDES, 1):
        sl = prs.slides.add_slide(blank)

        # --- SLIDE 1: COVER ---
        if sd.get("kind") == "cover":
            rect(sl, 0, 0, W_IN, H_IN, NAVY)

            # Logo Telkom University badge
            badge_path = FIG / "logo_telkom_badge.png"
            if badge_path.exists():
                sl.shapes.add_picture(str(badge_path), Inches(0.8), Inches(0.8), Inches(1.3), Inches(1.3))

            # Lembaga & Mata Kuliah
            tb_inst = sl.shapes.add_textbox(Inches(2.25), Inches(0.8), Inches(4.8), Inches(1.3))
            tf_inst = tb_inst.text_frame
            tf_inst.word_wrap = True
            p = tf_inst.paragraphs[0]
            p.text = "TELKOM UNIVERSITY"
            p.font.name = "Calibri"
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = RGBColor(255, 255, 255)
            p.space_after = Pt(2)

            p2 = tf_inst.add_paragraph()
            p2.text = "Fakultas Informatika · S1 Informatika"
            p2.font.name = "Calibri"
            p2.font.size = Pt(11)
            p2.font.color.rgb = RGBColor(*LIGHT_BLUE)
            p2.space_after = Pt(2)

            p3 = tf_inst.add_paragraph()
            p3.text = "Midterm Project Visualisasi Data (CAK4XBB3)"
            p3.font.name = "Calibri"
            p3.font.size = Pt(11)
            p3.font.bold = True
            p3.font.color.rgb = RGBColor(*ACCENT_LIGHT)

            # Judul Utama
            tb_title = sl.shapes.add_textbox(Inches(0.8), Inches(2.35), Inches(6.4), Inches(2.7))
            tf_title = tb_title.text_frame
            tf_title.word_wrap = True

            pt0 = tf_title.paragraphs[0]
            pt0.text = "Laporan Analisis Time Series:"
            pt0.font.name = "Calibri"
            pt0.font.size = Pt(18)
            pt0.font.color.rgb = RGBColor(*LIGHT_BLUE)
            pt0.space_after = Pt(4)

            pt1 = tf_title.add_paragraph()
            pt1.text = "Pasar Saham & Portofolio Finansial"
            pt1.font.name = "Calibri"
            pt1.font.size = Pt(32)
            pt1.font.bold = True
            pt1.font.color.rgb = RGBColor(255, 255, 255)
            pt1.space_after = Pt(4)

            pt2 = tf_title.add_paragraph()
            pt2.text = "(2020–2026)"
            pt2.font.name = "Calibri"
            pt2.font.size = Pt(26)
            pt2.font.bold = True
            pt2.font.color.rgb = RGBColor(*ACCENT)

            # Aksen & Subtitle Kiri
            rect(sl, 0.8, 5.25, 2.2, 0.06, ACCENT)

            tb_sub = sl.shapes.add_textbox(Inches(0.8), Inches(5.45), Inches(6.4), Inches(1.5))
            tf_sub = tb_sub.text_frame
            tf_sub.word_wrap = True

            ps1 = tf_sub.paragraphs[0]
            ps1.text = "Kelompok Cihuy"
            ps1.font.name = "Calibri"
            ps1.font.size = Pt(15)
            ps1.font.bold = True
            ps1.font.color.rgb = RGBColor(255, 255, 255)
            ps1.space_after = Pt(3)

            ps2 = tf_sub.add_paragraph()
            ps2.text = "Komparasi Lintas 9 Aset Finansial dari 5 Kategori"
            ps2.font.name = "Calibri"
            ps2.font.size = Pt(12)
            ps2.font.color.rgb = RGBColor(*LIGHT_BLUE)
            ps2.space_after = Pt(2)

            ps3 = tf_sub.add_paragraph()
            ps3.text = "Data Harian (2 Jan 2020 – 30 Okt 2026) · Sumber: Yahoo Finance"
            ps3.font.name = "Calibri"
            ps3.font.size = Pt(11)
            ps3.font.color.rgb = RGBColor(*ACCENT_LIGHT)

            # Kolom Kanan: Tim Penyusun & Peran (Persis Tabel di Laporan)
            tb_hdr = sl.shapes.add_textbox(Inches(7.6), Inches(0.8), Inches(4.9), Inches(0.45))
            tf_hdr = tb_hdr.text_frame
            ph = tf_hdr.paragraphs[0]
            ph.text = "TIM PENYUSUN & PERAN"
            ph.font.name = "Calibri"
            ph.font.size = Pt(14)
            ph.font.bold = True
            ph.font.color.rgb = RGBColor(*ACCENT)

            rect(sl, 7.6, 1.25, 4.9, 0.04, ACCENT)

            tb_team = sl.shapes.add_textbox(Inches(7.6), Inches(1.35), Inches(4.9), Inches(5.6))
            tf_team = tb_team.text_frame
            tf_team.word_wrap = True

            for idx, (nm, nim, role) in enumerate(ANGGOTA, 1):
                p_nm = tf_team.paragraphs[0] if idx == 1 else tf_team.add_paragraph()
                p_nm.space_after = Pt(1)
                r_num = p_nm.add_run()
                r_num.text = f"{idx}. {nm} "
                r_num.font.name = "Calibri"
                r_num.font.size = Pt(12)
                r_num.font.bold = True
                r_num.font.color.rgb = RGBColor(255, 255, 255)

                r_nim = p_nm.add_run()
                r_nim.text = f"({nim})"
                r_nim.font.name = "Calibri"
                r_nim.font.size = Pt(11)
                r_nim.font.color.rgb = RGBColor(*LIGHT_BLUE)

                p_rl = tf_team.add_paragraph()
                p_rl.space_after = Pt(8)
                r_rl = p_rl.add_run()
                r_rl.text = f"    • {role}"
                r_rl.font.name = "Calibri"
                r_rl.font.size = Pt(10.5)
                r_rl.font.color.rgb = RGBColor(*ACCENT_LIGHT)
            continue

        # Header untuk Slide 2 s.d. 10
        header(sl, sd["title"], sd["presenter"], sd["role"], n)
        top = 1.25

        # --- SLIDE 2 & 10: MULTI-COLUMN (2 atau 3 Kolom) ---
        if "columns" in sd:
            k = len(sd["columns"])
            gap = 0.35
            total_w = W_IN - 1.0
            cw = (total_w - gap * (k - 1)) / k

            for i, (h, items) in enumerate(sd["columns"]):
                x = 0.5 + i * (cw + gap)

                # Card background & accent bar
                rect(sl, x, top, cw, 5.5, CARD_BG)
                rect(sl, x, top, cw, 0.06, ACCENT)

                tb = sl.shapes.add_textbox(Inches(x + 0.15), Inches(top + 0.15), Inches(cw - 0.3), Inches(5.2))
                tf = tb.text_frame
                tf.word_wrap = True

                # Header kolom
                p_h = tf.paragraphs[0]
                p_h.text = h
                p_h.font.name = "Calibri"
                p_h.font.size = Pt(17 if k == 2 else 15)
                p_h.font.bold = True
                p_h.font.color.rgb = RGBColor(*NAVY)
                p_h.space_after = Pt(10)

                # Bullet points
                for item in items:
                    add_para_with_runs(tf, "• " + item, default_size=12 if k == 3 else 13, space_after=8)

        # --- SLIDE 9: 2 KOLOM KESIMPULAN (8 Insight Utama) ---
        elif "insights_2col" in sd:
            col_w = (W_IN - 1.0 - 0.4) / 2
            for c_idx, col_items in enumerate(sd["insights_2col"]):
                x = 0.5 + c_idx * (col_w + 0.4)
                tb = sl.shapes.add_textbox(Inches(x), Inches(top), Inches(col_w), Inches(5.6))
                tf = tb.text_frame
                tf.word_wrap = True

                for it_idx, (it_title, it_desc) in enumerate(col_items):
                    p_t = tf.paragraphs[0] if (it_idx == 0) else tf.add_paragraph()
                    p_t.space_after = Pt(2)
                    r_t = p_t.add_run()
                    r_t.text = it_title
                    r_t.font.name = "Calibri"
                    r_t.font.size = Pt(13)
                    r_t.font.bold = True
                    r_t.font.color.rgb = RGBColor(*NAVY)

                    p_d = tf.add_paragraph()
                    p_d.space_after = Pt(10)
                    r_d = p_d.add_run()
                    r_d.text = it_desc
                    r_d.font.name = "Calibri"
                    r_d.font.size = Pt(11.5)
                    r_d.font.color.rgb = RGBColor(*GREY)

        # --- SLIDE 3 s.d. 8: GAMBAR + BULLET POINTS ---
        else:
            ih_max = 5.5
            if "images" in sd:
                # 2 gambar vertikal
                gap_img = 0.15
                h_each = (ih_max - gap_img) / 2
                y_curr = top
                max_w_seen = 0
                for im in sd["images"]:
                    w, h = fit_box(im, 7.2, h_each)
                    sl.shapes.add_picture(str(FIG / im), Inches(0.5), Inches(y_curr), Inches(w), Inches(h))
                    max_w_seen = max(max_w_seen, w)
                    y_curr += h + gap_img

                text_x = 0.5 + max_w_seen + 0.35
                text_w = W_IN - text_x - 0.5
            else:
                # 1 gambar tunggal
                w, h = fit_box(sd["image"], 7.4, ih_max)
                img_y = top + (ih_max - h) / 2
                sl.shapes.add_picture(str(FIG / sd["image"]), Inches(0.5), Inches(img_y), Inches(w), Inches(h))

                text_x = 0.5 + w + 0.35
                text_w = W_IN - text_x - 0.5

            tb = sl.shapes.add_textbox(Inches(text_x), Inches(top + 0.1), Inches(text_w), Inches(ih_max))
            tf = tb.text_frame
            tf.word_wrap = True

            for b in sd["bullets"]:
                add_para_with_runs(tf, "• " + b, default_size=13, default_color=GREY, space_after=10)

    out = OUT / "Slide_Midterm_Kelompok_Cihuy.pptx"
    prs.save(out)
    return out


# ======================================================================
# PDF BUILDER (Menggunakan ReportLab)
# ======================================================================
def build_pdf():
    from reportlab.lib.colors import Color
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    from reportlab.platypus import Paragraph

    fdir = Path("C:/Windows/Fonts")
    try:
        pdfmetrics.registerFont(TTFont("Cal", str(fdir / "calibri.ttf")))
        pdfmetrics.registerFont(TTFont("Cal-B", str(fdir / "calibrib.ttf")))
        pdfmetrics.registerFont(TTFont("Cal-I", str(fdir / "calibrii.ttf")))
        pdfmetrics.registerFontFamily("Cal", normal="Cal", bold="Cal-B", italic="Cal-I", boldItalic="Cal-B")
        F, FB, FI = "Cal", "Cal-B", "Cal-I"
    except Exception:
        F, FB, FI = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"

    PT = 72
    W, H = W_IN * PT, H_IN * PT

    def col(rgb):
        return Color(*(c / 255.0 for c in rgb))

    def rect(c, x, y_top, w, h, rgb):
        c.setFillColor(col(rgb))
        c.rect(x * PT, H - (y_top + h) * PT, w * PT, h * PT, stroke=0, fill=1)

    def draw_p(c, text_content, x, y_top, w, size=13, rgb=GREY, bold=False, space=6, highlight_bold=False):
        # Format HTML tags
        t = text_content
        # Escape raw ampersands not already part of an entity
        t = re.sub(r"&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)", "&amp;", t)
        t = t.replace("<code>", "<b>").replace("</code>", "</b>")
        if highlight_bold:
            t = re.sub(r"<b>(.*?)</b>", r"<font color='#1F3A5F'><b>\1</b></font>", t)

        st = ParagraphStyle(
            "p_style",
            fontName=FB if bold else F,
            fontSize=size,
            leading=size * 1.25,
            textColor=col(rgb),
        )
        p = Paragraph(t, st)
        _, h = p.wrap(w * PT, H)
        p.drawOn(c, x * PT, H - y_top * PT - h)
        return y_top + (h / PT) + (space / PT)

    out = OUT / "Slide_Midterm_Kelompok_Cihuy.pdf"
    c = canvas.Canvas(str(out), pagesize=(W, H))
    c.setTitle("Slide Presentasi Midterm Visualisasi Data - Kelompok Cihuy")

    for n, sd in enumerate(SLIDES, 1):
        # --- SLIDE 1: COVER ---
        if sd.get("kind") == "cover":
            rect(c, 0, 0, W_IN, H_IN, NAVY)

            # Logo Telkom
            badge_path = FIG / "logo_telkom_badge.png"
            if badge_path.exists():
                c.drawImage(str(badge_path), 0.8 * PT, H - (0.8 + 1.3) * PT, 1.3 * PT, 1.3 * PT)

            # Lembaga & Mata Kuliah
            y = 0.8
            y = draw_p(c, "<b>TELKOM UNIVERSITY</b>", 2.25, y, 4.8, size=14, rgb=WHITE, space=3)
            y = draw_p(c, "Fakultas Informatika · S1 Informatika", 2.25, y, 4.8, size=11, rgb=LIGHT_BLUE, space=3)
            draw_p(c, "<b>Midterm Project Visualisasi Data (CAK4XBB3)</b>", 2.25, y, 4.8, size=11, rgb=ACCENT_LIGHT, space=0)

            # Judul Utama
            y = 2.4
            y = draw_p(c, "Laporan Analisis Time Series:", 0.8, y, 6.4, size=18, rgb=LIGHT_BLUE, space=4)
            y = draw_p(c, "<b>Pasar Saham & Portofolio Finansial</b>", 0.8, y, 6.4, size=32, rgb=WHITE, space=4)
            y = draw_p(c, "<b>(2020–2026)</b>", 0.8, y, 6.4, size=26, rgb=ACCENT, space=0)

            # Aksen & Subtitle Kiri
            rect(c, 0.8, 5.25, 2.2, 0.06, ACCENT)
            y = 5.45
            y = draw_p(c, "<b>Kelompok Cihuy</b>", 0.8, y, 6.4, size=15, rgb=WHITE, space=3)
            y = draw_p(c, "Komparasi Lintas 9 Aset Finansial dari 5 Kategori", 0.8, y, 6.4, size=12, rgb=LIGHT_BLUE, space=3)
            draw_p(c, "Data Harian (2 Jan 2020 – 30 Okt 2026) · Sumber: Yahoo Finance", 0.8, y, 6.4, size=11, rgb=ACCENT_LIGHT, space=0)

            # Kolom Kanan: Tim Penyusun & Peran
            draw_p(c, "<b>TIM PENYUSUN & PERAN</b>", 7.6, 0.8, 4.9, size=14, rgb=ACCENT, space=0)
            rect(c, 7.6, 1.25, 4.9, 0.04, ACCENT)

            y_m = 1.4
            for idx, (nm, nim, role) in enumerate(ANGGOTA, 1):
                y_m = draw_p(c, f"<b>{idx}. {nm}</b> <font color='#CFDBE8'>({nim})</font>", 7.6, y_m, 4.9, size=12, rgb=WHITE, space=2)
                y_m = draw_p(c, f"• <font color='#F7D488'>{role}</font>", 7.85, y_m, 4.65, size=10.5, rgb=ACCENT_LIGHT, space=9)

            c.showPage()
            continue

        # Header Navbar untuk Slide 2 s.d. 10
        rect(c, 0, 0, W_IN, 0.95, NAVY)
        rect(c, 0, 0.95, W_IN, 0.05, ACCENT)

        # Judul
        c.setFillColor(col(WHITE))
        c.setFont(FB, 24)
        c.drawString(0.5 * PT, H - 0.62 * PT, sd["title"])

        # Presenter di kanan atas
        c.setFont(F, 10)
        c.setFillColor(col(LIGHT_BLUE))
        c.drawRightString((W_IN - 0.5) * PT, H - 0.38 * PT, f"Presenter: {sd['presenter']}")
        c.setFont(FB, 10.5)
        c.setFillColor(col(ACCENT_LIGHT))
        c.drawRightString((W_IN - 0.5) * PT, H - 0.62 * PT, sd["role"])

        # Footer
        rect(c, 0.5, 7.0, W_IN - 1.0, 0.02, (0xDD, 0xDD, 0xDD))
        c.setFont(F, 9.5)
        c.setFillColor(col(GREY_MUTED))
        c.drawString(0.5 * PT, 0.25 * PT, "Midterm Project Visualisasi Data (CAK4XBB3) · Kelompok Cihuy · Telkom University")
        c.setFont(FB, 10)
        c.drawRightString((W_IN - 0.5) * PT, 0.25 * PT, f"{n}/{len(SLIDES)}")

        top = 1.25

        # --- SLIDE 2 & 10: MULTI-COLUMN (2 atau 3 Kolom) ---
        if "columns" in sd:
            k = len(sd["columns"])
            gap = 0.35
            total_w = W_IN - 1.0
            cw = (total_w - gap * (k - 1)) / k

            for i, (h, items) in enumerate(sd["columns"]):
                x = 0.5 + i * (cw + gap)
                rect(c, x, top, cw, 5.5, CARD_BG)
                rect(c, x, top, cw, 0.06, ACCENT)

                y_col = top + 0.18
                y_col = draw_p(c, f"<b>{h}</b>", x + 0.15, y_col, cw - 0.3, size=16 if k == 2 else 14.5, rgb=NAVY, space=10)

                for item in items:
                    y_col = draw_p(c, "• " + item, x + 0.15, y_col, cw - 0.3, size=11.5 if k == 3 else 12.5, space=8, highlight_bold=True)

        # --- SLIDE 9: 2 KOLOM KESIMPULAN (8 Insight Utama) ---
        elif "insights_2col" in sd:
            col_w = (W_IN - 1.0 - 0.4) / 2
            for c_idx, col_items in enumerate(sd["insights_2col"]):
                x = 0.5 + c_idx * (col_w + 0.4)
                y_ins = top + 0.1
                for it_title, it_desc in col_items:
                    y_ins = draw_p(c, f"<b>{it_title}</b>", x, y_ins, col_w, size=13, rgb=NAVY, space=2)
                    y_ins = draw_p(c, it_desc, x, y_ins, col_w, size=11.5, rgb=GREY, space=10)

        # --- SLIDE 3 s.d. 8: GAMBAR + BULLET POINTS ---
        else:
            ih_max = 5.5
            if "images" in sd:
                gap_img = 0.15
                h_each = (ih_max - gap_img) / 2
                y_curr = top
                max_w_seen = 0
                for im in sd["images"]:
                    w, h = fit_box(im, 7.2, h_each)
                    c.drawImage(str(FIG / im), 0.5 * PT, H - (y_curr + h) * PT, w * PT, h * PT)
                    max_w_seen = max(max_w_seen, w)
                    y_curr += h + gap_img

                text_x = 0.5 + max_w_seen + 0.35
                text_w = W_IN - text_x - 0.5
            else:
                w, h = fit_box(sd["image"], 7.4, ih_max)
                img_y = top + (ih_max - h) / 2
                c.drawImage(str(FIG / sd["image"]), 0.5 * PT, H - (img_y + h) * PT, w * PT, h * PT)

                text_x = 0.5 + w + 0.35
                text_w = W_IN - text_x - 0.5

            y_b = top + 0.12
            for b in sd["bullets"]:
                y_b = draw_p(c, "• " + b, text_x, y_b, text_w, size=12.5, space=10, highlight_bold=True)

        c.showPage()

    c.save()
    return out


if __name__ == "__main__":
    pptx_path = build_pptx()
    print("PPTX Berhasil:", pptx_path.name)
    pdf_path = build_pdf()
    print("PDF Berhasil:", pdf_path.name, f"({len(SLIDES)} slide)")
