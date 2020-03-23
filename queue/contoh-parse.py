import sys

# check argument to program
name = sys.argv[0]
numberargs = len(sys.argv)
if (numberargs) < 4:
   print("Usage: " + name + " IDpenyetor root follower")
   exit(1)

# get data
IDpenyetor = sys.argv[1]
root = sys.argv[2]
follower = sys.argv[3]
pesan= IDpenyetor + " " + root + " " + follower
print("Kirim " + pesan)

# eksekusi pengiriman
