import streamlit as st
import pandas as pd
import os
import numpy as np
from scipy import stats
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from model import predict, insight, aboutme
import io

import warnings
warnings.filterwarnings("ignore", message=".*use_column_width.*")

#######################
# ⚙️ Page Configuration
st.set_page_config(
    page_title="Food Delivery Time Prediction",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title('⚙️ Menu Utama')
page = st.sidebar.radio('Pilih halaman:', ['Data Understanding', 'Predict', 'Insight', 'About Me'])

if page == 'Data Understanding':

    pd.set_option('display.max_rows', None)  # Menampilkan semua baris
    pd.set_option('display.max_columns', None)  # Jika ada banyak kolom

    st.markdown("<h1 style='text-align: center;'>Food Delivery Time Prediction</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])  # kolom tengah lebih lebar
    with col2:
        st.image("images/food-delivery.jpg", use_container_width=True)

    st.markdown("<h2 style='text-align: left;'>Latar Belakang Masalah (Problem Background):</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>Perusahaan layanan pengiriman makanan menghadapi tantangan besar dalam menyediakan estimasi waktu pengiriman yang akurat kepada pelanggan. Ketidakakuratan estimasi waktu pengiriman dapat menyebabkan:</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Ketidakpuasan Pelanggan</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Penurunan loyalitas pengguna</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Masalah efisiensi logistik & manajemen kurir</div>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: left;'>Tujuan Project (Project Objective)</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>Membangun model machine learning untuk memprediksi waktu pengiriman (Delivery_Time_min) berdasarkan fitur-fitur seperti:</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Jarak antara restoran dan pelanggan</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Kondisi cuaca</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Tingkat kemacetan</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Waktu pengiriman (siang, malam, dll.)</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Tipe kendaraan</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Lama waktu persiapan makanan</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'>- Pengalaman kurir</div>", unsafe_allow_html=True)
    st.markdown("---")

    with st.expander("📋 About Dataset"):
        st.write('## Dataset : Food_Delivery_Times.csv')
        st.write('1000 baris : Dengan jumlah 1000 Order_ID')
        st.write('9 kolom : dengan 1 target (Delivery_Time_min)')

        st.markdown("""
        ### 📄 Deskripsi Dataset

        | **Kolom**                | **Deskripsi**                                                                 |
        |--------------------------|-------------------------------------------------------------------------------|
        | `Order_ID`               | ID unik untuk setiap pesanan                                                 |
        | `Distance_km`            | Jarak pengiriman dalam kilometer                                             |
        | `Weather`                | Kondisi cuaca saat pengiriman: *Clear, Rainy, Snowy, Foggy, Windy*            |
        | `Traffic_Level`          | Tingkat kepadatan lalu lintas: *Low, Medium, High*                            |
        | `Time_of_Day`            | Waktu pengiriman: *Morning, Afternoon, Evening, Night*                        |
        | `Vehicle_Type`           | Jenis kendaraan yang digunakan: *Bike, Scooter, Car*                          |
        | `Preparation_Time_min`   | Waktu yang dibutuhkan untuk menyiapkan pesanan (menit)                        |
        | `Courier_Experience_yrs` | Pengalaman kurir dalam tahun                                                  |
        | `Delivery_Time_min`      | Total waktu pengiriman dari awal sampai akhir (menit) — ✅ *Target Variable*  |
        """)

        df_fd = pd.read_csv('dataset/Food_Delivery_Times.csv')
        st.markdown("<h2 style='text-align: justify;'>Datasets</h2>", unsafe_allow_html=True)
        st.dataframe(df_fd)
        if 'Unnamed: 0' in df_fd.columns:
            df_fd.drop(columns='Unnamed: 0', inplace=True)
        info_df = pd.DataFrame({
            "Kolom": df_fd.columns,
            "Non-Null Count": df_fd.notnull().sum().values,
            "Tipe Data": df_fd.dtypes.astype(str).values
            })
        st.subheader("📋 Informasi Struktur Datasets)")
        st.dataframe(info_df)

    with st.expander("📦 Data Preparation"):

        st.subheader("🔍 a. Inspeksi Data")
        st.write(df_fd.describe().T)
        st.write(df_fd.describe(include='object').T)
        st.write("Jumlah nilai unik:")
        st.write(df_fd.nunique())

        st.subheader("❓ b. Missing Value")
        st.write("Jumlah Missing Value Awal:")
        st.write(df_fd.isna().sum())

        for col in ['Weather', 'Traffic_Level', 'Time_of_Day']:
            df_fd[col].fillna(df_fd[col].mode()[0], inplace=True)
        df_fd['Courier_Experience_yrs'].fillna(df_fd['Courier_Experience_yrs'].median(), inplace=True)

        st.success("✅ Missing value sudah diimputasi (modus / median).")
        st.write("Jumlah Missing Value Setelah Imputasi:")
        st.write(df_fd.isna().sum())

        st.subheader("⚠️ c. Cek Anomali Nilai Negatif")
        numerics = df_fd.select_dtypes(include=['int64', 'float64'])
        st.write("Jumlah nilai negatif per kolom:")
        st.write((numerics < 0).sum())

        st.subheader("📌 d. Cek Duplikat")
        prop_unique = len(df_fd.drop_duplicates()) / len(df_fd)
        st.write(f"Proporsi data unik: {prop_unique:.4f}")
        if prop_unique < 1:
            st.error("⚠️ Terdapat duplikat data.")
        else:
            st.success("✅ Tidak ditemukan duplikat.")

        st.subheader("🔍 e. Check Outlier")

        numerical_cols = ['Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs', 'Delivery_Time_min']
        selected_num_col = st.selectbox("Pilih kolom numerik:", numerical_cols)

        def check_plot(df, variable):
            plt.figure(figsize=(16, 4))
            plt.subplot(1, 3, 1)
            sns.histplot(df[variable], bins=30)
            plt.title("Histogram")

            plt.subplot(1, 3, 2)
            stats.probplot(df[variable], dist="norm", plot=plt)
            plt.ylabel("Variable quantiles")

            plt.subplot(1, 3, 3)
            sns.boxplot(y=df[variable])
            plt.title("Boxplot")

            st.pyplot(plt.gcf())
            plt.clf()

        check_plot(df_fd, selected_num_col)

elif page == 'Predict':
    from model import predict
    predict.predict()

elif page == 'Insight':
    from model import insight
    insight.insight()

elif page == 'About Me':
    from model import aboutme
    aboutme.aboutme()