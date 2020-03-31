# Instagram Crawler

Instagram crawler yang ada di sini akan mengambil sebuah *ID instagram* (IDinstagram)
dan kemudian mencari followernya.
IDinstagram dapat diperoleh dari Queue (**OutQueue**) dan kemudian disetor ke **InQueue**

**instacrawl.py** adalah program yang melakukan crawling ke instagram (untuk mendapatkan data follower).
Program ini membutuhkan selenium agar berfungsi. 
Cek konfigurasi dari program ini (dengan membubuhkan userid dan password instagram anda).
Penggunaannya adalah

python3 instacrawl.py IDtocrawl

Perlu dicatat bahwa ada proses lain yang mendahului ini. Proses tersebut adalah
mendapatkan *IDtocrawl* dari queue (OutQueue). Lihat di direktori queue untuk 
melihat bagaimana caranya untuk mendapatkan IDtocrawl ini.
Pada prinsipnya adalah menjalan program ConsumingOneTime.py

**igorchestra.py** merupakan program untuk meng-orkestrakan proses crawling.
Dia membaca berkas yang berisi *instagram ID* yang akan dicrawl (id.txt) dan
kemudian menjalankan **instacrawl.py** dengan ID tersebut. 
Hasilnya disimpan dalam berkas **followers.txt**. 
Jalankan program ini di direktori terpisah (agar tidak menimpa berkas).
Program dijalankan dengan perintah:

python3 igorchestra.py

**kirimkequeue.py** mengirimkan hasil dari igorchestra di atas ke InQueue
(lihat di direktori queue). Silahkan ubah konfigurasi skrip sebelum dijalankan.
Perintah dijalankan dengan cara:

python3 kirimkequeue.py
