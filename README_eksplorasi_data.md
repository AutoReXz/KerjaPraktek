# Script Eksplorasi Data Properti DIY

## Deskripsi
Script Python untuk melakukan eksplorasi data properti DIY (Daerah Istimewa Yogyakarta) dengan dataset CSV yang berisi informasi harga, luas tanah, luas bangunan, kamar, WC, dan parkir.

## Fitur Utama

### 1. Analisis Statistik Deskriptif
- Menghitung statistik deskriptif (min, Q1, median, Q3, max, mean, std, count) untuk semua variabel numerik
- Menyimpan hasil ke file CSV: `statistik_deskriptif_properti_diy.csv`

### 2. Visualisasi Distribusi Harga
- Histogram harga dengan skala linear dan logaritmik
- Menandai median dengan garis vertikal merah
- Output: `histogram_harga_properti_diy.png`

### 3. Visualisasi Distribusi Luas
- Histogram luas tanah dan luas bangunan dalam 2 subplot
- Menandai median untuk masing-masing distribusi
- Output: `histogram_luas_properti_diy.png`

### 4. Heatmap Korelasi
- Menampilkan korelasi antar semua variabel numerik
- Menggunakan colormap yang mudah dibaca
- Output: `heatmap_korelasi_properti_diy.png`

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

### Instalasi Dependencies (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install -y python3-pandas python3-matplotlib python3-seaborn python3-numpy
```

## Cara Penggunaan

### Menjalankan Analisis
```bash
python3 eksplorasi_data_properti_diy.py
```

### Menjalankan Test
```bash
python3 test_eksplorasi_data.py
```

## Input
- File CSV: `databaru.csv` (harus berada di direktori yang sama)
- Kolom yang diperlukan:
  - `Harga`: Harga properti (Rupiah)
  - `Luas_Tanah`: Luas tanah (m²)
  - `Luas_Bangunan`: Luas bangunan (m²)
  - `Kamar`: Jumlah kamar
  - `WC`: Jumlah kamar mandi/WC
  - `Parkir`: Jumlah tempat parkir

## Output

### 1. File CSV
- `statistik_deskriptif_properti_diy.csv`: Berisi statistik deskriptif untuk semua variabel

### 2. File PNG (Resolusi Tinggi - 300 DPI)
- `histogram_harga_properti_diy.png`: Histogram distribusi harga (linear & log-scale)
- `histogram_luas_properti_diy.png`: Histogram distribusi luas tanah dan bangunan
- `heatmap_korelasi_properti_diy.png`: Heatmap korelasi antar variabel

## Contoh Output Statistik

```
💰 Harga:
   Min     : Rp       20.0 juta
   Q1      : Rp      550.0 juta
   Median  : Rp      850.0 juta
   Q3      : Rp     1500.0 juta
   Max     : Rp     3600.0 juta

🏠 Luas_Tanah:
   Min     :       21.0 m²
   Q1      :       91.0 m²
   Median  :      115.0 m²
   Q3      :      150.0 m²
   Max     :      251.0 m²
```

## Fitur Script

### Konfigurasi Visualisasi
- Font: DejaVu Sans (mendukung karakter Indonesia)
- Ukuran figure: 12x8 inch untuk plot tunggal, 16x6 untuk subplot
- Resolusi: 300 DPI untuk semua output PNG
- Grid dan styling yang konsisten

### Error Handling
- Penanganan file tidak ditemukan
- Pembersihan data dari nilai kosong
- Validasi input dan output

### Bahasa Indonesia
- Semua judul, label sumbu, dan output menggunakan Bahasa Indonesia
- Format angka yang sesuai untuk mata uang Rupiah dan satuan metrik

## Struktur Data yang Didukung
Script ini dirancang untuk dataset properti dengan struktur:
- Minimal 6 kolom numerik (Harga, Luas_Tanah, Luas_Bangunan, Kamar, WC, Parkir)
- Format CSV dengan header
- Data numerik yang valid (tanpa nilai kosong)

## Author
Copilot Assistant - 2024