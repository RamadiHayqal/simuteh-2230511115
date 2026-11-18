"""praproses.py: rangkaian praproses SIMUTEH untuk dipakai mulai P5."""
import json
from pathlib import Path

import cv2
import numpy as np

PARAM_BAWAAN = {
    "lebar": 640,
    "gamma": 1.0,
    "clahe_clip": 2.0,
    "clahe_tile": 8,
    "penapis": "rerata",  # none, rerata, gaussian, median
    "kernel": 5,
    "sigma": 1.0,
    "tajam_k": 0.0,
}


def gamma_lut(gamma):
    gamma = float(gamma)
    if gamma <= 0:
        raise ValueError("Gamma harus lebih besar dari nol.")
    values = 255.0 * (np.arange(256, dtype=np.float32) / 255.0) ** gamma
    return np.clip(values, 0, 255).astype(np.uint8)


def praproses(img_bgr, p=None):
    """Urutan: ubah ukuran -> gamma -> CLAHE kanal V -> redam derau -> tajamkan."""
    if img_bgr is None or img_bgr.ndim != 3 or img_bgr.shape[2] != 3:
        raise ValueError("Masukan harus berupa citra warna BGR tiga kanal.")
    param = {**PARAM_BAWAAN, **(p or {})}

    lebar = int(param["lebar"])
    if lebar <= 0:
        raise ValueError("Parameter lebar harus lebih besar dari nol.")
    tinggi_asli, lebar_asli = img_bgr.shape[:2]
    tinggi_baru = max(1, int(round(tinggi_asli * lebar / lebar_asli)))
    img = cv2.resize(img_bgr, (lebar, tinggi_baru), interpolation=cv2.INTER_AREA)

    gamma = float(param["gamma"])
    if gamma != 1.0:
        img = cv2.LUT(img, gamma_lut(gamma))

    clip = float(param["clahe_clip"])
    tile = int(param["clahe_tile"])
    if tile < 1:
        raise ValueError("clahe_tile harus minimal 1.")
    if clip > 0:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(tile, tile))
        hsv[:, :, 2] = clahe.apply(hsv[:, :, 2])
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    jenis = str(param["penapis"]).lower()
    kernel = int(param["kernel"])
    if kernel < 1 or kernel % 2 == 0:
        raise ValueError("Ukuran kernel harus bilangan ganjil dan lebih dari nol.")
    if jenis == "rerata":
        img = cv2.blur(img, (kernel, kernel))
    elif jenis == "gaussian":
        img = cv2.GaussianBlur(img, (kernel, kernel), float(param["sigma"]))
    elif jenis == "median":
        img = cv2.medianBlur(img, kernel)
    elif jenis != "none":
        raise ValueError("Jenis penapis harus none/rerata/gaussian/median.")

    tajam_k = float(param["tajam_k"])
    if tajam_k > 0:
        blur = cv2.GaussianBlur(img, (5, 5), 1.0)
        img = cv2.addWeighted(img, 1.0 + tajam_k, blur, -tajam_k, 0)
    return img


def simpan_param(p, path="../hasil/param_praproses.json"):
    """Menyimpan parameter lengkap agar hasil dapat direproduksi."""
    target = Path(path)
    if not target.is_absolute():
        repo_root = Path(__file__).resolve().parents[1]
        # Jalur default pada petunjuk ditulis relatif terhadap folder notebook/.
        base = repo_root / "notebook" if target.parts and target.parts[0] == ".." else repo_root
        target = (base / target).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    hasil = {**PARAM_BAWAAN, **(p or {})}
    target.write_text(json.dumps(hasil, indent=2, ensure_ascii=False), encoding="utf-8")
    return target
