import os, time, errno, pickle, stdiomask
from selenium import webdriver
# import selenium
import re
from urllib.request import urlopen
import json
import csv

from selenium import webdriver  
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "2560,1440"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(
    executable_path=CHROMEDRIVER_PATH,
    chrome_options=chrome_options
)  

import getpass

login_id = input('Username Akun Instagram Anda: ')
password = getpass.getpass('Password Akun Instagram Anda: ')

def login_instagram():
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        username_bar = driver.find_element_by_name("username")
        username_bar.send_keys(login_id)

        password_bar = driver.find_element_by_name("password")
        password_bar.send_keys(password)
        time.sleep(2)

        login_button = driver.find_element_by_class_name("L3NKy")
        login_button.click()
    except:
        pass

def followerButton():
    try:
        follButtonXpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        follower_button = driver.find_element_by_xpath(follButtonXpath)
        print("button found")
        print(follower_button.text)
        follower_button.click()
        print("button clicked")
        printfoll = (follower_button.text)
        follValue = printfoll.split()
        print(follValue[0])
        follvalue = follValue[0]
        return follvalue
    except:
        pass

login_instagram()
time.sleep(5)
account = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
acc = account.get_attribute('href')
driver.get(acc)
time.sleep(3)

follvalue=followerButton()
xint = int(follvalue)
time.sleep(3)

fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
scroll = 0
while scroll < xint:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(0.1)
    scroll += 1
    if scroll == xint/2:
        print("break")
        break
    else:
        pass

def follGet(n):
    try:
        str_n = str(n)
        follXpath = '/html/body/div[4]/div/div[2]/ul/div/li[' + str_n + ']/div/div[1]/div[2]/div[1]/a'
        follower_name = driver.find_element_by_xpath(follXpath)
        time.sleep(0.2)
        follvalue = (follower_name.text)
        return follvalue
    except:
        pass

folllist = []
for i in range(1, xint):
    zstr = str(follGet(i))
    print(str(i)+zstr)
    folllist.append("#TypeYourNameHere, "+login_id+", "+zstr)
print(folllist)
time.sleep(3)
with open('followers.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for follower in folllist:
        wr.writerow([follower])
time.sleep(5)
driver.close