# program untuk mengirimkan hasil crawling yang berisi daftar followers
# (followers.txt) ke Queue
#
# 2020, Budi Rahardjo

# configuration
FOLfile = "followers.txt"
# skrip untuk mengirimkan data ke Queue (lihat di direktori queue)
# Kirim.py ID root follower
KIRIM = "python3 Sending.py"
# this is your ID in the system (for billing purposes, if any)
MYID = "budi"

import sys, os

### Program dimulai di sini

# cari daftar followers
try:
   f = open(FOLfile, "r")
except:
   sys.stderr.write("Tidak dapat membuka " + FOLfile + "\n")
   sys.exit(1)

lines = f.readlines()
f.close()
# iterate over lines, if line is empty then exit
if len(lines) < 1 :
   sys.exit(1)
# make sure the format of the content is: root follower
for line in lines:
   node = line.split()
   if (len(node)<2):
      pass
   else:
      cmd = KIRIM + " " + MYID + " " + node[0] + " " + node[1]
      print(cmd)
      os.system(cmd)
