# 🚚 Food Delivery Time Prediction with Regression & Dashboard Insights

📊 Prediksi waktu pengiriman makanan menggunakan model regresi, visualisasi eksploratif dengan PowerBI, dan implementasi prediksi real-time dengan Streamlit.

---

## 🚀 Tujuan Project

- Memprediksi estimasi waktu pengiriman makanan berdasarkan faktor-faktor seperti jarak, cuaca, lalu lintas, jenis kendaraan, dan pengalaman kurir.
- Mengidentifikasi variabel yang paling berpengaruh terhadap keterlambatan pengiriman.
- Meningkatkan kepuasan pelanggan melalui prediksi ETA yang lebih akurat.
- Menyediakan dashboard interaktif untuk analisis dan monitoring performa pengiriman.

---

## 🧾 Dataset

**Sumber:** [Food Delivery Time Dataset – Kaggle](https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction)

| Fitur                   | Deskripsi                                           |
|------------------------|-----------------------------------------------------|
| `Delivery_Time_min`    | Target: Waktu pengiriman makanan (menit)           |
| `Distance_km`          | Jarak dari restoran ke pelanggan                    |
| `Preparation_Time_min` | Waktu persiapan makanan oleh restoran              |
| `Courier_Experience_yrs` | Pengalaman kurir (tahun)                        |
| `Weather`              | Kondisi cuaca saat pengiriman                       |
| `Traffic_Level`        | Tingkat kemacetan                                   |
| `Time_of_Day`          | Waktu pengiriman (pagi, siang, malam)              |
| `Vehicle_Type`         | Jenis kendaraan kurir                               |

---

## 👥 Stakeholders

- **Tim Operasional & Logistik:** Optimasi rute dan estimasi waktu.
- **Customer Support:** Memberikan estimasi waktu yang lebih akurat kepada pelanggan.
- **Manajemen:** Monitoring performa pengiriman dan evaluasi.
- **Developer Dashboard:** Mengembangkan fitur prediksi ETA & integrasi sistem.

---

## 🧩 Tools & Tech Stack

| Tool/Library         | Fungsi                                       |
|---------------------|-----------------------------------------------|
| Python              | Data processing, modeling, dan deployment     |
| Pandas, NumPy       | Data wrangling & transformasi                 |
| scikit-learn        | Linear Regression, pipeline, evaluasi         |
| XGBoost, LightGBM, CatBoost | Model alternatif & tuning         |
| Streamlit           | Web app prediksi real-time                    |
| PowerBI             | Visualisasi interaktif & insight              |
| Seaborn, Matplotlib | Visualisasi eksploratif awal                  |

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Menghapus kolom ID yang tidak relevan
- Encoding fitur kategorikal
- Pemetaan ordinal untuk fitur seperti `Traffic_Level` dan `Time_of_Day`
- Pisah data numerik & kategorikal, lalu scaling & encoding

### 2. Modeling
- Split data (train-test: 80:20)
- Melatih 5 model regresi:
  - Linear Regression ✅
  - CatBoost
  - Random Forest
  - XGBoost
  - LightGBM
- Evaluasi metrik: MAE, MSE, RMSE, R²
- Hyperparameter tuning dengan GridSearch/RandomSearch
- **Fokus metrik:** `RMSE` → menunjukkan deviasi prediksi dalam satuan menit

### 3. Deployment & Dashboard
- **PowerBI:** Visualisasi EDA & Insight
- **Streamlit:** Prediksi waktu pengiriman makanan secara real-time
  - Input: Jarak, Waktu Persiapan, Cuaca, Lalu Lintas, Kendaraan, dll

---

## 📈 Model Evaluation

**📌 Fokus Metrik:** `RMSE (Root Mean Squared Error)`  
Alasan:
- Target dalam satuan menit → RMSE lebih relevan secara bisnis
- Sensitif terhadap outlier → cocok untuk estimasi keterlambatan parah
- Interpretasi lebih mudah oleh tim non-teknis

| Model              | MAE  | MSE   | RMSE | R²   |
|-------------------|------|-------|------|------|
| Linear Regression | 5.90 | 77.91 | 8.83 | 0.83 |
| CatBoost          | 6.36 | 85.09 | 9.22 | 0.81 |
| Random Forest     | 6.87 | 93.83 | 9.69 | 0.79 |
| LightGBM          | 6.65 | 87.10 | 9.33 | 0.80 |
| XGBoost           | 6.49 | 86.45 | 9.29 | 0.80 |

✅ **Model Terbaik: Linear Regression**
- RMSE terendah → Prediksi paling akurat
- Model sederhana dan explainable → Cocok untuk bisnis
- Mudah diintegrasikan ke sistem Streamlit

---

## 💡 Key Insights

- 🚦 Cuaca buruk + kemacetan ekstrem → waktu pengiriman melonjak
- 🚗 Kendaraan `Car` lebih cepat dibanding `Bike`/`Scooter` di kondisi macet
- 📅 `Night` + `Stormy` = kombinasi waktu terburuk
- 🔧 Kurir berpengalaman → pengiriman lebih cepat
- 📏 `Jarak` & `Waktu Persiapan` → dua faktor paling berpengaruh

---

## 🖥️ Dashboard & App

- 🔗 **Prediksi Real-time (Streamlit):** [streamlit.app](https://food-delivery-time-prediction-thxplay.streamlit.app/)
- 📊 **PowerBI Insight Dashboard:** [Google Drive](https://drive.google.com/drive/folders/15ZU_Q2K4hdkh1rgdlx-B9rDeQ1kD-VRS?usp=sharing)
- 📈 **Full Discussion (LinkedIn)** [LinkedIn](https://www.linkedin.com/posts/okaviantama-karunia-haris_food-delivery-time-prediction-data-analyst-activity-7354561962376122369-Rft1?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAADd-fr0BN0o1qX9eCqvh0HMGtY3QNYyyb7A)

---

## ✅ Business Impact

- Meningkatkan estimasi waktu pengiriman → Kepuasan pelanggan naik
- Optimasi rute pengiriman & jam operasional
- Dasar sistem ETA di aplikasi food delivery
- Insight strategis untuk manajemen operasional

---

## 📂 Folder Structure
📄 main.py # Aplikasi utama Streamlit  <br>
📄 README.md # Dokumentasi proyek   <br>
📄 requirements.txt # Daftar library yang dibutuhkan <br>
📁 dataset/ <br>
├── 📄 Food_Delivery_Times.csv <br>
📁 images/ # Gambar visualisasi & dashboard  <br>
📁 model/ <br>
├── 📄 linear_pipeline.pkl # Model Linear Regression terbaik <br>
├── 📄 insight.py # Halaman insight visual <br>
├── 📄 predict.py # Fungsi prediksi model   <br>
├── 📄 aboutme.py # Halaman profil  <br>
📁 .streamlit <br>
└── 📄 config.toml # Konfigurasi tampilan Streamlit <br>
