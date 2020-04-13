# membaca config
# April 2020 BR
import sys, configparser
from configparser import ConfigParser

CONF="config.txt"

def bacaconfig():
   # membaca configuration
   config = ConfigParser()
   berhasil = config.read(CONF)
   # jika berhasil, maka berhasil = 1. gagal berasil = 0
   if (len(berhasil)<1):
      sys.stderr.write("Gagal membaca " + CONF + "\n")
      return(-1)

   # mari kita baca sections "queue"
   q_username = config.get('queue','username')
   q_pass = config.get('queue','password')
   q_host = config.get('queue','host')
   q_queue = config.get('queue','queue')
   q_port = config.get('queue','port')
   URL = ''.join(['ampq://',q_username, ':', q_pass, '@', q_host, ':', q_port])
   return(URL)


# mulai program

CLOUDAMPQ_URL=bacaconfig()
print(CLOUDAMPQ_URL)
