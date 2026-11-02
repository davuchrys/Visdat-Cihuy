"""
Unduh data harga harian dari Yahoo Finance (https://finance.yahoo.com) via library yfinance.

Jalankan dari root folder proyek:
    python data/download_data.py

Hasil:
    data/raw_yahoo_finance.csv  -> data mentah (format long: Date, Ticker, Open, High, Low, Close, Volume)
    data/close_clean.csv        -> harga penutupan (Close) bersih, format wide, hari kerja Senin-Jumat
    data/volume_clean.csv       -> volume transaksi bersih, format wide
"""
from pathlib import Path

import pandas as pd
import yfinance as yf

START = "2020-01-01"
END = "2026-11-01"  # yfinance: tanggal END tidak ikut -> data sampai 31 Okt 2026

# Ticker Yahoo Finance -> (nama pendek, kategori)
ASSETS = {
    "^JKSE":   ("IHSG",      "Indeks"),
    "^GSPC":   ("S&P 500",   "Indeks"),
    "BBCA.JK": ("BBCA",      "Saham Bank"),
    "BBRI.JK": ("BBRI",      "Saham Bank"),
    "BMRI.JK": ("BMRI",      "Saham Bank"),
    "BBNI.JK": ("BBNI",      "Saham Bank"),
    "BTC-USD": ("Bitcoin",   "Kripto"),
    "GC=F":    ("Emas",      "Komoditas"),
    "IDR=X":   ("USD/IDR",   "Kurs"),
}

OUT = Path(__file__).resolve().parent


def main():
    raw = yf.download(list(ASSETS), start=START, end=END,
                      auto_adjust=True, progress=False, group_by="column")

    # 1. Simpan data mentah dalam format long
    long = (raw.stack(level="Ticker", future_stack=True)
               .reset_index()
               .rename(columns={"level_1": "Ticker"}))
    long["Nama"] = long["Ticker"].map(lambda t: ASSETS[t][0])
    long["Kategori"] = long["Ticker"].map(lambda t: ASSETS[t][1])
    long = long.dropna(subset=["Close"])
    long = long[["Date", "Ticker", "Nama", "Kategori", "Open", "High", "Low", "Close", "Volume"]]
    long.to_csv(OUT / "raw_yahoo_finance.csv", index=False)

    # 2. Cleaning harga penutupan
    close = raw["Close"].rename(columns=lambda t: ASSETS[t][0])
    close = close[close.index.dayofweek < 5]       # Bitcoin buka 7 hari -> samakan ke hari kerja
    close = close.dropna(how="all")                 # buang hari yang semua pasar libur
    close = close.ffill(limit=5)                    # libur bursa lokal (Lebaran dsb.) diisi harga terakhir
    close = close.dropna()                          # sisa NaN di awal periode dibuang
    close.index.name = "Date"
    close.to_csv(OUT / "close_clean.csv")

    # 3. Cleaning volume (tidak di-ffill: hari libur = tidak ada transaksi)
    volume = raw["Volume"].rename(columns=lambda t: ASSETS[t][0])
    volume = volume.reindex(close.index).fillna(0)
    volume.to_csv(OUT / "volume_clean.csv")

    print("raw   :", long.shape, long["Date"].min().date(), "->", long["Date"].max().date())
    print("close :", close.shape, close.index.min().date(), "->", close.index.max().date())
    print("volume:", volume.shape)


if __name__ == "__main__":
    main()
