#!/usr/bin/env python3
"""
Script test untuk memverifikasi bahwa eksplorasi data properti DIY berjalan dengan benar.
"""

import os
import pandas as pd
import subprocess
import sys

def test_data_exploration():
    """
    Test untuk memverifikasi bahwa script eksplorasi data berjalan dengan benar.
    """
    print("🧪 Testing script eksplorasi data properti DIY...")
    
    # List file yang diharapkan akan dibuat
    expected_files = [
        'statistik_deskriptif_properti_diy.csv',
        'histogram_harga_properti_diy.png',
        'histogram_luas_properti_diy.png',
        'heatmap_korelasi_properti_diy.png'
    ]
    
    # Hapus file output sebelumnya jika ada
    for file in expected_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"🗑️  Menghapus file lama: {file}")
    
    # Jalankan script eksplorasi data
    print("▶️  Menjalankan script eksplorasi data...")
    try:
        result = subprocess.run([sys.executable, 'eksplorasi_data_properti_diy.py'], 
                              capture_output=True, text=True, timeout=120)
        
        if result.returncode != 0:
            print(f"❌ Script gagal dijalankan: {result.stderr}")
            return False
        
        print("✅ Script berhasil dijalankan")
        
    except subprocess.TimeoutExpired:
        print("❌ Script timeout (>120 detik)")
        return False
    except Exception as e:
        print(f"❌ Error menjalankan script: {e}")
        return False
    
    # Periksa apakah semua file output dibuat
    missing_files = []
    for file in expected_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            file_size = os.path.getsize(file)
            print(f"✅ {file} dibuat dengan ukuran {file_size:,} bytes")
    
    if missing_files:
        print(f"❌ File yang hilang: {missing_files}")
        return False
    
    # Periksa isi file CSV statistik
    try:
        stats_df = pd.read_csv('statistik_deskriptif_properti_diy.csv')
        expected_variables = ['Harga', 'Luas_Tanah', 'Luas_Bangunan', 'Kamar', 'WC', 'Parkir']
        
        if len(stats_df) != len(expected_variables):
            print(f"❌ Jumlah variabel dalam statistik tidak sesuai: {len(stats_df)} vs {len(expected_variables)}")
            return False
        
        # Periksa kolom yang diperlukan
        required_columns = ['Variabel', 'Min', 'Q1', 'Median', 'Q3', 'Max', 'Mean', 'Std', 'Count']
        missing_columns = [col for col in required_columns if col not in stats_df.columns]
        
        if missing_columns:
            print(f"❌ Kolom yang hilang dalam statistik: {missing_columns}")
            return False
        
        print("✅ File CSV statistik valid")
        
    except Exception as e:
        print(f"❌ Error membaca file statistik: {e}")
        return False
    
    print("🎉 Semua test berhasil!")
    return True

if __name__ == "__main__":
    success = test_data_exploration()
    sys.exit(0 if success else 1)