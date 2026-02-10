# BERT (indobert) dan LSTM-analysis
BERT (Bidirectional Encoder Representations from Transformers) merupakan model pemrosesan bahasa alami berbasis arsitektur Transformer yang mampu memahami konteks kata secara dua arah, yaitu dari kiri dan kanan secara bersamaan. Salah satu variannya, IndoBERT, telah dilatih menggunakan korpus teks berbahasa Indonesia sehingga lebih efektif dalam menangani tugas klasifikasi teks dalam bahasa Indonesia, termasuk analisis sentimen. Model ini memanfaatkan mekanisme self-attention untuk menangkap hubungan antar kata dalam suatu kalimat dan menghasilkan representasi teks yang kaya konteks. Dalam penelitian ini, IndoBERT digunakan untuk menganalisis opini masyarakat mengenai kendaraan listrik yang diperoleh dari media sosial.
Sementara itu, Long Short-Term Memory (LSTM) merupakan pengembangan dari Recurrent Neural Network (RNN) yang dirancang untuk memproses data sekuensial dengan mempertahankan informasi jangka panjang melalui mekanisme memori internal. LSTM memiliki tiga komponen utama berupa forget gate, input gate, dan output gate yang berfungsi mengatur aliran informasi selama proses pembelajaran. Model ini mampu mengenali pola urutan kata dalam teks setelah data diubah menjadi representasi numerik melalui teknik embedding. Pada penelitian ini, LSTM digunakan sebagai model pembanding untuk mengevaluasi performa klasifikasi sentimen terhadap kendaraan listrik.

## 🔍 Tujuan
Merupakan proyek tugas akhir (skripsi) Fadhil Harahap yang berfokus pada analisis sentimen terhadap kendaraan listrik menggunakan pendekatan pembelajaran mesin berbasis BERT (IndoBERT) dan Long Short-Term Memory (LSTM). Penelitian ini bertujuan untuk menganalisis opini masyarakat yang diperoleh dari media sosial serta membandingkan performa kedua model dalam melakukan klasifikasi teks sentimen. Proses penelitian mencakup tahap pengumpulan data, pra-pemrosesan teks, pelatihan model, serta evaluasi kinerja menggunakan metrik pengujian yang relevan. Hasil penelitian diharapkan memberikan gambaran mengenai efektivitas masing-masing metode dalam mengolah bahasa alami berbahasa Indonesia pada konteks analisis sentimen.

## 📊 Dataset
Dataset penelitian diperoleh dari media sosial (X, Instagram, dan TikTok) sebanyak 5.172 komentar, yang selanjutnya diklasifikasikan ke dalam lima kategori sentimen.

<img width="229" height="81" alt="Image" src="https://github.com/user-attachments/assets/f6996953-944e-4fa7-8427-feed42ec6067" />

## 📈 Model
- **IndoBERT** (akurasi: 91%)
- **LSTM** (akurasi: 32%)

## 🚀 Tools
- Python
- Google Colaboratory
- Streamlit

## 🧠 Hasil
  BERT (indoBERT) terletak pada kemampuannya memahami konteks bahasa secara mendalam karena telah dilatih sebelumnya dengan data skala besar dan menggunakan arsitektur transformer yang efektif untuk klasifikasi teks. Sebaliknya, LSTMyang masih berbasis pemrosesan sekuensial dan bergantung pada representasi seperti onehot encoding, lebih terbatas dalam menangkap makna konteks 5 kelas secara menyeluruh dan tidak seibangnya dataset dalam kelas mempengaruhi juga kinerja LSTM. Meski begitu, LSTM masih relevan dalam kasus-kasus tertentu seperti pemrosesan data berurutan yang lebih jelas atau ketika sumber data terbatas.

  Dari hasil tersebut, dapat disimpulkan bahwa metode Bidirectional Encoder
Representations from Transformers (BERT) lebih unggul dibandingkan dengan Long
Short-Term Memory (LSTM) dalam melakukan analisis sentimen terhadap opini
masyarakat mengenai kendaraan listrik di media sosial.

# Tampilan Streamlit

## 📌 Halaman Informasi
<img width="960" height="436" alt="Image" src="https://github.com/user-attachments/assets/111573bf-0706-4c8b-b4f1-d2401c8af288" />

## 📊 Halaman Visualisasi
<img width="960" height="446" alt="Image" src="https://github.com/user-attachments/assets/32da731b-0ede-48e2-b3e5-bf59aad5415e" />

## 📥 Halaman Dashboard Upload File
<img width="960" height="457" alt="Image" src="https://github.com/user-attachments/assets/06f45c7a-8c28-4343-b236-261cff14f14c" />
