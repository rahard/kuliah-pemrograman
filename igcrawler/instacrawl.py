# python script to find followers of an instagram ID
# EL5203 Pemrograman Lanjut
# Institut Teknologi Bandung (ITB)
# 2020
# Budi Rahardjo (rahard), Luqman Rahardjo (luqmanr), Tyo

import time, sys, selenium
from selenium import webdriver

if len(sys.argv) < 2:
   print("Usage: "+sys.argv[0]+" IDtocheck")
   sys.exit(1)

IDtocheck = sys.argv[1]
# IDtocheck = 'rahard'

# your instagram account
userid=''
password=''

# maximum number of followers to get
# just to be on the safe side, set it, to less than 100
# still find ways to make it better 
MAXfollower = 10
# set to True for verbose messages
DEBUG = True

chrome_options = webdriver.ChromeOptions()
# if you do not want to see what's going on, uncomment this line
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')

#
# program starts here - do not touch, unless you know what you're doing
#
driver = webdriver.Chrome(
   executable_path='chromedriver',
   chrome_options=chrome_options
)

def signin():
   try:
      driver.get('https://www.instagram.com/accounts/login')
      time.sleep(2)
      driver.find_element_by_name("username").send_keys(userid)
      driver.find_element_by_name("password").send_keys(password)
      time.sleep(2)
      driver.find_element_by_class_name("L3NKy").click()
      return userid
   except:
      print("Gagal login")

def cekuser(orang):
   try:
      if (DEBUG):
         print("mencoba masuk ke halaman "+orang)
      driver.get("https://www.instagram.com/"+orang)
      time.sleep(1)
   except:
      print("Gagal memantau")

def cekfollower():
   # cari tombol follower dulu
   try:
      follButtonXpath = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span'
      follower_button = driver.find_element_by_xpath(follButtonXpath)
      printfoll = follower_button.get_attribute('title')
   except:
      print("ERROR: Tidak menemukan follower button")
      pass
   
   if (DEBUG):
      print("DEBUG: Follower button found")
   #print("DEBUG: Jumlah follower "+follower_button.text)
   #jumlah_follower = follower_button.text
   follower_button.click()
   followerValue = printfoll.split()
   jmlfollower = followerValue[0]
   if (DEBUG):
      print("DEBUG: followerValue[0] "+jmlfollower)
   return jmlfollower


if (DEBUG):
   print("Crawling "+IDtocheck)
   print("Logging in")
signin()

# cari user - tunggu sebentar
if (DEBUG):
   print("Tunggu sebentar")
time.sleep(2)
cekuser(IDtocheck)

# cek dulu kalau berhasil
# cari tombol follower
stringnfollower = cekfollower()
# konversikan ke integer, tapi string ada koma untuk ribuan
# jadi harus dihapuskan dulu. misal 2,650 menjadi 2650
nfollower = int(stringnfollower.replace(',','')) 

# mendaftar 100 follower pertama
jumlah = MAXfollower
if (jumlah > nfollower):
   jumlah = nfollower
if (DEBUG):
   print("Akan mencari follower sebanyak "+str(jumlah))

# cari window baru yang dibuat instagram, yang berisi daftar followers
time.sleep(1)
try:
   fBody = driver.find_element_by_xpath("//div[@class='isgrP']")
except:
   print("tidak menemukan fbody")
   exit()

# scroll di window baru tersebut untuk mendapatkan daftar nama followers
scroll = 0
while scroll < jumlah:
   scroll += 1
   driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
   time.sleep(0.1)

# looping ambil nama follower
pathawal = '/html/body/div[4]/div/div[2]/ul/div/li['
pathakhir =']/div/div[1]/div[2]/div[1]/a'
for n in range(jumlah):
   x = n+1
   path = pathawal+str(x)+pathakhir
   #print(path)
   try:
      follower_name = driver.find_element_by_xpath(path)
      nama = (follower_name.text)
      print(x, nama)
   except:
      print("tidak menemukan follower name")

if (DEBUG):
   print("Selesai")
