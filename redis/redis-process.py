# 1. baca dari InQueue
# 2. parse hasilnya. pilah2 mana ID, root, follower
# 3. cek apakah follower sudah pernah dicrawl (berarti sudah ada di db redis)
# 4. kalau follower belum pernah dicrawl, masukkan follower ke OutQueue

import os, redis

CONSUME = 'ConsumingOneTime.py - >'
TEMPFILE = 'temp-out.txt'
KIRIM = 'Outqueue.py'


CMD = ''.join(["python3 ", CONSUME, " ", TEMPFILE])
# print(CMD)
os.system(CMD)

# check for errors. harusnya outputnya: ID root follower
try:
   f = open(TEMPFILE,"r")
except:
   sys.stderr.write("File tidak ditemukan: " + TEMPFILE + "\n")
   exit(1)

baris = f.read()
kata = baris.split()
if (len(kata) < 3):
   sys.stderr.write("Format salah: " + str(kata))
   exit(1)

ID = kata[0]
root = kata[1]
follower = kata[2]

# cek apakah follower sudah ada di redis
# jika sudah ada ... selesai


# TO DO
# jika belum, maka masukkan follower ke redis dan ke OutQueue
# masukkan ke Redis  r.set(root,follower)
# connect ke redis
# print("Memasukkan ke redis: ", root, follower)
# r.set(root,follower)


# masukkan follower ke OutQueue
print("Akan memproses " + follower)
# masukkan follower ke OutQueue
CMD = ''.join(["python3 ", KIRIM, " ", follower])
print(CMD)
os.system(CMD)
