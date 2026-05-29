# Prediksi Harga Mobil

Aplikasi berbasis Machine Learning yang digunakan untuk memprediksi harga mobil berdasarkan spesifikasi kendaraan. Proyek ini dibangun menggunakan Python, Scikit-Learn, dan Streamlit serta dapat diakses secara publik melalui Hugging Face Spaces.

## Demo

Coba aplikasi secara langsung:

**https://huggingface.co/spaces/myu9s/prediksi-harga-mobil**

---

## Deskripsi

Prediksi harga mobil sering digunakan dalam industri otomotif untuk membantu pembeli maupun penjual menentukan estimasi harga kendaraan berdasarkan karakteristik tertentu.

Aplikasi ini menggunakan model Machine Learning yang telah dilatih untuk memprediksi harga mobil berdasarkan beberapa fitur utama kendaraan.

Pengguna cukup memasukkan spesifikasi mobil, kemudian sistem akan memberikan estimasi harga secara otomatis.

---

## Fitur

* Prediksi harga mobil secara instan
* Antarmuka sederhana dan mudah digunakan
* Berbasis Machine Learning
* Dapat diakses melalui browser tanpa instalasi
* Deploy menggunakan Hugging Face Spaces

---

## Parameter Input

Model menggunakan enam fitur sebagai dasar prediksi:

| Fitur           | Deskripsi              |
| --------------- | ---------------------- |
| Engine Size     | Ukuran mesin kendaraan |
| Horsepower      | Tenaga mesin (HP)      |
| Wheelbase       | Jarak sumbu roda       |
| Width           | Lebar kendaraan        |
| Length          | Panjang kendaraan      |
| Fuel Efficiency | Efisiensi bahan bakar  |

---

## Teknologi yang Digunakan

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* Pickle

---

## Struktur Proyek

```text
├── app.py
├── model_mobil.sav
├── requirements.txt
└── README.md
```

---

## Menjalankan Secara Lokal

### 1. Clone Repository

```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

---

## Cara Menggunakan

1. Buka aplikasi melalui browser.
2. Masukkan spesifikasi mobil pada form input.
3. Klik tombol **Prediksi Harga**.
4. Sistem akan menampilkan estimasi harga mobil.

---

## Output

Hasil yang ditampilkan berupa:

```text
Perkiraan Harga Mobil: $XX.XX ribu
```

Nilai tersebut merupakan estimasi harga berdasarkan model machine learning yang telah dilatih sebelumnya.

---

## Lisensi

Proyek ini dibuat untuk tujuan pembelajaran dan pengembangan portofolio.
