# SIMUTEH – Repository Evaluasi Computer Vision P1–P4

**Mahasiswa:** Ramadi Hayqal Dwinugraha  
**NIM:** 2230511115  
**Kelas:** 7A  
**SEED:** 1115

## PENTING: gunakan folder baru ini secara utuh

Versi ini memperbaiki pemeriksaan SEED dan pencarian folder di Google Colab. Jangan mencampur notebook baru dengan modul `src/` dari folder lama.

## Cara memasang di Google Drive

1. Hapus atau pindahkan folder lama `simuteh-2230511115` dari `Drive Saya/Colab Notebooks` agar tidak terbaca sebagai versi aktif.
2. Ekstrak ZIP ini di komputer. Hasil ekstraksi harus berupa satu folder bernama `simuteh-2230511115`.
3. Upload **folder `simuteh-2230511115` secara utuh** ke `Drive Saya/Colab Notebooks`, bukan hanya file notebook.
4. Pastikan folder `src/` memuat `buat_dataset_sintetis.py`, `utils_cv.py`, dan `praproses.py`.
5. Buka `notebook/B1_lingkungan.ipynb` menggunakan Google Colab.
6. Jalankan sel persiapan. Izinkan Google Colab mengakses Drive saat diminta.
7. Jalankan B1, B2, B3, B4, dan B5 secara berurutan. Pilih **Runtime > Restart session** sebelum pengujian penuh dari awal.

## Struktur folder

```text
simuteh-2230511115/
├── data/sintetis/
│   ├── citra/
│   ├── bersih/
│   ├── mask_daun/
│   └── mask_bercak/
├── notebook/
│   ├── B1_lingkungan.ipynb
│   ├── B2_citra_warna.ipynb
│   ├── B3_histogram.ipynb
│   ├── B4_penapisan.ipynb
│   └── B5_praproses.ipynb
├── src/
│   ├── buat_dataset_sintetis.py
│   ├── utils_cv.py
│   └── praproses.py
├── hasil/
├── laporan/
├── requirements.txt
└── README.md
```

## SEED dan dataset

`src/buat_dataset_sintetis.py` memuat deklarasi tingkat modul `SEED = 1115`. Notebook memvalidasi nilai ini dengan empat digit terakhir NIM. Dataset dibuat otomatis oleh B1 bila belum lengkap. Dataset terdiri atas 60 citra (20 sehat, 20 ringan, 20 berat), masing-masing berukuran 640 × 480 piksel.

## Catatan Colab

- Tidak perlu menjalankan `pip install -r requirements.txt` jika pustaka telah tersedia di runtime Colab.
- Jika muncul pesan repository tidak ditemukan, periksa apakah nama folder tepat `simuteh-2230511115` dan seluruh folder `src/`, `notebook/`, `data/`, serta `hasil/` ikut terunggah.
- Jika ada folder lama dan baru yang sama-sama tersimpan, hapus folder lama. Notebook versi baru memvalidasi bahwa file generator berisi `SEED = 1115` sebelum memilih repository.

## Pemeriksaan paket

Kelima notebook telah dijalankan berurutan dalam kernel Python lokal dengan dataset 60 citra hasil generator SEED 1115; B1, B2, B3, B4, dan B5 selesai tanpa exception. Fungsi korelasi manual pada B4 memakai `sliding_window_view` agar pengujian citra 640 × 480 tidak bergantung pada loop Python yang sangat lambat. Uji lokal ini bukan pengganti pengujian akhir di akun Google Colab Anda.
