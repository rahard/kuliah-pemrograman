# orchestrating the instagram crawler process
# run this in a temporary directory
#
# 1. get the ID to crawl from IDfile
# 2. run the idcrawler and send the output to OUTfile
# if success, OUTfile consists of list of followers
#    otherwise it is empty (must test this)
# this process is going to take a while, depending on (2)
# (future: should have indication of progress)

# configuration
IDfile = 'id.txt'
OUTfile = 'followers.txt'
# you may want to give the full path of instacrawl.py
CRAWLER ='python3 instacrawl.py'
DEBUG = True

import sys, os

# Program starts here
# 1. get ID to crawl
try:
   f = open(IDfile, "r")
except:
   sys.stderr.write("Cannot open file " + IDfile + "\n")
   sys.exit(1)
# baca ID, remove \n if any
tempID = f.read()
IDtocrawl = tempID.rstrip()

# check if IDtocrawl "none"
if (IDtocrawl == "none"):
   sys.exit(1)

# crawling ...

crawling = CRAWLER + " " + IDtocrawl + " > " + OUTfile
if (DEBUG):
   print("start crawling: "+crawling)

os.system(crawling)
