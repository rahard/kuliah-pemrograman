# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:52:51 2020

@author: Vius
"""

"""
Get Redis Server Status
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
key = r.info('keyspace') 
db = []
server=r.info('server')
uptime = server['uptime_in_days']
client = r.info('Clients')
conclient = client['connected_clients']
print('Server Uptime : %s days'%uptime)
print('Connected Client : %s'%conclient)

for i in key.keys():
    rediskey = key[i]['keys']
    expire = key[i]['expires']
    print ('DB : %s'%i)
    print ('Key Available : %s'%rediskey)
    print ('Expires Key : %s'%expire)
print ('---------------------')
print('Available Keys :')
for i in r.keys('*'):
    allkey = i.decode("utf-8")
    print(allkey)

