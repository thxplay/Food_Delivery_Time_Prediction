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
    # 1. User Count by Segment
    with st.expander("### 👥 User Count by Segment"):
        row1, row2, row3 = st.columns([1, 2, 2])
        with row1:
            st.image("images/food-delivery.jpg")
        with row2:
            st.markdown("""
            **Insight**  
            ---
            - Sebagian besar pelanggan ada di segmen **Loyal (26K)**, **Potential Loyalist (22K)**, dan **Cannot Lose Them (20K)** artinya potensi retensi dan konversi sangat besar.  
            - Segmen **Average (12K)** & **About to Sleep (7K)** berisiko churn bila tidak ditindaklanjuti.  
            - Jumlah **Recent Customer (6K)** dan **Champion (7K)** rendah, menunjukkan pentingnya nurturing pelanggan baru dan top spender.

            **Rekomendasi Aksi**  
            ---
            - **Loyal & Cannot Lose Them** : Pertahankan dengan loyalty program dan penawaran eksklusif.  
            - **Potential Loyalist** : Dorong jadi pelanggan setia dengan edukasi dan promo.  
            - **Average & About to Sleep** : Kirim re-engagement campaign dan diskon berkala.  
            - **Recent Customer** : Aktifkan dengan welcome offer dan promo pembelian pertama.  
            - **Champion** : Berikan apresiasi khusus agar makin loyal.
            """)
        with row3:
            st.image("images/food-delivery.jpg")
