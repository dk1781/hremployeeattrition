# Menyelesaikan Permasalahan Perusahaan Human Resource Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut.
### Business Problem

Perusahaan Jaya Jaya Maju menghadapi Tingkat attrition Rate yang tinggi melebihi 10%. Dikhawatirkan jika Faktor yang mempengerahi tingginya attrition rate tersebut tidak ditemukan secepatnya akan berpengaruh terhadap bertambahnya karyawan yang akan keluar dari perusahaan. Maka darri itu diperlukan :

1. Menganalisis fitur/faktor yang apa yang paling mempengaruhi terhadap Attrition rate karyawan
2. Membuat visualisasi yang interaktif dan mudah dipahami oleh HR
3. Membuat model prediksi untuk memprediksi lebih awal apakah karyawan tersebut akan keluar atau tidak


### Project Scope

- Melakukan pembersihan terhadap dataset (missing value, duplikat value, dll)
- Menganalisis Data karyawan, dengan melakukan explorasi (EDA) untuk menemukan hal hal, faktor faktor yang sangat berkaitan dengan penyebab keluarnya karyawan
- Membangun model prediktif menggunakan Machine Learning untuk memprediksi kemungkinan keluarnya karyawan
- Membuat dashboard interaktif yang dapat memudahkan HR untuk memantau kondisi karyawan dan melihat hal hal yang mempengaruhi attrition rate
- Merekomendasikan strategi yang efektif untuk perusahaan berdasarkan temuan yang didapat

### Preparation

**Sumber source:** [Employee data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee 'Dicoding GitHub - Employee data')



**Setup environment:**
1. Prasyarat Tools
   - Google Colab: [Google Colab](https://colab.research.google.com/)
   - Google Looker Studio: [Looker](https://lookerstudio.google.com/u/0/navigation/reporting)
2. Clone Repository\
   Clone Repository 
   ```
   git clone [https://github.com/dk1781/hremployeeattrition]
   cd hremployeeattrition
   ```
3. Setup Google Colab
   ```
   Python 3.11.12
   ```
   Penggunaan Google Colab sudah menyediakan versi Python terbaru secara default, dan library yang akan digunakan sudah kompatibel, sehingga tidak perlu menginstall requirements.txt 

4. Setelah seluruh proses setup selesai, Anda bisa menjalankan skrip utama atau mulai melakukan proses prediksi.
   - Untuk menjalankan analisis utama terdapat pada
     ```
     employeeattrition.ipynb
     ```
   - Untuk mencoba prediksi dapat memasukan data karyawan(ganti data dummy yang adda)
     ```
     python prediction.py
     ```
     File `prediction.py` ini perlu dijalankan dengan mencantumkan sekaligus file `best_model.pkl` dan `scaler.pkl` sebagai alat standarisasi data dummy.


## Business Dashboard

Business Dashboard dirancang untuk membantu HR memantau faktor faktor yang mempengaruhi attrition rate karyawan.
Dashboard ini berisi:
1. Jumlah Karyawan yang ada di Perusahaan

   Dimana Perusahaan Jaya jaya maju memiliki 1058 Karyawan
2. Rata rata Gaji Perbulan Karyawan

   Gaji rata rata Karyawan di perusahaan ini adalah $6,625.95
3. Attrition rate

   Attritionn rate karyawan adalah sebesar 16,9%
4. Attrition by Marital Status

   Karyawan yang berstatus single memiliki angka attrition tertinggi
5. Employee Age Impact to Attrition

   Angka attrition berbanding terbalik dengan usia karyawan karyawan yang lebih tua cenderung tidak meninggalkan perusahaan akan tetapi karyawan yang masih muda terutama pada rentang usia 26-35 memiliki angka attrition tertinggi
6. Total Working Year Impact to Attrition

   Begitu pula halnya dengan Total working Year sama halnya sseperti usia, semakin lamanya pengalman bekerja karyawan semakin rendah angka attrtionnya
7. Attrition By Job Level

   Karyawan dengan job level rendah cenderung keluar dari perusahaan
8. Overtime Impact to Attrition

   Over time atau lembur menjadi hal yang paling berpengaruh pada kemungkinan keluarnya karyawan karena sebanyak 54,7% karywan yang melakukan lembur cenderung meninggalkna perusahaan(attrition)

> Link [Dashboard](https://lookerstudio.google.com/reporting/803a21c7-2489-4dd3-bd17-1c5ff500e1f5)

## Conclusion

Melalui proses analisis terdapat beberapa faktor yang mempengaruhi tingginya attrition rate pada perusahaan jaya jaya maju. Faktor faktor yang sangat mempengaruhi keluarnya karyawan dari perusahaan ialah Lembur, Usia, Lamanya pengalaman bekerja, Tingkat pekerjaan, dan Status pernikahan. Model machine learning yang dibangun dapat meprediksi kemungkinan keluarnya karyawan lewat fitur fitur yang dimasukan dan mendapatkan tingkat akurasi yang baik  sehingga dapat membantu perusahaan untuk melakukan langkah preventif terhadap karyawan yang memiliki chance keluar tinggi. Kemudian dashboard interaktif memberikan visualisasi yang jelas sangat berguna bagi HR untuk memantau kondisi karyawan dan memahami aspek aspek yang perlu diberi perhatian lebih. 

### Recommended Action Items

Berikut beberapa rekomendai yang dapat dilakukan oleh perusahaan untuk mengatasi permasalahan attrition rate:
- Evaluasi mengenai kebijakan Lembur pada perusahaan bisa seperti batasi jam lemburnya atau memberi upah yang lebih banyak
- Memberikan jenajang karir yang jelas terhadap karyawan agar tidak banyak karyawan dilevel bawah yang meninggalkan perusahaan
- Monitor selalu kondisi karyawan dan lakukan langkah preventif jika karyawan itu memiliki chance untuk meninggalkan perusahaan
