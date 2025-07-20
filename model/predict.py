import streamlit as st
import pandas as pd
import joblib
import os

def predict():
    # Load pipeline model
    model_path = os.path.join("model", "linear_pipeline.pkl")
    
    try:
        model = joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Gagal memuat model: {e}")
        return

    # Judul
    st.title("🚚 Prediksi Waktu Pengiriman Makanan")
    st.markdown("Masukkan detail order untuk memprediksi estimasi waktu pengiriman makanan (dalam menit).")

    # --- INPUT USER ---
    distance = st.number_input("Jarak Pengiriman (km)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)
    prep_time = st.number_input("Waktu Persiapan (menit)", min_value=0, max_value=180, value=15, step=1)
    courier_exp = st.number_input("Pengalaman Kurir (tahun)", min_value=0, max_value=30, value=2, step=1)

    weather = st.selectbox("Kondisi Cuaca", sorted(['Clear', 'Rainy', 'Foggy', 'Windy']))
    traffic = st.selectbox("Tingkat Kemacetan", sorted(['Low', 'Medium', 'High']))
    time_of_day = st.selectbox("Waktu dalam Sehari", ['Morning', 'Afternoon', 'Evening', 'Night'])
    vehicle = st.selectbox("Jenis Kendaraan", sorted(['Bike', 'Car', 'Scooter']))

    # --- BENTUK DATAFRAME ---
    input_data = pd.DataFrame({
        'Distance_km': [distance],
        'Preparation_Time_min': [prep_time],
        'Courier_Experience_yrs': [courier_exp],
        'Weather': [weather],
        'Traffic_Level': [traffic],
        'Time_of_Day': [time_of_day],
        'Vehicle_Type': [vehicle],
    })

    # --- PREDIKSI ---
    if st.button("Prediksi"):
        try:
            prediction = model.predict(input_data)
            st.success(f"⏱️ Estimasi Waktu Pengiriman: **{prediction[0]:.2f} menit**")
        except Exception as e:
            st.error(f"❌ Gagal melakukan prediksi: {e}")