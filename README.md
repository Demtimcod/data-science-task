# Data Science

Dokumentasi ini menjelaskan langkah-langkah membuat lingkungan kerja (virtual environment) menggunakan **[uv](https://github.com/astral-sh/uv)**, lalu memasang **Jupyter** dan **Streamlit** untuk pengembangan data science.

---

install lewat curl

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

atau

pip

```bash
pip install uv
```

untuk membuat venv nya

```sh
uv venv [option] [path]
```

setalah itu untuk install jupiter lab menggunakan uv

```bash
 uv run --with jupyter jupyter lab
```

jika kalian tidak pernah install jupiter lab ini akan meninstall package yang di butuhkan oleh jupiter

untuk menjalankan nya tinggal perintah

```bash
jupiter lab
```

## Statistik Deskriptif

- [Data Science](#data-science)
  - [Statistik Deskriptif](#statistik-deskriptif)
    - [Count (Jumlah)](#count-jumlah)
    - [Mean (Rata-Rata)](#mean-rata-rata)
    - [Std (Standard Deviation / Simpangan Baku)](#std-standard-deviation--simpangan-baku)
    - [Min (Minimum)](#min-minimum)
    - [25% (Kuartil Pertama / Q1)](#25-kuartil-pertama--q1)
    - [50% (Kuartil Kedua / Q2 atau Median)](#50-kuartil-kedua--q2-atau-median)
    - [75% (Kuartil Ketiga / Q3)](#75-kuartil-ketiga--q3)
    - [Max (Maximum)](#max-maximum)

### Count (Jumlah)

**Apa itu**: Jumlah total observasi atau data points dalam dataset Anda.

**Fungsinya**: Untuk memastikan tidak ada data yang missing (hilang) dan memahami ukuran sampel. Jika `count` lebih kecil dari jumlah baris yang diharapkan, berarti ada nilai yang kosong (NaN).

**Example**:

> Jika Anda memiliki data nilai 10 orang, maka count-nya adalah 10.

### Mean (Rata-Rata)

**Apa itu**: Nilai rata-rata dari seluruh data. Diperoleh dengan menjumlahkan semua nilai, lalu dibagi dengan jumlah data (`count`).

**Fungsinya**: Memberikan gambaran tentang pusat atau nilai tipikal dari data. Sangat sensitif terhadap outlier (nilai ekstrem).

**Rumus mean**:

```math
Mean = (jumlah_semua_nilai) / (Count)
```

> Count = total nilainya

**Example**:

> Mean dari [2, 4, 6] adalah (2+4+6)/3 = 4.

### Std (Standard Deviation / Simpangan Baku)

**Apa itu**: Ukuran seberapa tersebar atau bervariasinya data di sekitar nilai mean.

**Fungsinya**:

- Std kecil: Data mengelompok rapat di sekitar mean (konsisten).

- Std besar: Data sangat tersebar dan variatif.

**Example**:

> Jika rata-rata tinggi badan adalah 170 cm dengan std 5 cm, maka sebagian besar data berada di sekitar 165 cm - 175 cm.

### Min (Minimum)

**Apa itu**: Nilai terkecil dalam kumpulan data.

**Fungsinya**: Mengetahui batas bawah dari data dan membantu mengidentifikasi kemungkinan kesalahan input (jika nilainya tidak masuk akal).

### 25% (Kuartil Pertama / Q1)

**Apa itu**: Nilai yang memisahkan 25% data terendah dari sisa 75% data. Dengan kata lain, 25% data memiliki nilai di bawah atau sama dengan Q1.

**Fungsinya**: Sebagai batas bawah dari Interquartile Range (IQR) dan untuk mengidentifikasi outlier ringan.

### 50% (Kuartil Kedua / Q2 atau Median)

**Apa itu**: Nilai tengah dari data ketika data diurutkan dari yang terkecil hingga terbesar. Membagi data menjadi dua bagian yang sama.

**Fungsinya**: Lebih robust (kuat) dibandingkan mean dalam menggambarkan pusat data karena tidak terpengaruh oleh outlier.

**Example**:

> Median dari [1, 3, 100] adalah 3, sedangkan mean-nya adalah 34.7. Median lebih mewakili "nilai tipikal" dalam kasus ini.

### 75% (Kuartil Ketiga / Q3)

**Apa itu**: Nilai yang memisahkan 75% data terendah dari 25% data tertinggi. Dengan kata lain, 75% data memiliki nilai di bawah atau sama dengan Q3.

**Fungsinya**: Sebagai batas atas dari Interquartile Range (IQR).

### Max (Maximum)

**Apa itu**: Nilai terbesar dalam kumpulan data.

**Fungsinya**: Mengetahui batas atas dari data.
