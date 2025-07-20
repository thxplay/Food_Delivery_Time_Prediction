import streamlit as st

def insight():
    st.header('📈 Dashboard Visualisasi PowerBI & Insightnya')

    with st.expander("### Dashboard Visualisasi with PowerBI"):
        st.markdown('<div style="text-align: justify;">Dashboard Visualisasi hanya memiliki 1 halaman dan memiliki 7 kategori termasuk home</div>', unsafe_allow_html=True)
        st.image("images/fooddelivery1.png")
        row1, row2, row3 = st.columns([1, 1, 1])
        with row1:
            st.image("images/fooddelivery2.png")
        with row2:
            st.image("images/fooddelivery3.png")
        with row3:
            st.image("images/fooddelivery4.png")
        row1, row2, row3 = st.columns([1, 1, 1])
        with row1:
            st.image("images/fooddelivery5.png")
        with row2:
            st.image("images/fooddelivery6.png")
        with row3:
            st.image("images/fooddelivery7.png")

    with st.expander("### 👥 EDA with PowerBI"):

        row1, row2, row3 = st.columns([2, 2, 1])
        with row1:
            st.image("images/edabi1.jpg")
        with row2:
            st.markdown("""
            Apakah jenis kendaraan memengaruhi waktu pengiriman rata-rata?

            🔍 **Insight:**
            - Mobil (Car) memiliki waktu pengiriman rata-rata tertinggi yaitu 58,20 menit.
            - Sepeda motor (Bike) dan Skuter (Scooter) memiliki waktu yang lebih cepat, masing-masing 56,57 menit dan 56,05 menit.
            - Selisih waktu pengiriman antara mobil dan skuter sekitar 2,15 menit.

            ✅ **Kesimpulan:**
            Jenis kendaraan memengaruhi efisiensi waktu pengiriman. Kendaraan lebih kecil seperti skuter dan motor memiliki waktu pengiriman yang lebih cepat dibandingkan mobil. Hal ini bisa disebabkan karena:
            - Kemampuan manuver lebih baik di lalu lintas padat
            - Lebih mudah parkir di area pengantaran
            - Tidak terlalu terhambat oleh kemacetan

            💡 **Rekomendasi Bisnis:**
            Untuk pengiriman cepat, terutama di wilayah padat atau urban:
            - Prioritaskan penggunaan kendaraan ringan seperti skuter dan motor.
            - Optimalkan rute untuk mobil atau alokasikan mobil untuk pengiriman jarak jauh atau pesanan besar.
            """)
        with row3:
            st.image("images/rd1.jpg")

        row1, row2, row3 = st.columns([1, 2, 2])
        with row1:
            st.image("images/rd2.jpg")
        with row2:
            st.markdown("""
            Level kurir mana yang paling cepat dalam pengiriman?

            🔍 **Insight:**
            - Kurir Expert memiliki waktu pengiriman rata-rata tercepat yaitu 56,04 menit.
            - Diikuti oleh kurir Intermediate dengan waktu 57,55 menit.
            - Kurir Newbie memiliki waktu pengiriman paling lambat yaitu 60,23 menit.

            ✅ **Kesimpulan:**
            Tingkat pengalaman kurir berpengaruh langsung terhadap efisiensi waktu pengiriman.
            - Kurir yang lebih berpengalaman (Expert) menunjukkan performa terbaik dalam hal kecepatan pengiriman.
            - Perbedaan antara kurir Newbie dan Expert cukup signifikan (sekitar 4 menit lebih lambat untuk Newbie), menunjukkan bahwa proses belajar dan pengalaman nyata sangat menentukan efisiensi.

            💡 **Rekomendasi Bisnis:**
            - Menetapkan program pelatihan khusus bagi kurir pemula (Newbie) agar mereka bisa menyamai performa kurir berpengalaman.
            - Mengalokasikan kurir Expert untuk menangani pesanan pada jam sibuk atau area dengan permintaan tinggi.
            - Memonitor kinerja kurir secara berkala dan memberi insentif berbasis performa guna mendorong peningkatan kualitas layanan.
            """)
        with row3:
            st.image("images/edabi2.jpg")

        row1, row2, row3 = st.columns([2, 2, 1])
        with row1:
            st.image("images/edabi3.jpg")
        with row2:
            st.markdown("""
            Apakah jenis kendaraan yang digunakan dalam kondisi cuaca tertentu memengaruhi efisiensi pengiriman?

            🔍 **Insight:**
            - Bike mendominasi pengiriman di berbagai kondisi cuaca, terutama saat cuaca Clear dan Rainy, menunjukkan sepeda motor sering digunakan bahkan dalam kondisi yang kurang ideal.
            - Penggunaan Scooter juga signifikan, tetapi distribusinya lebih merata di berbagai kondisi cuaca.
            - Car paling sedikit digunakan secara relatif, meskipun mungkin lebih stabil dalam kondisi cuaca ekstrem.

            📌 **Kesimpulan:**
            Jenis kendaraan tidak selalu disesuaikan secara optimal dengan kondisi cuaca. Meskipun sepeda motor (Bike) banyak digunakan, mereka lebih rentan terhadap keterlambatan atau risiko keselamatan dalam cuaca buruk seperti hujan, kabut, atau salju.

            💼 **Rekomendasi Bisnis:**
            - Kembangkan kebijakan alokasi kendaraan berdasarkan kondisi cuaca: misalnya, prioritaskan mobil untuk pengiriman saat cuaca buruk (Rainy, Snowy).
            - Evaluasi kembali distribusi kendaraan: pertimbangkan efisiensi, kapasitas, dan keselamatan untuk setiap kondisi cuaca.
            - Latih kurir dalam pengambilan keputusan kendaraan atau pertimbangkan sistem otomatis berbasis cuaca untuk pemilihan jenis kendaraan.
            - Optimalkan rute berdasarkan kombinasi kendaraan dan cuaca, agar waktu pengiriman lebih konsisten.
            """)
        with row3:
            st.image("images/rd3.jpg")

        row1, row2, row3 = st.columns([1, 2, 2])
        with row1:
            st.image("images/rd4.jpg")
        with row2:
            st.markdown("""
            Berapa lama pengiriman paling efisien dilakukan?

            🔍 **Insight:**
            - Pengiriman pada malam hari (Night) memiliki waktu rata-rata tercepat, yaitu 55.21 menit.
            - Pengiriman paling lambat terjadi pada sore hari (Evening) dengan rata-rata 57.48 menit.
            - Terdapat pola efisiensi waktu yang membaik seiring berjalannya hari, dari pagi ke malam.

            📌 **Kesimpulan:**
            - Waktu malam hari adalah periode paling efisien untuk pengiriman, dengan waktu tempuh terpendek dibandingkan periode lainnya.
            - Kemungkinan efisiensi ini disebabkan oleh lalu lintas yang lebih lancar dan volume pesanan yang lebih rendah saat malam.

            💡 **Rekomendasi Bisnis:**
            - Pertimbangkan untuk meningkatkan alokasi pengiriman di malam hari terutama untuk area dengan lalu lintas padat saat siang.
            - Tawarkan insentif khusus (diskon atau bonus poin) bagi pelanggan yang memilih pengiriman malam.
            - Optimalkan jadwal shift kurir untuk memperkuat armada malam, tanpa mengganggu beban kerja siang.
            """)
        with row3:
            st.image("images/edabi4.jpg")

        row1, row2, row3 = st.columns([2, 2, 1])
        with row1:
            st.image("images/edabi5.jpg")
        with row2:
            st.markdown("""
            Apakah lalu lintas padat benar-benar memperlambat proses pengiriman?

            🔍 **Insight:**
            - Semakin tinggi tingkat kemacetan, semakin lama waktu pengiriman:
              - High traffic: 64.81 menit
              - Medium traffic: 56.45 menit
              - Low traffic: 52.89 menit
            - Selisih antara kondisi High dan Low Traffic mencapai hampir 12 menit, menunjukkan dampak besar kemacetan terhadap efisiensi pengiriman.

            ✅ **Kesimpulan:**
            - Kemacetan lalu lintas secara signifikan memperlambat waktu pengiriman.
            - Kurir membutuhkan waktu pengiriman yang jauh lebih lama saat volume lalu lintas tinggi.

            💡 **Rekomendasi Bisnis:**
            - Optimalkan rute pengiriman menggunakan sistem navigasi berbasis traffic real-time untuk menghindari jalur macet.
            - Jadwalkan pengiriman prioritas pada jam dengan lalu lintas rendah (misalnya malam hari atau pagi sangat awal).
            - Tingkatkan penggunaan kendaraan kecil (scooter atau sepeda motor) yang lebih fleksibel dalam kondisi padat.
            """)
        with row3:
            st.image("images/rd5.jpg")

        row1, row2, row3 = st.columns([1, 2, 2])
        with row1:
            st.image("images/rd6.jpg")
        with row2:
            st.markdown("""
            Bagaimana pengaruh cuaca dan jenis kendaraan terhadap efisiensi waktu pengiriman?

            🔍 **Insight:**
            - Cuaca ekstrem memperlambat pengiriman:
              - Rata-rata waktu pengiriman tertinggi terjadi saat cuaca Snowy (67.11 menit) dan Foggy (59.47 menit).
            - Jenis kendaraan memengaruhi efisiensi:
              - Car (58.20 menit) memiliki waktu pengiriman tertinggi dibanding Bike (56.57) dan Scooter (56.05).
              - Scooter menunjukkan waktu pengiriman terbaik saat cuaca Foggy (54.52) dan Windy (56.43), mengalahkan kendaraan lain.

            📌 **Kesimpulan:**
            Cuaca dan jenis kendaraan memiliki pengaruh signifikan terhadap waktu pengiriman. Mobil cenderung lebih lambat dalam kondisi buruk, sedangkan sepeda motor dan skuter lebih efisien dalam kondisi ringan hingga sedang.

            💡 **Rekomendasi Bisnis:**
            - Gunakan scooter atau bike untuk pengiriman saat cuaca ringan–sedang.
            - Minimalkan penggunaan car saat cuaca bersalju atau berkabut jika memungkinkan.
            - Siapkan protokol pengalihan rute dan penyesuaian waktu estimasi pengiriman saat cuaca buruk.
            - Integrasikan data prakiraan cuaca dengan sistem penjadwalan pengiriman untuk memilih kendaraan paling efisien.
            """)
        with row3:
            st.image("images/edabi6.jpg")

        st.markdown("""
        ### ✅ Kesimpulan Keseluruhan :
        Berdasarkan analisis terhadap berbagai faktor yang memengaruhi waktu pengiriman:
        1. Jenis kendaraan berdampak signifikan terhadap kecepatan pengiriman. Kendaraan seperti Bike dan Scooter memiliki waktu antar rata-rata yang lebih cepat dibandingkan Car.
        2. Level pengalaman kurir berpengaruh langsung terhadap efisiensi.
        3. Faktor cuaca sangat memengaruhi durasi pengiriman.
        4. Efisiensi pengiriman bervariasi tergantung waktu dalam sehari.
        5. Kondisi lalu lintas terbukti menjadi hambatan utama.
        6. Kombinasi antara jenis kendaraan dan cuaca memunculkan tren penting: Bike paling fleksibel dalam segala cuaca, sedangkan Car sangat tidak efisien saat cuaca buruk.

        💡 **Rekomendasi Bisnis :**
        - Optimalkan penggunaan kendaraan ringan seperti Bike atau Scooter.
        - Susun jadwal pengiriman utama di malam hari.
        - Prioritaskan kurir berlevel Senior.
        - Gunakan data cuaca dan lalu lintas real-time sebagai dasar penugasan kendaraan dan kurir.
        - Siapkan SOP dan pelatihan khusus bagi kurir untuk menghadapi cuaca buruk.
        - Pertimbangkan insentif berbasis efisiensi.
        """)

    with st.expander("### 👥 EDA with Python"):
        # 1. Distribusi Delivery Time (Menit)
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.image("images/eda1.jpg")
        with col2:
            st.markdown("""
            **1. Distribusi Delivery Time (Menit)**  
            Bagaimana pola sebaran waktu pengiriman?

            🎯 **Tujuan:**
            - Memahami distribusi target (Delivery_Time_min) sebagai dasar untuk memilih jenis model regresi.
            - Deteksi awal adanya outlier atau nilai ekstrem.

            🧠 **Insight:**
            - Sebagian besar pengiriman selesai dalam 20–40 menit.
            - Distribusi right-skewed (positif skew): ekor panjang ke kanan.
            - Terlihat ada outlier (waktu pengiriman yang sangat tinggi).

            ✅ **Kesimpulan:**
            Target tidak terdistribusi normal, sehingga:
            - Linear Regression menjadi kurang cocok karena sensitif terhadap outlier dan asumsi normalitas residual.
            - Perlu model yang lebih fleksibel terhadap non-normal data → Tree-based models seperti Random Forest atau XGBoost.
            - Outlier perlu dianalisis lebih lanjut, bukan langsung dihapus, karena bisa mencerminkan kondisi realistis seperti hujan, macet, dll.
            """)
        with col3:
            st.image("images/rdp1.jpg")

        # 2. Korelasi Antar Fitur Numerik
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            st.image("images/rdp2.jpg")
        with col2:
            st.markdown("""
            **2. Korelasi Antar Fitur Numerik**  
            Apakah fitur numerik punya hubungan kuat terhadap Delivery_Time_min?

            🎯 **Tujuan:**
            Mengetahui fitur numerik yang relevan dan signifikan untuk dimasukkan ke model.

            🧠 **Insight:**
            Korelasi positif yang paling kuat:
            - Distance_km → makin jauh, makin lama pengiriman.
            - Preparation_Time_min → semakin lama persiapan, makin lama total pengiriman.
            - Fitur lain seperti Courier_Age dan Courier_Experience_yrs tidak terlalu berpengaruh.

            ✅ **Kesimpulan:**
            - Fokus pada Distance_km dan Preparation_Time_min sebagai prediktor utama.
            - Fitur numerik dengan korelasi rendah bisa tetap digunakan, tapi perlu uji lebih lanjut di modeling.
            """)
        with col3:
            st.image("images/eda2.jpg")

        # 3. Rata-rata Delivery Time per jenis Kendaraan
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.image("images/eda3.jpg")
        with col2:
            st.markdown("""
            **3. Rata-rata Delivery Time per jenis Kendaraan**  
            Apakah jenis kendaraan memengaruhi rata-rata waktu pengiriman?

            🎯 **Tujuan:**
            Mengevaluasi efisiensi kendaraan yang digunakan.

            🧠 **Insight:**
            - Kendaraan seperti Scooter dan Bike lebih cepat dibandingkan Car.
            - Tidak ada perbedaan signifikan antar kendaraan, meskipun mobil sedikit lebih lambat.
            - Variasi standar waktu hampir serupa.

            ✅ **Kesimpulan:**
            - Kendaraan kecil seperti scooter lebih efisien dalam pengiriman makanan.
            - Semua jenis kendaraan memiliki waktu pengiriman yang hampir setara. Mobil cenderung sedikit lebih lambat, mungkin karena keterbatasan manuver di jalan kecil atau lalu lintas padat, tapi perbedaannya kecil.
            """)
        with col3:
            st.image("images/rdp3.jpg")

        # 4. Delivery Time per Weather Condition
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            st.image("images/rdp4.jpg")
        with col2:
            st.markdown("""
            **4. Delivery Time per Weather Condition**  
            Bagaimana pengaruh cuaca terhadap waktu pengiriman?

            🎯 **Tujuan:**
            Memahami bagaimana cuaca memengaruhi durasi pengiriman makanan.

            🧠 **Insight:**
            Rata-rata waktu pengiriman meningkat pada kondisi cuaca buruk.

            ✅ **Kesimpulan:**
            Cuaca buruk seperti salju dan hujan menyebabkan pengiriman lebih lama secara signifikan dibanding cuaca cerah.
            """)
        with col3:
            st.image("images/eda4.jpg")

        # 5. Hubungan Jarak dan Waktu Pengiriman
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.image("images/eda5.jpg")
        with col2:
            st.markdown("""
            **5. Hubungan Jarak dan Waktu Pengiriman**  
            Seberapa besar pengaruh jarak terhadap waktu pengiriman?

            🎯 **Tujuan:**
            Menguji apakah jarak memengaruhi waktu tempuh pengiriman makanan.

            🧠 **Insight:**
            Scatterplot menunjukkan tren naik — makin jauh jaraknya, makin lama waktu pengiriman.

            ✅ **Kesimpulan:**
            Ada korelasi positif antara jarak dan waktu pengiriman. Namun hubungan tidak sepenuhnya linear, karena faktor lain seperti lalu lintas dan cuaca ikut berperan.
            """)
        with col3:
            st.image("images/rdp5.jpg")

        # 6
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            st.image('images/rdp6.jpg')
        with col2:
            st.markdown('''
        **6. Delivery Time berdasarkan Tingkat Lalu Lintas**  
        Apakah waktu pengiriman bervariasi tergantung waktu dalam sehari?

        🎯 **Tujuan:**  
        Menganalisis apakah jam sibuk (pagi, siang, malam) memengaruhi lama pengiriman.

        🧠 **Insight:**  
        Scatterplot menunjukkan tren naik — makin jauh jaraknya, makin lama waktu pengiriman.

        ✅ **Kesimpulan:**  
        Ada korelasi positif antara jarak dan waktu pengiriman. Namun hubungan tidak sepenuhnya linear, karena faktor lain seperti lalu lintas dan cuaca ikut berperan.
        ''')
        with col3:
            st.image('images/eda6.jpg')

        # 7
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.image('images/eda7.jpg')
        with col2:
            st.markdown('''
        **7. Hubungan Jarak dan Waktu Pengiriman**  
        Bagaimana hubungan antara jarak tempuh pengiriman (km) dan waktu pengiriman (menit)?

        🎯 **Tujuan:**  
        Mengetahui apakah terdapat hubungan linier antara jarak yang ditempuh oleh kurir dan durasi pengiriman, guna mengevaluasi efisiensi sistem logistik. Garis tren merah membantu memperjelas pola korelasinya.

        🧠 **Insight:**  
        - Terdapat korelasi positif antara jarak dan waktu pengiriman.  
        - Semakin jauh jaraknya, umumnya waktu pengiriman juga meningkat.  
        - Sebaran data tidak sepenuhnya rapat (terlihat dispersi), artinya ada faktor lain selain jarak yang memengaruhi durasi pengiriman.  
        - Garis tren merah menunjukkan tren linier moderat.

        ✅ **Kesimpulan:**  
        Jarak pengiriman berkontribusi signifikan terhadap waktu tempuh kurir. Namun, karena data menyebar di sekitar garis regresi, faktor lain seperti lalu lintas, jenis kendaraan, dan kondisi cuaca juga memainkan peran penting. Maka, jarak bukan satu-satunya prediktor waktu pengiriman.
        ''')
        with col3:
            st.image('images/rdp7.jpg')

        # 8
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            st.image('images/rdp8.jpg')
        with col2:
            st.markdown('''
        **8. Hubungan Preparation Time dan Delivery Time**  
        Apakah waktu persiapan makanan memengaruhi lama waktu pengiriman ke pelanggan?

        🎯 **Tujuan:**  
        Mengetahui apakah lama waktu persiapan makanan memengaruhi total waktu pengiriman ke pelanggan.

        🧠 **Insight:**  
        - Terdapat korelasi positif ringan: semakin lama persiapan, umumnya pengiriman juga lebih lambat.  
        - Namun, pengaruhnya tidak sebesar faktor jarak.

        ✅ **Kesimpulan:**  
        Waktu persiapan memang berdampak pada waktu pengiriman, tapi bukan satu-satunya penyebab keterlambatan. Perlu dipadukan dengan variabel lain (seperti jarak & lalu lintas) dalam model prediktif.
        ''')
        with col3:
            st.image('images/eda8.jpg')

        # 9
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.image('images/eda9.jpg')
        with col2:
            st.markdown('''
        **9. Pengalaman Kurir per Jenis Kendaraan**  
        Apakah terdapat perbedaan pengalaman kurir (dalam tahun) berdasarkan jenis kendaraan yang mereka gunakan?

        🎯 **Tujuan:**  
        Untuk menganalisis distribusi pengalaman kerja kurir berdasarkan jenis kendaraan yang digunakan — apakah kurir yang mengendarai Scooter, Bike, atau Car memiliki tingkat pengalaman yang berbeda secara signifikan atau tidak.

        🧠 **Insight:**  
        - Median pengalaman kurir Scooter & Bike: 5 tahun, dan Car: 4 tahun.  
        - Rentang pengalaman mirip (0–9 tahun).  
        - Distribusi merata, tanpa outlier ekstrem.

        ✅ **Kesimpulan:**  
        Tidak ada perbedaan signifikan pengalaman antar jenis kendaraan. Artinya, penempatan kurir tidak bergantung pada tingkat pengalaman tertentu.
        ''')
        with col3:
            st.image('images/rdp9.jpg')

        # 10
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            st.image('images/rdp10.jpg')
        with col2:
            st.markdown('''
        **10. Delivery Time per Time of Day**  
        Bagaimana pengaruh waktu dalam sehari (Time of Day) terhadap lamanya waktu pengiriman (Delivery Time)?

        🎯 **Tujuan:**  
        Mengidentifikasi waktu pengiriman paling efisien dan stabil.

        🧠 **Insight:**  
        - Morning & Evening memiliki banyak outlier → pengiriman tidak konsisten.  
        - Afternoon & Night lebih stabil dengan sebaran waktu lebih sempit.  
        - Median waktu pengiriman relatif serupa di semua waktu.

        ✅ **Kesimpulan:**  
        Waktu pengiriman lebih konsisten di siang dan malam. Pengiriman pagi dan sore rentan keterlambatan.
        ''')
        with col3:
            st.image('images/eda10.jpg')