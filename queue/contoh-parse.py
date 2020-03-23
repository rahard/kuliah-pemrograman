import sys

# check argument to program
name = sys.argv[0]
numberargs = len(sys.argv)
if (numberargs) < 4:
   print("Usage: " + name + "IDpenyetor root follower")
   exit(1)

# get data
root = sys.argv[2]
follower = sys.argv[3]
print("Kirim " + root + " " + follower)
