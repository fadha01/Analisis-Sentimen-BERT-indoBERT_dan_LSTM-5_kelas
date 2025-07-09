import pandas as pd
import streamlit as st
import altair as alt


def Dashboard():
    st.title("Dashboard")

    # Upload file baru
    file = st.file_uploader("Upload file Excel", type="xlsx")

    # Jika file baru diupload, simpan ke session_state
    if file is not None:
        df = pd.read_excel(file)
        st.session_state.df = df
        st.success("File berhasil diupload!")
    elif 'df' in st.session_state:
        df = st.session_state.df
    else:
        st.warning("Silakan upload file Excel terlebih dahulu.")
        return  # Stop di sini kalau belum ada data

    # Tampilkan data
    st.write("### Data:")
    st.dataframe(df)

    st.markdown("---")
    # Tampilkan jumlah kategori jika kolom 'Keterangan' tersedia
    if 'Keterangan' in df.columns:
        kategori = [
            ('Sangat Positif', '😄'),
            ('Positif', '🙂'),
            ('Netral', '😐'),
            ('Negatif', '🙁'),
            ('Sangat Negatif', '😠')
        ]

        counts = df['Keterangan'].value_counts()

        # Buat data untuk tabel jumlah kategori
        data = []
        for k, icon in kategori:
            jumlah = counts.get(k, 0)
            data.append({'Kategori': f"{icon} {k}", 'Jumlah': jumlah})

        hasil = pd.DataFrame(data)

        st.write("### Jumlah Kategori:")
        st.dataframe(hasil)
    else:
        st.warning("Kolom 'Keterangan' tidak ditemukan dalam data.")


def Informasi():
    st.title("Informasi")
    st.header("Apa yang dimaksud dengan Analisis Sentimen?")
    st.write("Analisis sentimen adalah proses menganalisis teks digital untuk menentukan apakah nada emosional pesan tersebut positif, negatif, atau netral. Saat ini, perusahaan memiliki data teks dalam volume besar seperti email, transkrip obrolan dukungan pelanggan, komentar media sosial, dan ulasan. Alat analisis sentimen dapat memindai teks ini untuk secara otomatis menentukan sikap penulis terhadap suatu topik. Perusahaan menggunakan wawasan dari analisis sentimen untuk meningkatkan mutu layanan pelanggan dan meningkatkan reputasi merek. ")
    st.header("Mengapa analisis sentimen penting?")
    st.write("Analisis sentimen, yang juga dikenal sebagai penambangan opini, adalah alat kecerdasan bisnis penting yang membantu perusahaan meningkatkan produk dan layanan mereka.")
    st.write("- Memberikan wawasan yang objektif")
    st.write("- Membangun produk dan layanan yang lebih baik")
    st.write("- Menganalisis dalam skala besar")
    st.write("- Hasil waktu nyata")
    st.header("Bagaimana cara kerja analisis sentimen?")
    st.write("Analisis sentimen adalah aplikasi teknologi pemrosesan bahasa alami (NLP) yang melatih perangkat lunak komputer untuk memahami teks dengan cara yang mirip dengan manusia. Analisis biasanya melewati beberapa tahap sebelum memberikan hasil akhir.")
    st.write("- Prapemrosesan")
    st.write("Selama tahap prapemrosesan, analisis sentimen mengidentifikasi kata kunci untuk menyoroti pesan inti teks.")
    st.write("- Analisis kata kunci")
    st.write("Teknologi NLP lebih lanjut menganalisis kata kunci yang diekstraksi dan memberi kata tersebut skor sentimen. Skor sentimen adalah skala pengukuran yang menunjukkan elemen emosional dalam sistem analisis sentimen. Ini memberikan persepsi yang terkait dengan emosi yang diekspresikan dalam teks untuk tujuan analitis. Misalnya, peneliti menggunakan 10 untuk merepresentasikan kepuasan dan 0 untuk kekecewaan saat menganalisis ulasan pelanggan.")
    st.header("Apa saja pendekatan untuk analisis sentimen?")
    st.write("- Berbasis aturan")
    st.write("Pendekatan berbasis aturan mengidentifikasi, menglasifikasikan, dan mencetak kata kunci tertentu berdasarkan leksikon yang telah ditentukan. Leksikon adalah kompilasi kata-kata yang merepresentasikan maksud, emosi, dan suasana hati penulis. Tenaga pemasaran memberi leksikon positif dan negatif skor untuk mencerminkan bobot emosional dari ekspresi yang berbeda. Untuk menentukan apakah sebuah kalimat positif, negatif, atau netral, perangkat lunak memindai kata-kata yang tercantum dalam leksikon dan menjumlahkan skor sentimen. Skor akhir dibandingkan dengan batas-batas sentimen untuk menentukan hubungan emosional secara keseluruhan.")
    st.write("- Pro dan kontra")
    st.write("Analisis sentimen ML menguntungkan karena memproses berbagai informasi teks secara akurat. Selama perangkat lunak menjalani pelatihan dengan contoh yang cukup, analisis sentimen ML dapat memprediksi nada emosional pesan dengan akurat. Namun, model ML yang terlatih dikhususkan untuk satu area bisnis. Artinya, perangkat lunak analisis sentimen yang dilatih dengan data pemasaran tidak dapat digunakan untuk pemantauan media sosial tanpa pelatihan ulang. ")
    st.write("- Machine learning")
    st.write("Pendekatan ini menggunakan teknik machine learning (ML) dan algoritma klasifikasi sentimen, seperti jaringan neural dan deep learning, untuk mengajari perangkat lunak komputer guna mengidentifikasi sentimen emosional dari teks. Proses ini melibatkan pembuatan model analisis sentimen dan melatihnya berulang kali di data yang diketahui sehingga dapat menebak sentimen di data yang tidak diketahui dengan akurasi tinggi. ")
    st.write("- Pelatihan")
    st.write("Selama pelatihan, ilmuwan data menggunakan set data analisis sentimen yang berisi banyak contoh. Perangkat lunak ML menggunakan set data sebagai input dan melatih dirinya sendiri untuk mencapai kesimpulan yang telah ditentukan. Dengan melatih banyak contoh beragam, perangkat lunak akan mendiferensiasi dan menentukan bagaimana susunan kata berbeda akan memengaruhi skor sentimen akhir.")
    

def Visualisasi():
    st.title("Visualisasi")
    if 'df' in st.session_state:
        df = st.session_state.df

        st.write("### Grafik Sentimen per Tahun (Garis)")
        if 'Keterangan' in df.columns and 'Tahun' in df.columns:
            # Hitung jumlah tiap kategori per tahun
            summary = df.groupby(['Tahun', 'Keterangan']).size().reset_index(name='Jumlah')

            # Urutan kategori
            kategori_order = ['Sangat Negatif', 'Negatif', 'Netral', 'Positif', 'Sangat Positif']

            # Grafik Garis
            chart_line = alt.Chart(summary).mark_line(point=True).encode(
                x=alt.X('Tahun:O', title='Tahun'),
                y=alt.Y('Jumlah:Q', title='Jumlah'),
                color=alt.Color('Keterangan:N', scale=alt.Scale(domain=kategori_order, 
                                                               range=['#d73027','#fc8d59','#ffffbf','#91bfdb','#4575b4'])),
                tooltip=['Tahun', 'Keterangan', 'Jumlah']
            ).properties(
                width=700,
                height=400
            ).interactive()

            st.altair_chart(chart_line)

            st.markdown("---")

            # Tabel prevalensi persentase
            st.write("### Prevalensi Sentimen per Tahun (%)")
            pivot = pd.crosstab(df['Tahun'], df['Keterangan'], normalize='index') * 100
            pivot = pivot[kategori_order] if all(k in pivot.columns for k in kategori_order) else pivot
            pivot = pivot.round(2)
            pivot_percent = pivot.astype(str) + '%'
            st.dataframe(pivot)
        else:
            st.warning("Pastikan file memiliki kolom 'Keterangan' dan 'Tahun'.")

        st.markdown("---")

        st.write("### Grafik Barplot Sentimen Berdasarkan Variabel yang Dipilih")

        possible_x = ['Tahun', 'Aplikasi', 'Hastag']
        default_order = ['Sangat Negatif', 'Negatif', 'Netral', 'Positif', 'Sangat Positif']

# Pilihan dari pengguna
        x_axis = st.selectbox("Pilih variabel untuk sumbu X", options=possible_x)

# Pilihan urutan kategori dari pengguna
        kategori_order = st.multiselect(
        "Pilih dan atur urutan kategori sentimen",
            options=default_order,
            default=default_order
    )

# Validasi kolom
    if 'Keterangan' in df.columns and x_axis in df.columns:
    # Hitung jumlah berdasarkan sumbu X dan Keterangan
        summary = df.groupby([x_axis, 'Keterangan']).size().reset_index(name='Jumlah')

    # Filter hanya kategori yang dipilih
        summary = summary[summary['Keterangan'].isin(kategori_order)]

    # Atur urutan kategori berdasarkan input pengguna
        summary['Keterangan'] = pd.Categorical(summary['Keterangan'], categories=kategori_order, ordered=True)

    # Buat grafik batang
        chart_bar = alt.Chart(summary).mark_bar().encode(
            x=alt.X(f'{x_axis}:O', title=x_axis),
            y=alt.Y('Jumlah:Q', title='Jumlah'),
            color=alt.Color('Keterangan:N', scale=alt.Scale(
                domain=kategori_order,
                range=['#d73027', '#fc8d59', '#ffffbf', '#91bfdb', '#4575b4'][:len(kategori_order)]
            )),
            tooltip=[x_axis, 'Keterangan', 'Jumlah']
        ).properties(
            width=700,
            height=400
        ).interactive()

        st.altair_chart(chart_bar)
    else:
        st.warning("Pastikan data memiliki kolom 'Keterangan' dan kolom yang dipilih tersedia.")

page = st.sidebar.selectbox(
    "📌 Pilih Halaman",
    [
        "📊 Dashboard",
        "ℹ️ Informasi",
        "📈 Visualisasi"
    ]
)


if page == "📊 Dashboard":
    Dashboard()
elif page == "ℹ️ Informasi":
    Informasi()
elif page == "📈 Visualisasi":
    Visualisasi()

