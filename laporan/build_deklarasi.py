"""Membuat dokumen PDF resmi Deklarasi Penggunaan AI Keseluruhan Anggota.

Jalankan dari root repo:  python laporan/build_deklarasi.py
Hasil: laporan/Deklarasi_AI_Kelompok_Cihuy.pdf
"""
from pathlib import Path
import re

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "laporan" / "Deklarasi_AI_Kelompok_Cihuy.pdf"

NAVY = HexColor("#1F3A5F")
ACCENT = HexColor("#E69F00")
GREY_TEXT = HexColor("#2D3748")
GREY_MUTED = HexColor("#718096")
TABLE_HEADER_BG = HexColor("#1F3A5F")
ROW_ALT_BG = HexColor("#F7FAFC")
BORDER_COLOR = HexColor("#CBD5E0")

# Register fonts
fdir = Path("C:/Windows/Fonts")
try:
    pdfmetrics.registerFont(TTFont("Cal", str(fdir / "calibri.ttf")))
    pdfmetrics.registerFont(TTFont("Cal-B", str(fdir / "calibrib.ttf")))
    pdfmetrics.registerFont(TTFont("Cal-I", str(fdir / "calibrii.ttf")))
    pdfmetrics.registerFontFamily("Cal", normal="Cal", bold="Cal-B", italic="Cal-I", boldItalic="Cal-B")
    F, FB, FI = "Cal", "Cal-B", "Cal-I"
except Exception:
    F, FB, FI = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"

# Data Tabel 1: Rekapitulasi Penggunaan AI
DATA_PENGGUNAAN = [
    (
        "1",
        "<b>Adhyatma Chrysostomos Davu</b><br/><font color='#718096'>103012340479</font>",
        "Claude<br/>(Claude Code)",
        "Perencanaan proyek",
        "Membaca soal, membagi jobdesk 5 anggota, membuat struktur folder & panduan pengerjaan di README.md",
        "Sedang",
    ),
    (
        "2",
        "<b>Adhyatma Chrysostomos Davu</b><br/><font color='#718096'>103012340479</font>",
        "Claude<br/>(Claude Code)",
        "Dataset & kerangka notebook",
        "Script unduh data Yahoo Finance (download_data.py), cleaning (long ke wide, hari kerja, f-fill libur), data profiling, kerangka notebook (sel load & cleaning), draf laporan Bab 1–2",
        "Tinggi",
    ),
    (
        "3",
        "<b>Raffa Anung El Haqqi</b><br/><font color='#718096'>103012300163</font>",
        "Claude<br/>(Claude Code)",
        "Line Plot & Area Plot<br/>(bagian 3.1–3.2)",
        "Menulis kode Line Plot IHSG dan Area Plot volume 4 saham bank (stacked), sel verifikasi perbandingan nilai rupiah vs lembar saham, draf interpretasi, dan penjelasan alur kode",
        "Tinggi",
    ),
    (
        "4",
        "<b>Tristan Satria Perdana Hermawan</b><br/><font color='#718096'>103012300253</font>",
        "Antigravity<br/>(Google DeepMind)",
        "Multiple Time Series & Calendar Heatmap<br/>(bagian 3.3–3.4)",
        "Menulis kode Multiple Time Series (basis 100, skala log, direct labeling) dan Calendar Heatmap return harian IHSG (skala divergen), beserta interpretasi analitis",
        "Tinggi",
    ),
    (
        "5",
        "<b>Naufal Rafif Hidayat</b><br/><font color='#718096'>103012300403</font>",
        "Claude<br/>(Claude Code)",
        "Analisis Tren<br/>(bagian 4.1–4.2)",
        "Menulis kode Moving Average 20 & 200 hari, tabel trade-off window vs NaN, fitting numpy.polyfit linear, polinomial derajat 3, dan eksponensial Emas & Bitcoin, beserta interpretasi",
        "Tinggi",
    ),
    (
        "6",
        "<b>Ahmad Naufal Ramadhan</b><br/><font color='#718096'>103012300239</font>",
        "Antigravity<br/>(Google DeepMind)",
        "Kesimpulan, Deklarasi AI, Daftar Pustaka, draf awal laporan & slide",
        "Clone repo & membaca README, menyusun draf kesimpulan (8 insight, 6 kendala, 5 pengembangan), merekap tabel deklarasi AI semua anggota, melengkapi sitasi pustaka formal, membuat draf awal laporan PDF (5 hal) dan slide awal (10 slide)",
        "Tinggi",
    ),
    (
        "7",
        "<b>Ahmad Naufal Ramadhan</b><br/><font color='#718096'>103012300239</font>",
        "Google Gemini<br/>(Gemini Web)",
        "Parafrase & revisi narasi laporan (Bab 1–5)",
        "Mengubah narasi draf laporan agar mengalir alami, menghilangkan gaya listicle kaku, memperkaya terminologi sains data/keuangan otentik (fat tails, Runge's phenomenon, sideways), untuk dokumen Word & PDF final 11 halaman",
        "Sedang",
    ),
    (
        "8",
        "<b>Ahmad Naufal Ramadhan</b><br/><font color='#718096'>103012300239</font>",
        "Antigravity<br/>(Google DeepMind)",
        "Pembaruan Slide (PPTX & PDF) & Sinkronisasi Dokumen",
        "Menyelaraskan seluruh 10 slide presentasi dengan laporan final hasil editan (Bab 1–5, logo Telkom University, peran anggota, 8 insight utama format 2-kolom, kendala & rencana pengembangan) serta finalisasi log AI",
        "Sedang",
    ),
]

# Data Tabel 2: Rekap Prompt Utama
DATA_PROMPT = [
    (
        "<b>Adhyatma Chrysostomos Davu</b><br/><font color='#718096'>103012340479</font><br/><i>Koordinator & Data</i>",
        "• <i>kamu baca dulu kita disuruh apa di pdf itu. kelompokku ada 5 orang dan tolong bagi2 jobdesknya...</i><br/>"
        "• <i>Kelompok cihuy / topik : Pasar Saham & Keuangan / sumber dataset : https://finance.yahoo.com / Pakai semua dataset yang ada dari situ</i><br/>"
        "• <i>lakukan jobdeskku sekarang</i>",
        "Screenshot_AI_103012340479.pdf<br/><font color='#718096'>(hal. 1–9)</font>",
    ),
    (
        "<b>Raffa Anung El Haqqi</b><br/><font color='#718096'>103012300163</font><br/><i>Line & Area Plot</i>",
        "• <i>sekarang saya raffa baca readme yang ada dulu dan pahami</i><br/>"
        "• <i>oke sekarang saya harus ngapain dan gimana bantuin dulu ... bantu saya memahami dong</i><br/>"
        "• <i>coba sekarang interpretasi mu gimana setiap hasil tadi ... buatkan drafnya dan untuk interpretasinya kirim sini dulu saya mau pahami</i>",
        "Screenshot_AI_103012300163.pdf<br/><font color='#718096'>(hal. 1–8)</font>",
    ),
    (
        "<b>Tristan Satria Perdana Hermawan</b><br/><font color='#718096'>103012300253</font><br/><i>Multi Series & Heatmap</i>",
        "• <i>pelajari folder Visdat-Cihuy ini, baca juga README nya</i><br/>"
        "• <i>lanjutkan pengerjaan Bagian 3.3 dan 3.4, sesuaikan dengan pengerjaan teman teman saya seperti pembuatan log_ai nya dll</i>",
        "Screenshot_AI_103012300253.pdf<br/><font color='#718096'>(hal. 1–5)</font>",
    ),
    (
        "<b>Naufal Rafif Hidayat</b><br/><font color='#718096'>103012300403</font><br/><i>Analisis Tren (MA & Fit)</i>",
        "• <i>clone github ini https://github.com/davuchrys/Visdat-Cihuy.git kemudian kerjakan sesuai readme nya</i><br/>"
        "• (Pemilihan peran Naufal Rafif, instalasi dependensi, implementasi MA 20 & 200, tabel trade-off, fitting polinomial & eksponensial)",
        "Screenshot_AI_103012300403.pdf<br/><font color='#718096'>(hal. 1–6)</font>",
    ),
    (
        "<b>Ahmad Naufal Ramadhan</b><br/><font color='#718096'>103012300239</font><br/><i>Kesimpulan, Laporan, Slide</i>",
        "• <i>pelajari folder visdat-cihuy ini ... kerjakan 1. Notebook Bagian 5 (Kesimpulan) ... s.d. 6. Rekap Log AI</i><br/>"
        "• (Lampiran draf PDF) <i>ubah laporan tersebut agar terlihat natural</i><br/>"
        "• <i>perbarui lagi slide presentasinya menyesuaikan dengan laporan yang telah saya buat</i><br/>"
        "• <i>tambahkan percakapan kita sekarang ini dan percakapan di ss.pdf ke dalam log_ai NaufalRamadhan.md</i>",
        "Screenshot_AI_103012300239.pdf<br/><font color='#718096'>(hal. 1–7 & IDE Log)</font>",
    ),
]

ANGGOTA_SIGN = [
    ("Adhyatma Chrysostomos Davu", "103012340479", "Koordinator, Data & Kerangka"),
    ("Raffa Anung El Haqqi", "103012300163", "Line Plot & Area Plot"),
    ("Tristan Satria Perdana Hermawan", "103012300253", "Multiple Series & Heatmap"),
    ("Naufal Rafif Hidayat", "103012300403", "Analisis Tren (MA & Fitting)"),
    ("Ahmad Naufal Ramadhan", "103012300239", "Kesimpulan, Laporan & Slide"),
]


def build_pdf():
    # Setup document: A4 Landscape, 36pt (0.5 in) margins
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=landscape(A4),
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32,
    )

    styles = {
        "title": ParagraphStyle("DocTitle", fontName=FB, fontSize=18, leading=22, textColor=NAVY),
        "subtitle": ParagraphStyle("DocSub", fontName=F, fontSize=10.5, leading=14, textColor=GREY_MUTED),
        "statement": ParagraphStyle("DocStatement", fontName=F, fontSize=9, leading=12.5, textColor=GREY_TEXT),
        "sec_hdr": ParagraphStyle("SecHdr", fontName=FB, fontSize=12, leading=16, textColor=NAVY),
        "th": ParagraphStyle("TH", fontName=FB, fontSize=8.5, leading=11, textColor=HexColor("#FFFFFF"), alignment=1),
        "td": ParagraphStyle("TD", fontName=F, fontSize=7.5, leading=10, textColor=GREY_TEXT),
        "td_center": ParagraphStyle("TDC", fontName=F, fontSize=7.5, leading=10, textColor=GREY_TEXT, alignment=1),
        "td_bold": ParagraphStyle("TDB", fontName=FB, fontSize=7.5, leading=10, textColor=NAVY),
        "td_p": ParagraphStyle("TDP", fontName=F, fontSize=7.5, leading=9.5, textColor=GREY_TEXT),
        "sign_name": ParagraphStyle("SName", fontName=FB, fontSize=8, leading=10, textColor=NAVY, alignment=1),
        "sign_nim": ParagraphStyle("SNIM", fontName=F, fontSize=7.5, leading=9.5, textColor=GREY_MUTED, alignment=1),
        "sign_role": ParagraphStyle("SRole", fontName=F, fontSize=7, leading=9, textColor=HexColor("#4A5568"), alignment=1),
    }

    story = []

    # ================= PAGE 1 =================
    # Header
    story.append(Paragraph("Deklarasi Penggunaan AI", styles["title"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Midterm Project Visualisasi Data (CAK4XBB3) · Kelompok Cihuy · Telkom University", styles["subtitle"]))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceBefore=0, spaceAfter=6))

    # Statement
    statement_text = (
        "Kami menyatakan dengan sebenar-benarnya bahwa dalam pengerjaan Midterm Project Visualisasi Data ini kami memanfaatkan bantuan "
        "AI generatif sebagaimana dirinci secara transparan pada tabel di bawah ini. Seluruh kode, visualisasi, analisis tren, dan dokumen "
        "laporan telah kami telaah, uji, pahami, dan verifikasi secara mandiri. Kami bertanggung jawab penuh atas seluruh isi dan integritas "
        "akademik tugas ini. Dokumentasi komprehensif (prompt asli, jawaban, serta tangkapan layar percakapan) tersimpan di folder <b>Log/</b> "
        "(file <code>log_ai_&lt;nama&gt;.md</code> dan <code>Screenshot_AI_&lt;NIM&gt;.pdf</code>)."
    )
    story.append(Paragraph(statement_text, styles["statement"]))
    story.append(Spacer(1, 8))

    # Table 1: Rekapitulasi Penggunaan AI
    t1_headers = [
        Paragraph("No", styles["th"]),
        Paragraph("Anggota & NIM", styles["th"]),
        Paragraph("Tools AI", styles["th"]),
        Paragraph("Bagian yang Dibantu", styles["th"]),
        Paragraph("Bentuk Bantuan / Tujuan Prompt", styles["th"]),
        Paragraph("Ketergantungan", styles["th"]),
    ]

    t1_rows = [t1_headers]
    for row in DATA_PENGGUNAAN:
        t1_rows.append([
            Paragraph(row[0], styles["td_center"]),
            Paragraph(row[1], styles["td"]),
            Paragraph(row[2], styles["td_center"]),
            Paragraph(row[3], styles["td"]),
            Paragraph(row[4], styles["td_p"]),
            Paragraph(row[5], styles["td_center"]),
        ])

    col_widths_1 = [22, 115, 95, 125, 338, 74]
    t1 = Table(t1_rows, colWidths=col_widths_1, repeatRows=1)
    t1_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#FFFFFF")),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ])
    for r in range(1, len(t1_rows)):
        if r % 2 == 0:
            t1_style.add("BACKGROUND", (0, r), (-1, r), ROW_ALT_BG)
    t1.setStyle(t1_style)
    story.append(t1)

    # Page Break to Page 2
    story.append(PageBreak())

    # ================= PAGE 2 =================
    story.append(Paragraph("Rekapitulasi Prompt Utama & Pernyataan Integritas Tim", styles["title"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Kutipan Prompt Inti dari File Log dan Bukti Dokumen Screenshot per Anggota", styles["subtitle"]))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceBefore=0, spaceAfter=6))

    # Table 2: Rekap Prompt
    t2_headers = [
        Paragraph("Anggota & Peran", styles["th"]),
        Paragraph("Prompt Utama yang Digunakan (Dikutip Langsung dari Log AI)", styles["th"]),
        Paragraph("Bukti Screenshot di Log/", styles["th"]),
    ]

    t2_rows = [t2_headers]
    for row in DATA_PROMPT:
        t2_rows.append([
            Paragraph(row[0], styles["td"]),
            Paragraph(row[1], styles["td_p"]),
            Paragraph(row[2], styles["td_center"]),
        ])

    col_widths_2 = [140, 484, 145]
    t2 = Table(t2_rows, colWidths=col_widths_2, repeatRows=1)
    t2_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#FFFFFF")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ])
    for r in range(1, len(t2_rows)):
        if r % 2 == 0:
            t2_style.add("BACKGROUND", (0, r), (-1, r), ROW_ALT_BG)
    t2.setStyle(t2_style)
    story.append(t2)
    story.append(Spacer(1, 10))

    # Section 3: Sign-off block
    sign_intro = (
        "<i>Rincian setiap interaksi percakapan lengkap tersimpan di folder <b>Log/</b> (log_ai_Davu.md, log_ai_Raffa.md, "
        "log_ai_Tristan.md, log_ai_NaufalRafif.md, dan log_ai_NaufalRamadhan.md). Kami menyatakan tidak ada penggunaan tools AI "
        "lain di luar yang telah dicantumkan di atas.</i>"
    )
    story.append(Paragraph(sign_intro, styles["statement"]))
    story.append(Spacer(1, 12))

    # Signature Table (5 columns)
    sign_headers = [Paragraph("<b>Tanda Tangan &amp; Pengesahan Anggota Kelompok</b>", styles["sec_hdr"])]
    story.append(KeepTogether([
        Table([
            [Paragraph("<font color='#718096'>Bandung, 5 November 2026</font>", styles["td"])]
        ], colWidths=[769]),
        Spacer(1, 4),
    ]))

    sig_cols = []
    col_w_sig = 769 / 5
    for nm, nim, role in ANGGOTA_SIGN:
        cell_flowables = [
            Spacer(1, 24),  # space for physical signature
            Paragraph(f"<b>{nm}</b>", styles["sign_name"]),
            Paragraph(nim, styles["sign_nim"]),
            Paragraph(f"<i>{role}</i>", styles["sign_role"]),
        ]
        sig_cols.append(cell_flowables)

    # 1 row, 5 cells
    t_sig = Table([sig_cols], colWidths=[col_w_sig] * 5)
    t_sig.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("LINEBEFORE", (1, 0), (-1, -1), 0.5, HexColor("#E2E8F0")),
    ]))
    story.append(t_sig)

    # Page numbering canvas callback
    def add_page_decorations(canvas, doc):
        canvas.saveState()
        canvas.setFont(F, 8)
        canvas.setFillColor(HexColor("#718096"))
        # Header text
        canvas.drawString(36, 595.28 - 22, "Midterm Project Visualisasi Data (CAK4XBB3) · Kelompok Cihuy")
        # Footer text
        canvas.drawString(36, 20, "Dokumen Deklarasi Integritas Akademik Penggunaan AI · Telkom University")
        canvas.drawRightString(841.89 - 36, 20, f"Halaman {doc.page} dari 2")
        canvas.restoreState()

    doc.build(story, onFirstPage=add_page_decorations, onLaterPages=add_page_decorations)
    print("Dokumen Deklarasi AI Berhasil Dibuat:", OUT.name)
    return OUT


if __name__ == "__main__":
    build_pdf()

