"""utils_cv.py: fungsi bantu yang dipakai ulang sepanjang praktikum."""
from pathlib import Path

import cv2
import numpy as np
import matplotlib.pyplot as plt


def baca(path, gray=False):
    """Membaca citra; memberi pesan jelas jika berkas tidak ditemukan."""
    flag = cv2.IMREAD_GRAYSCALE if gray else cv2.IMREAD_COLOR
    img = cv2.imread(str(path), flag)
    if img is None:
        raise FileNotFoundError(f"Citra tidak ditemukan atau gagal dibaca: {path}")
    return img


def tampil(daftar, judul, baris=1, ukuran=(14, 4)):
    """Menampilkan citra BGR/keabuan berdampingan."""
    if len(daftar) != len(judul):
        raise ValueError("Jumlah citra dan judul harus sama.")
    if not daftar:
        raise ValueError("Daftar citra kosong.")
    kolom = int(np.ceil(len(daftar) / baris))
    plt.figure(figsize=ukuran)
    for i, (im, jd) in enumerate(zip(daftar, judul), 1):
        plt.subplot(baris, kolom, i)
        if im.ndim == 3:
            plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
        else:
            plt.imshow(im, cmap="gray", vmin=0, vmax=255)
        plt.title(jd)
        plt.axis("off")
    plt.tight_layout()


def kontras_bercak(kanal, mask_daun, mask_bercak):
    """KB = |rerata bercak - rerata daun sehat| / simpangan baku daun sehat."""
    if kanal.shape[:2] != mask_daun.shape[:2] or kanal.shape[:2] != mask_bercak.shape[:2]:
        raise ValueError("Ukuran kanal dan mask harus sama.")
    k = kanal.astype(np.float64)
    sehat = (mask_daun > 0) & (mask_bercak == 0)
    bercak = mask_bercak > 0
    if not bercak.any() or not sehat.any():
        return float("nan")
    return abs(k[bercak].mean() - k[sehat].mean()) / (k[sehat].std() + 1e-6)


def statistik(gray):
    """Statistik intensitas untuk diagnosis mutu citra."""
    return {
        "rerata": round(float(gray.mean()), 1),
        "simpangan_baku": round(float(gray.std()), 1),
        "min": int(gray.min()),
        "maks": int(gray.max()),
        "persen_gelap": round(100 * float((gray < 50).mean()), 1),
        "persen_terang": round(100 * float((gray > 205).mean()), 1),
    }
