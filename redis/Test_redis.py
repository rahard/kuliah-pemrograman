# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:52:51 2020

@author: Vius
"""

"""
Test Kebutuhan Redis Server
"""


import redis

try:
    r = redis.Redis(host='103.89.6.76', port=6379, db=0,password='proglan') #Try to connect to redis server
except Exception as er:
    print(er)#Print the exception error
    
a = r.keys('*') #Get list of all key
print(a) # Print all available Key

b = list(r.smembers('root'))#Get list of all value of root key
# print(b)
for i in range(len(b)):
    print (b[i].decode("utf-8")) # Decode the byte object to str


#Just for debug
# r.delete('root') #Delet specific key and all value


