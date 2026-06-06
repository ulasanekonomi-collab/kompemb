import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi Halaman Utama
st.set_page_config(page_title="Konvergen.id - Komunikasi Pembangunan", layout="wide")

st.title("🎯 Konvergen.id")
st.subheader("Platform Konvergensi Alur Komunikasi Kebijakan Pembangunan")
st.write("---")

# Sidebar untuk Navigasi Alur
menu = st.sidebar.radio(
    "Pilih Alur Komunikasi:",
    ["Dasbor Konvergensi", "Alur 1: Pengujian Kebijakan (Top-Down)", "Alur 2: Translasi Suara Publik (Bottom-Up)"]
)

# -------------------------------------------------------------
# MENU 1: DASBOR UTAMA
# -------------------------------------------------------------
if menu == "Dasbor Konvergensi":
    st.header("📈 Dasbor Indeks Konvergensi Pembangunan")
    st.write("Mempertemukan sinyal kebijakan negara dengan ekspektasi perilaku masyarakat.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Indeks Konvergensi", "82%", "+5% minggu ini")
    col2.metric("Potensi Distorsi Publik", "18%", "-2% penurunan risiko")
    col3.metric("Kelompok Paling Rentan", "UMKM & Buruh", "Butuh intervensi")
    
    st.write("### Grafik Pertemuan Ekspektasi vs Realitas Perilaku")
    # Simulasi data konvergensi
    chart_data = pd.DataFrame(
        np.random.randn(20, 2) + [2, 2.1],
        columns=['Sinyal Kebijakan (Pemerintah)', 'Interpretasi Perilaku (Masyarakat)']
    )
    st.line_chart(chart_data)
    st.caption("Jika kedua garis berjalan beriringan (konvergen), risiko kepanikan pasar/panic buying berada di titik terendah.")

# -------------------------------------------------------------
# MENU 2: ALUR 1 (PEMERINTAH -> MASYARAKAT)
# -------------------------------------------------------------
elif menu == "Alur 1: Pengujian Kebijakan (Top-Down)":
    st.header("🏛️ Policy Distortion Checker (Alur Pemerintah ke Masyarakat)")
    st.write("Uji draf narasi kebijakan Anda sebelum dilempar ke ruang digital untuk meminimalkan salah tafsir.")
    
    # Input Draf Teks
    draf_teks = st.text_area(
        "Masukkan Draf Pengumuman Kebijakan (Contoh Kasus Suku Bunga BI):",
        "Inflasi perlu dikendalikan dan konsumsi perlu dijaga karena ketidakpastian global meningkat. Oleh karena itu, Bank Indonesia menyesuaikan suku bunga."
    )
    
    if st.button("Uji Potensi Distorsi Narasi"):
        st.write("### 🔍 Hasil Analisis Risiko Komunikasi")
        
        # Simulasi deteksi parameter dari gambar blueprint
        st.warning("**⚠️ Temuan Risiko Tinggi:** Penggunaan kata 'Ketidakpastian Meningkat' berpotensi diterjemahkan publik sebagai 'Ekonomi Sedang Krisis! Tarik dana sekarang!'")
        
        st.write("### 📢 Rekomendasi Strategi Saluran & Segmentasi Pesan:")
        
        # Tabel Rekomendasi Segmentasi berdasarkan image_2bfca5.jpg
        data_rekomendasi = {
            "Kelompok Sasaran": ["Kelas Menengah", "Pelaku UMKM", "Buruh / Pekerja"],
            "Potensi Respon Psikologis": ["Menahan konsumsi & pindah ke instrumen aman", "Sakit kepala karena biaya pinjaman naik", "Mengurangi pengeluaran harian secara drastis"],
            "Solusi Narasi Pendamping": ["Edukasi instrumen investasi obligasi negara", "Sinyal program relaksasi modal atau subsidi bunga", "Komunikasi bantuan sosial bantalan ekonomi"]
        }
        df_rekomendasi = pd.DataFrame(data_rekomendasi)
        st.table(df_rekomendasi)

# -------------------------------------------------------------
# MENU 3: ALUR 2 (MASYARAKAT -> PEMERINTAH)
# -------------------------------------------------------------
elif menu == "Alur 2: Translasi Suara Publik (Bottom-Up)":
    st.header("🗣️ Expression Translator (Alur Masyarakat ke Pemerintah)")
    st.write("Mengubah riuh ekspresi emosional dan keluhan publik di media sosial menjadi indikator kebijakan yang terstruktur.")
    
    st.write("### Simulasi Aliran Data Keluhan Publik (Masyarakat Miskin & UMKM)")
    
    # Contoh data keluhan mentah
    keluhan_mentah = [
        "Aduh pusing jualan makin sepi, modal minjem di bank bunganya malah naik lagi. Gimana mau muter uang!",
        "Nyari kerjaan susah, mana harga-harga sembako merangkak naik terus gara-gara isu ekonomi sulit.",
        "Uang belanja makin gak cukup, terpaksa kurangi jajan anak demi bisa bayar angsuran."
    ]
    
    for i, teks in enumerate(keluhan_mentah, 1):
        st.text_area(f"Keluhan Publik {i} (Sumber: Media Sosial/Forum)", teks, height=70)
        
    if st.button("Terjemahkan ke Bahasa Indikator Pembangunan"):
        st.write("### 📊 Hasil Translasi untuk Pembuat Kebijakan (Eksekutif & Legislatif)")
        
        # Hasil konversi ke indikator makro
        st.info("**Indikator 1 (Sektor UMKM):** Tekanan pada Margin Keuntungan akibat kontraksi kredit. Rekomendasi: Intervensi kebijakan kredit mikro.")
        st.info("**Indikator 2 (Sektor Ketenagakerjaan):** Penurunan daya beli riil masyarakat rentan. Rekomendasi: Akselerasi jaring pengaman sosial/bansos.")
        
        st.success("Data berhasil dirapikan! Siap dikirim sebagai umpan balik otomatis ke sistem perencanaan Bank Indonesia dan Kemenkeu.")
