import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

def main():
    data_path = Path(__file__).parent / 'data' / 'datas.csv'
    df = pd.read_csv(data_path, sep=';')
    df['Nilai'] = pd.to_numeric(df['Nilai'], errors='coerce')

    nilai = df['Nilai']
    desc = nilai.describe(percentiles=[0.25, 0.5, 0.75])
    
    # Outlier di boxplot dihitung pakai IQR (Interquartile Range):
    # Q1 (25%) = 72
    # Q3 (75%) = 88
    # IQR = Q3 - Q1 = 16
    # Lalu batasnya dihitung:
    # Lower fence = Q1 − 1.5 × IQR = 72 − 1.5×16 = 48
    # Upper fence = Q3 + 1.5 × IQR = 88 + 1.5×16 = 112
    
    # mode = nilai.mode().tolist()
    # variance = nilai.var(ddof=1)
    # std = nilai.std(ddof=1)
    # skewness = nilai.skew()
    # kurtosis = nilai.kurtosis()
    # missing = nilai.isna().sum()
    # print("Statistik deskriptif untuk kolom 'Nilai':")
    # print(desc.to_string())
    
    plt.figure(figsize=(8, 4))
    plt.boxplot(nilai, vert=False, patch_artist=True,
                boxprops=dict(facecolor='skyblue', color='black'),
                medianprops=dict(color='red', linewidth=2))

    plt.title('Boxplot Nilai Siswa', fontsize=14, weight='bold')
    plt.xlabel('Nilai', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.show()
    
    plt.figure(figsize=(8, 5))
    plt.hist(nilai.dropna(), bins=4, color='skyblue', edgecolor='black')
    plt.title('Distribusi Nilai Siswa', fontsize=14, weight='bold')
    plt.xlabel('Nilai', fontsize=12)
    plt.ylabel('Frekuensi', fontsize=12)
    plt.grid(alpha=0.3, linestyle='--')
    plt.show()
    
    

if __name__ == '__main__':
    main()