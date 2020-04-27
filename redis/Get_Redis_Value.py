# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:52:51 2020

@author: Vius
"""

"""
Get All Redis Value
"""


import redis
from configparser import ConfigParser

try :
    config = ConfigParser()
    config.read_file(open('config.ini'))
    redis_host = config['redis']['host']
    redis_port = config['redis']['port']
    redis_pass = config['redis']['password']
    
except Exception as er:
    print(er)


try:
    r = redis.Redis(host=redis_host, port=redis_port, db=0,password=redis_pass) #Try to connect to redis server
except Exception as er:
    print(er)#Print the exception error
for i in r.keys('*'):
    allkey = i.decode("utf-8")
    print("Key : %s"%allkey)
    print('Follower :')
    for n in(r.smembers(allkey)):
        print(n.decode("utf-8"))
    print('------------------------')




