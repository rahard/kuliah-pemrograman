# Instagram Crawler

Instagram crawler yang ada di sini akan mengambil sebuah *ID instagram* (IDinstagram)
dan kemudian mencari followernya.
IDinstagram dapat diperoleh dari Queue (**OutQueue**) dan kemudian disetor ke **InQueue**

**instacrawl.py** membutuhkan selenium agar berfungsi. Penggunaannya adalah

python3 instacrawl.py IDtocrawl

**igorchestra.py** merupakan program untuk meng-orkestrakan proses crawling.
Dia membaca berkas yang berisi *instagram ID* yang akan dicrawl (id.txt) dan
kemudian menjalankan **instacrawl.py** dengan ID tersebut. 
Hasilnya disimpan dalam berkas **followers.txt**. 
Jalankan program ini di direktori terpisah (agar tidak menimpa berkas).
