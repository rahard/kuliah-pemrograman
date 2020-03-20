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
