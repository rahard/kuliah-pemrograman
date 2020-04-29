# Kuliah Pemrograman EL5203

Oleh: Kerja Kelompok Kuliah Pemrograman EL5203

Repositori ini digunakan untuk berbagi kode, dokumentasi, untuk kuliah EL5203 (STEI, ITB).
Informasi yang lebih rinci ada pada Trello kami.

Sistem yang akan dikembangkan adalah sebuah *instagram crawler* berbasis *queue*.
Sebuah *crawler* akan mengambil data (ID instagram) dari sebuah queue (TO DO list queue,
yang kemungkinan akan disebut **outQueue**).
Crawler akan mengakses akun instagram tersebut dan mengambil data followernya.
(Asumsinya adalah akun instagram tersebut terbuka / dapat dilihat.)
Daftar follower tersebut disetor kembali ke sebuah Queue (disebut **inQueue**).

Di dalamnya ada banyak proses yang akan dijabarkan sebagai berikut.

## InQueue processing
Data di **inQueue** diambil dan dilakukan beberapa hal
- parsing untuk dimasukkan ke database (yang kemungkinan menggunakan Redis)
- untuk setiap follower yang baru diterima, dicek apakah sudah pernah dicrawl
(dengan menguji apakah sudah ada di dalam database), jika belum maka 
follower tersebut dimasukkan ke **outQueue*

Budi Rahardjo (Dosen)

## Crawling/Scrapping
Scraping atau crawling adalah proses mengumpulkan data-data yang dikembalikan oleh instagram.com ke browser dalam format html. Proses ini dilakukan dengan menggunakan Selenium Webdriver.

## Database Processing
Data-data user yang telah melalui proses scrapping disimpan ke dalam suatu database. Seringkali user yang telah diekstrak data followernya masuk kembali ke dalam queue dan berpotensi diekstrak lagi. Jika proses ini terjadi terus-menerus, maka komputasi menjadi tidak efisien. Salah satu proses pada databse ditujukan untuk memfilter data yang masuk agar tidak terjadi duplikasi data. 

## Graph Visualizer
Proses visualisasi bertujuan untuk menunjukan interaksi antar user yang telah diekstrak informasinya followernya. Dari sini didapat visualisasi yang menggambarkan role masing-masing user dalam bentuk graph. Ke depannya, graph yang dihasilkan akan digunakan untuk analisis.

## Requirements
Program ini dibuat dalam bahasa pemrograman Python, sehingga proses instalasi requirement dapat menggunakan perintah 
```
pip install <requirement>
```
Secara arsitektur, program ini menggunakan ```config.ini``` untuk menyimpan informasi-informasi credential yang dibutuhkan oleh masing-masing modul. Untuk itu dibutuhkan library untuk melakukan parsing informasi dari file konfigurasi.

General Requirement
* configparse

Modul Queue Requirement
* request
* pika

Modul Crawler Requirement
* ?

Modul Database Requirement
* redis

Modul Visualization Requirement
* networkx
* matplotlib
