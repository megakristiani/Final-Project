# Beer Early BPOM Prediction
By: Mega Kristiani, Purwadhika - Data Science 

Beer merupakan minuman fermentasi tertua dan paling banyak di dunia, namun tingkat konsumsi beer di Indonesia hanya mencapai 0.6 L per tahun (thejakartapost.com, 2018). Meskipun begitu, Indonesia memproduksi beer bermerek (Bintang, Stark Craft Beer, Anker Beer, Bali Hai) dan beer tradisional (Bir Pletok, Bir Kotjok, Bir, Jawa, dan masih banyak lainnya). Untuk dapat meningkatkan angka penjualan beer, dibutuhkan pemasaran yang baik, salah satu syarat beer dapat dipasarkan di Indonesia adalah lolos uji BPOM.

Dalam final project ini, saya akan membuat machine learning yang memprediksi apakah beer dapat lulus uji BPOM atau tidak. Tujuan saya membuat prediksi ini adalah untuk mengurangi angka kerugian yang disebabkan beer tidak lolos uji BPOM, juga membantu pihak perusahaan dan BPOM untuk mengambil keputusan mengenai produk beer yang diuji. 

### 1. Data Sampling

Data yang saya gunakan untuk membuat prediksi BPOM ini terdiri dari 2 dataframe yang saya peroleh dari kaggle (https://www.kaggle.com/jtrofe/beer-recipes), yakni:
1. recipeData (dataframe utama, terdiri dari 23 kolom),
2. styleData (dataframe pendukung untuk mengisi nan value dalam kolom Style, terdiri dari 2 kolom)

Berikut adalah informasi mengenai recipeData:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/inforeal.png)

![alt text](https://github.com/megakristiani/Final-Project/blob/master/dataframe.png)

![alt text](https://github.com/megakristiani/Final-Project/blob/master/dataframe2.png)

### 2. Data Preprocessing

Seperti yang tercantum dalam info diatas, terdapat beberapa Nan Value. Untuk kolom Name, saya melakukan drop pada row yang berisi Nan Value karena hanya berisi 1 dan tidak dapat diprediksi. Untuk kolom Style, saya juga melakukan drop pada row yang berisi Nan Value karena jumlahnya sedikit dan tidak dapat diisi (berdasarkan styleData, styleID yang diperoleh merupakan Nan Value). Untuk kolom BoilGravity saya isi menggunakan nilai hasil Linear Regression karena memiliki korelasi yang tinggi. Untuk kolom MashThickness saya isi menggunakan nilai mean yang dikelompokan berdasarkan StyleID dan SugarScale. Untuk PrimaryTemp saya isi menggunakan nilai mode yang dikelompokan berdasarkan StyleID dan SugarScale karena memiliki interval. Dan untuk kolom PitchRate, PrimingMethod, PrimingAmount, UserId saya drop kolomnya karena berisi Nan Value sebanyak > 50%.

Selain mengisi dan melakukan drop untuk Nan Value, saya juga melakukan drop untuk kolom URL dan BeerID karena kedua kolom ini tidak memiliki nilai yang dapat dijadikan parameter. Dan saya juga menambah 1 kolom berdasarkan ketentuan BPOM (beer dikelompokan berdasarkan warna dan ABV) sebagai berikut:


|  ABV  |  Beer(Color < 24) | Stout(Color >=24) |
| :---: |       :---:       |      :---:        |
|  <2%  |          1        |         4         |
|  2-8% |          2        |         5         |
|  >8%  |          3        |         6         |

### 3. Data Analysis

Untuk mengatasi ketidakseimbangan presentasi data, saya menggunakan teknik SMOTE, yaitu penambahan data baru berdasarkan data minoritas.

Kemudian, saya mencoba beberapa metode klasifikasi, yaitu SVM, Decision Tree, Random Forest, dan XGBoost.

### 3. a. SVM

Saya menggunakan kernel Poly dan degree sebanyak 6 karena data akan diklasifikasikan berdasarkan Color dan ABV menjadi 6 label. Dan berikut hasil yang saya peroleh:

Data Test:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/svm%20test.png)

Data Train:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/svmtrain.png)

Saya memutuskan untuk tidak menggunakan metode ini karena hasil prediksi yang diperoleh kurang baik, terutama dalam nilai presisi dan recall.

### 3. b. Decision Tree

Saya tidak menggunakan parameter khusus, dan berikut hasil yang saya peroleh:

Data Test:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/dtreetest.png)

Data Train:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/dtreetrain.png)

Hasil prediksi yang diperoleh sangat bagus.

### 3. c. Random Forest

Sama seperti Decision Tree, saya tidak menggunakan parameter khusus, dan berikut hasil yang saya peroleh:

Data Test:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/rftest.png)

Data Train:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/rftrain.png)

Hasil prediksinya sangat baik.

### 3. d. XGBoost

Untuk XGBoost saya menggunakan learning_rate 0.01, n_estimators 500, max_depth 5, dan n_jobs -1 agar memperoleh hasil yang maksimal. Berikut hasil yang saya peroleh:

Data Test:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/xgtest.png)

Data Train:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/xgtrain.png)

Hasil yang diperoleh sangat baik.

Dari keempat metode yang saya gunakan, saya memutuskan untuk menggunakan XGBoost karena konsep klasifikasinya mengabungkan beberapa weak learner sehingga saya asumsikan hasil yang diperoleh lebih baik dan akurat.

Dari hasil prediksi dengan metode XGBoost, saya melakukan labeling lagi sebagai berikut:

| Prediksi | Label |      Keterangan      |
|   :---:  | :---: |        :---:         |
|     1    |  Yes  |    Beer lolos BPOM   |
|     2    |  Yes  |    Beer lolos BPOM   |
|     3    |   No  | Beer tidak lolos BPOM|
|     4    |   No  |Stout tidak lolos BPOM|
|     5    |  Yes  |   Stout lolos BPOM   |
|     6    |   No  |Stout tidak lolos BPOM|

Dan berikut persentasinya:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/persen.png)

Hasil yang diperoleh sangat seimbang antara 'Yes' dan 'No'. Hasil ini diperoleh karena pada awal prediksi, saya melakukan SMOTE sehingga datanya seimbang, dan metode prediksi yang saya gunakan mengasilkan prediksi yang sangat baik.

### 4. Dashboard

Saya membuat dashboard yang terdiri dari 5 menu:

1. Home

Home merupakan tampilan awal yang berisi latar belakang.

![alt text](https://github.com/megakristiani/Final-Project/blob/master/home.png)

2. Data Table

Data Table akan menampilkan data setelah data preprocessing, namun belum dilakukan SMOTE.

![alt text](https://github.com/megakristiani/Final-Project/blob/master/data.png)

3. Data Visualization

Data Visualization akan menampilkan visualisasi data seperti heatmap korelasi antar table, 25 beer style terbanyak, persentasi BrewMethod berdasarkan SugarScale, dan masih banyak lainnya.

![alt text](https://github.com/megakristiani/Final-Project/blob/master/datavis.png)

4. Prediction

Prediction akan menampilkan sebuah form yang dapat diisi dengan ABV dan Color, jika di klik, maka akan keluar hasil prediksi lolos atau tidaknya uji BPOM.

![alt text](https://github.com/megakristiani/Final-Project/blob/master/pred.png)

Berikut tampilan hasil prediksinya:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/pred2.png)

5. Boil Gravity

Boil Gravity akan menampilkan form yang dapat diisi dengan beberapa karakteristik beer yang akan memprediksikan berapa nilai BoilGravity beer yang dibuat.

![alt text](https://github.com/megakristiani/Final-Project/blob/master/pred3.png)

Berikut hasil prediksi yang akan ditampilkan:

![alt text](https://github.com/megakristiani/Final-Project/blob/master/pred4.png)
