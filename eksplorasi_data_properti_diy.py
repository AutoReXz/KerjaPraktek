#!/usr/bin/env python3
"""
Script Python untuk Eksplorasi Data Properti DIY
Dibuat untuk analisis dataset properti DIY dengan visualisasi dan statistik deskriptif.

Author: Copilot Assistant
Date: 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Konfigurasi matplotlib untuk font yang mendukung bahasa Indonesia
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

def load_and_prepare_data(csv_file='databaru.csv'):
    """
    Memuat dan mempersiapkan data dari file CSV.
    
    Args:
        csv_file (str): Path ke file CSV
        
    Returns:
        pd.DataFrame: DataFrame yang sudah dipersiapkan
    """
    print("📊 Memuat data dari", csv_file)
    df = pd.read_csv(csv_file)
    
    # Kolom numerik yang akan dianalisis
    numeric_columns = ['Harga', 'Luas_Tanah', 'Luas_Bangunan', 'Kamar', 'WC', 'Parkir']
    
    # Bersihkan data dari nilai kosong
    df_clean = df[numeric_columns].dropna()
    
    print(f"✅ Data berhasil dimuat: {df_clean.shape[0]:,} properti dengan {len(numeric_columns)} variabel numerik")
    return df_clean

def calculate_descriptive_statistics(df):
    """
    Menghitung statistik deskriptif untuk semua variabel numerik.
    
    Args:
        df (pd.DataFrame): DataFrame input
        
    Returns:
        pd.DataFrame: DataFrame dengan statistik deskriptif
    """
    print("📈 Menghitung statistik deskriptif...")
    
    statistics = {}
    
    for column in df.columns:
        stats = {
            'Variabel': column,
            'Min': df[column].min(),
            'Q1': df[column].quantile(0.25),
            'Median': df[column].median(),
            'Q3': df[column].quantile(0.75),
            'Max': df[column].max(),
            'Mean': df[column].mean(),
            'Std': df[column].std(),
            'Count': df[column].count()
        }
        statistics[column] = stats
    
    stats_df = pd.DataFrame(statistics).T
    stats_df = stats_df.reset_index(drop=True)
    
    # Simpan ke CSV
    output_file = 'statistik_deskriptif_properti_diy.csv'
    stats_df.to_csv(output_file, index=False)
    print(f"💾 Statistik deskriptif disimpan ke: {output_file}")
    
    return stats_df

def create_price_histogram(df):
    """
    Membuat histogram harga dengan skala linear dan logaritmik.
    
    Args:
        df (pd.DataFrame): DataFrame input
    """
    print("📊 Membuat histogram harga...")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Histogram skala linear
    ax1.hist(df['Harga'], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    median_price = df['Harga'].median()
    ax1.axvline(median_price, color='red', linestyle='--', linewidth=2, 
                label=f'Median: Rp {median_price/1e9:.2f} M')
    ax1.set_xlabel('Harga (Rupiah)')
    ax1.set_ylabel('Frekuensi')
    ax1.set_title('Distribusi Harga Properti DIY (Skala Linear)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Format label sumbu x untuk skala linear
    ax1.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
    
    # Histogram skala logaritmik
    ax2.hist(df['Harga'], bins=50, alpha=0.7, color='lightgreen', edgecolor='black')
    ax2.axvline(median_price, color='red', linestyle='--', linewidth=2,
                label=f'Median: Rp {median_price/1e9:.2f} M')
    ax2.set_xlabel('Harga (Rupiah)')
    ax2.set_ylabel('Frekuensi')
    ax2.set_title('Distribusi Harga Properti DIY (Skala Logaritmik)')
    ax2.set_yscale('log')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Format label sumbu x untuk skala log
    ax2.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
    
    plt.tight_layout()
    
    # Simpan dengan resolusi tinggi
    output_file = 'histogram_harga_properti_diy.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"💾 Histogram harga disimpan ke: {output_file}")
    plt.close()

def create_area_histograms(df):
    """
    Membuat histogram untuk luas tanah dan luas bangunan.
    
    Args:
        df (pd.DataFrame): DataFrame input
    """
    print("📊 Membuat histogram luas tanah dan bangunan...")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Histogram luas tanah
    ax1.hist(df['Luas_Tanah'], bins=50, alpha=0.7, color='orange', edgecolor='black')
    median_land = df['Luas_Tanah'].median()
    ax1.axvline(median_land, color='red', linestyle='--', linewidth=2,
                label=f'Median: {median_land:.0f} m²')
    ax1.set_xlabel('Luas Tanah (m²)')
    ax1.set_ylabel('Frekuensi')
    ax1.set_title('Distribusi Luas Tanah Properti DIY')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Histogram luas bangunan
    ax2.hist(df['Luas_Bangunan'], bins=50, alpha=0.7, color='purple', edgecolor='black')
    median_building = df['Luas_Bangunan'].median()
    ax2.axvline(median_building, color='red', linestyle='--', linewidth=2,
                label=f'Median: {median_building:.0f} m²')
    ax2.set_xlabel('Luas Bangunan (m²)')
    ax2.set_ylabel('Frekuensi')
    ax2.set_title('Distribusi Luas Bangunan Properti DIY')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Simpan dengan resolusi tinggi
    output_file = 'histogram_luas_properti_diy.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"💾 Histogram luas disimpan ke: {output_file}")
    plt.close()

def create_correlation_heatmap(df):
    """
    Membuat heatmap korelasi antar variabel numerik.
    
    Args:
        df (pd.DataFrame): DataFrame input
    """
    print("🔥 Membuat heatmap korelasi...")
    
    # Hitung matriks korelasi
    correlation_matrix = df.corr()
    
    # Buat heatmap
    plt.figure(figsize=(10, 8))
    
    # Membuat custom colormap
    colors = ['#d7191c', '#fdae61', '#ffffbf', '#a6d96a', '#1a9641']
    n_bins = 100
    cmap = sns.blend_palette(colors, n_colors=n_bins, as_cmap=True)
    
    # Buat heatmap dengan anotasi
    sns.heatmap(correlation_matrix, 
                annot=True, 
                cmap=cmap,
                center=0,
                square=True,
                fmt='.3f',
                cbar_kws={'label': 'Koefisien Korelasi'},
                annot_kws={'size': 10})
    
    plt.title('Heatmap Korelasi Variabel Numerik Properti DIY', fontsize=16, pad=20)
    plt.xlabel('Variabel', fontsize=12)
    plt.ylabel('Variabel', fontsize=12)
    
    # Rotasi label untuk keterbacaan yang lebih baik
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    plt.tight_layout()
    
    # Simpan dengan resolusi tinggi
    output_file = 'heatmap_korelasi_properti_diy.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"💾 Heatmap korelasi disimpan ke: {output_file}")
    plt.close()

def print_summary_statistics(stats_df):
    """
    Menampilkan ringkasan statistik deskriptif.
    
    Args:
        stats_df (pd.DataFrame): DataFrame statistik deskriptif
    """
    print("\n" + "="*80)
    print("📋 RINGKASAN STATISTIK DESKRIPTIF PROPERTI DIY")
    print("="*80)
    
    for _, row in stats_df.iterrows():
        var_name = row['Variabel']
        if var_name == 'Harga':
            print(f"\n💰 {var_name}:")
            print(f"   Min     : Rp {row['Min']/1e6:>10.1f} juta")
            print(f"   Q1      : Rp {row['Q1']/1e6:>10.1f} juta") 
            print(f"   Median  : Rp {row['Median']/1e6:>10.1f} juta")
            print(f"   Q3      : Rp {row['Q3']/1e6:>10.1f} juta")
            print(f"   Max     : Rp {row['Max']/1e6:>10.1f} juta")
        elif var_name in ['Luas_Tanah', 'Luas_Bangunan']:
            print(f"\n🏠 {var_name}:")
            print(f"   Min     : {row['Min']:>10.1f} m²")
            print(f"   Q1      : {row['Q1']:>10.1f} m²")
            print(f"   Median  : {row['Median']:>10.1f} m²")
            print(f"   Q3      : {row['Q3']:>10.1f} m²")
            print(f"   Max     : {row['Max']:>10.1f} m²")
        else:
            print(f"\n🔢 {var_name}:")
            print(f"   Min     : {row['Min']:>10.0f}")
            print(f"   Q1      : {row['Q1']:>10.1f}")
            print(f"   Median  : {row['Median']:>10.1f}")
            print(f"   Q3      : {row['Q3']:>10.1f}")
            print(f"   Max     : {row['Max']:>10.0f}")

def main():
    """
    Fungsi utama untuk menjalankan seluruh analisis eksplorasi data.
    """
    print("🏡 EKSPLORASI DATA PROPERTI DIY")
    print("="*50)
    
    try:
        # 1. Muat dan persiapkan data
        df = load_and_prepare_data()
        
        # 2. Hitung statistik deskriptif
        stats_df = calculate_descriptive_statistics(df)
        
        # 3. Buat visualisasi
        create_price_histogram(df)
        create_area_histograms(df)
        create_correlation_heatmap(df)
        
        # 4. Tampilkan ringkasan
        print_summary_statistics(stats_df)
        
        print("\n" + "="*80)
        print("✅ ANALISIS SELESAI! File output yang dihasilkan:")
        print("📄 statistik_deskriptif_properti_diy.csv")
        print("🖼️  histogram_harga_properti_diy.png") 
        print("🖼️  histogram_luas_properti_diy.png")
        print("🖼️  heatmap_korelasi_properti_diy.png")
        print("="*80)
        
    except FileNotFoundError:
        print("❌ Error: File 'databaru.csv' tidak ditemukan!")
        print("   Pastikan file CSV berada di direktori yang sama dengan script ini.")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("   Terjadi kesalahan saat menjalankan analisis.")

if __name__ == "__main__":
    main()