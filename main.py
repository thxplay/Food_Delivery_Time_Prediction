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

    # Fungsi untuk visualisasi outlier
    # def check_plot(df_cs, column):
    #     plt.figure(figsize=(16, 4))

    #     plt.subplot(1, 3, 1)
    #     sns.histplot(df_cs[column], bins=30)
    #     plt.title(f'Histogram - {column}')

    #     plt.subplot(1, 3, 2)
    #     stats.probplot(df_cs[column], dist="norm", plot=plt)
    #     plt.ylabel('Variable quantiles')

    #     plt.subplot(1, 3, 3)
    #     sns.boxplot(y=df_cs[column])
    #     plt.title(f'Boxplot - {column}')

    #     st.pyplot(plt.gcf())
    #     plt.clf()

    # with st.expander("🧹 Data Pre Processing (Python with Google Colab)"):
    #     # 1. Duplikat
    #     st.subheader("✅ Pengecekan Duplikat")
    #     st.markdown("<div style='text-align: justify;'>Tidak ditemukan duplikat.</div>", unsafe_allow_html=True)
    #     pilih1 = st.radio("Tampilkan pengecekan?", ["Tidak", "Pengecekan"], key="cek_duplikat")
    #     if pilih1 == "Pengecekan":
    #         prop_unique = len(df.drop_duplicates()) / len(df)
    #         st.write(f"Proporsi data unik: `{prop_unique:.4f}`")
    #         if prop_unique < 1:
    #             st.error("⚠️ Ditemukan duplikat dalam data.")
    #         else:
    #             st.success("✅ Tidak ditemukan duplikat dalam data.")

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

        # # 2. Tipe Data
        # st.subheader("⚠️ Pengecekan Tipe Data")
        # st.markdown("<div style='text-align: justify;'>Merubah format kolom “Invoice Date” ( Object → Datetime )</div>", unsafe_allow_html=True)
        # pilih2 = st.radio("Tampilkan setelah sudah diubah?", ["Tidak", "Pengecekan"], key="cek_tipe")
        # if pilih2 == "Pengecekan":
        #     buffer = io.StringIO()
        #     df.info(buf=buffer)
        #     info_str = buffer.getvalue()
        #     st.text(info_str)

        # st.markdown("---")

        # # 3. Missing Value
        # st.subheader("✅ Pengecekan Missing Value")
        # st.markdown("<div style='text-align: justify;'>Tidak ditemukan missing value.</div>", unsafe_allow_html=True)
        # pilih3 = st.radio("Tampilkan pengecekan?", ["Tidak", "Pengecekan"], key="cek_missing")
        # if pilih3 == "Pengecekan":
        #     st.dataframe(df.isna().sum())

        # st.markdown("---")

        # # 4. Outlier
        # st.subheader("⚠️ Pengecekan Outlier")
        # st.markdown("<div style='text-align: justify;'>Terdapat Outlier pada kolom “Price” dimana harga pada kolom “Price” masih masuk akal dan banyak sehingga outlier tidak dihapus</div>", unsafe_allow_html=True)
        # pilih4 = st.radio("Tampilkan pengecekan?", ["Tidak", "Pengecekan"], key="cek_outlier")
        # if pilih4 == "Pengecekan":
        #     st.write("🔍 Cek Plot Kolom `age`")
        #     check_plot(df, 'age')

        #     st.write("🔍 Cek Plot Kolom `quantity`")
        #     check_plot(df, 'quantity')

        #     st.write("🔍 Cek Plot Kolom `price`")
        #     check_plot(df, 'price')

        #     st.write("📌 Nilai unik di kolom `price` (diurutkan):")
        #     uq_price = sorted(df['price'].unique())
        #     st.write(uq_price)

        #     # Tampilkan transaksi tertentu (bukti outlier logis)
        #     for target_price in [5250.0, 4200.0, 3150.0, 3000.85]:
        #         st.write(f"📄 Transaksi dengan harga {target_price}:")
        #         df_cs_filter = df[df['price'] == target_price]
        #         st.dataframe(df_cs_filter)
        
    # with st.expander("🎯 Tujuan Proyek & Masalah Bisnis"):
    #     st.markdown("### 🎯 Tujuan Proyek")
    #     st.markdown("""
    #     - Mengelompokkan pelanggan berdasarkan **RFM** waktu terakhir pembelian **(Recency)**, frekuensi transaksi (**Frequency)**, dan nilai pembelian **(Monetary)**.  
    #     - Mengidentifikasi pelanggan bernilai tinggi dan berisiko hilang untuk menyusun strategi yang lebih tepat.  
    #     - Memberikan insight untuk pengambilan keputusan pemasaran berbasis data.
    #     """)

    #     st.markdown("### 👥 Pihak yang Diuntungkan")
    #     st.markdown("""
    #     - **Tim Marketing**: Menargetkan kampanye promosi ke segmen dengan potensi tertinggi.  
    #     - **Manajemen Pusat Perbelanjaan**: Menentukan strategi retensi pelanggan dan loyalty program.  
    #     - **Retailer**: Lebih memahami pelanggan aktif vs. pasif untuk penawaran yang disesuaikan.
    #     """)

    #     st.markdown("### ❓ Masalah Bisnis")
    #     st.markdown("""
    #     **Bagaimana cara mengelompokkan pelanggan berdasarkan perilaku belanja mereka agar strategi pemasaran lebih terarah dan berdampak?**  

    #     Saat ini, semua pelanggan cenderung diperlakukan sama, padahal kontribusinya berbeda-beda. Tanpa pemetaan pelanggan yang jelas, promosi bisa tidak efektif dan menyebabkan biaya tinggi.
    #     """)

    #     st.markdown("### ✅ Manfaat dari Solusi Ini:")
    #     st.markdown("""
    #     - Meningkatkan efisiensi anggaran promosi.  
    #     - Fokus pada retensi pelanggan bernilai tinggi.  
    #     - Mengurangi churn dari pelanggan yang berisiko hilang.  
    #     - Mendukung strategi bisnis yang lebih terfokus dan berbasis data.
    #     """)

    # with st.expander("🧠 Customer Segmentation - RFM Score"):
    #     st.markdown("## 📊 Customer Segmentation")
    #     st.markdown("Perhitungan RFM ( **R**ecency, **F**requency, **M**onetary ) Score")
    #     row1, row2, row3 = st.columns([2, 1, 2])

    #     with row1:
    #         st.image("images/rfm1.png", caption="Total Score Formula RFM", use_container_width=True)
    #     with row2:
    #         st.image("images/rfm2.png", caption="Distribution RFM Score", use_container_width=True)
    #     with row3:
    #         st.image("images/rfm3.png", caption="Customer Segmentation Strategy & Action", use_container_width=True)

    #     st.markdown("---")

    #     st.markdown("## 📐 Pembagian RFM (Recency, Frequency, Monetary)")
    #     left_col, right_col = st.columns([2, 2])

    #     with left_col:
    #         st.markdown("""
    #         - **Q1 (25%)**: Batas bawah — 25% data di bawah nilai ini  
    #         - **Q2 (50%)**: Median — nilai tengah dari seluruh data  
    #         - **Q3 (75%)**: Batas atas — 75% data di bawah nilai ini
    #         """)

    #     with right_col:
    #         st.image("images/rfm4.png", caption="RFM Quartile", use_container_width=True)

    # with st.expander("📈 Exploratory Data Analysis (EDA)"):
    # st.subheader("1. Distribusi Target (Delivery Time)")
    # fig1 = sns.histplot(df_fd['Delivery_Time_min'], kde=True, color='skyblue')
    # st.pyplot(fig1.figure)

    # st.subheader("2. Korelasi Antar Fitur Numerik")
    # fig2 = sns.heatmap(df_fd.corr(numeric_only=True), annot=True, cmap='Blues')
    # st.pyplot(fig2.figure)

    # st.subheader("3. Delivery Time vs Jenis Kendaraan")
    # fig3 = sns.barplot(data=df_fd, x='Vehicle_Type', y='Delivery_Time_min', estimator=np.mean, palette='Set2')
    # st.pyplot(fig3.figure)

    # st.subheader("4. Delivery Time vs Kondisi Cuaca")
    # fig4 = sns.boxplot(data=df_fd, x='Weather', y='Delivery_Time_min', palette='Set2')
    # st.pyplot(fig4.figure)

    # st.subheader("5. Jarak vs Delivery Time")
    # fig5, ax5 = plt.subplots()
    # sns.scatterplot(data=df_fd, x='Distance_km', y='Delivery_Time_min', alpha=0.6, ax=ax5)
    # sns.regplot(data=df_fd, x='Distance_km', y='Delivery_Time_min', scatter=False, color='red', ax=ax5)
    # st.pyplot(fig5)

    # with st.expander("📊 Outlier Detection (Visual)"):
    # numerical_cols = ['Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs', 'Delivery_Time_min']
    # var_selected = st.selectbox("Pilih variabel numerik:", numerical_cols)

    # def check_plot(df_fd, variable):
    #     fig, axs = plt.subplots(1, 3, figsize=(16, 4))
    #     sns.histplot(df_fd[variable], bins=30, ax=axs[0])
    #     axs[0].set_title("Histogram")

    #     stats.probplot(df_fd[variable], dist="norm", plot=axs[1])
    #     axs[1].set_ylabel("Variable quantiles")

    #     sns.boxplot(y=df_fd[variable], ax=axs[2])
    #     axs[2].set_title("Boxplot")
    #     st.pyplot(fig)

    # check_plot(df_fd, var_selected)
    # st.info("💡 Outlier ditampilkan untuk analisis visual, tidak dihapus karena data masih tergolong wajar.")

elif page == 'Predict':
    from model import predict
    predict.predict()

elif page == 'Insight':
    from model import insight
    insight.insight()

elif page == 'About Me':
    from model import aboutme
    aboutme.aboutme()