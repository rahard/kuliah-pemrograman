# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:17:12 2020

@author: Vius
"""

"""
1. Ambil data dari InQueue dengan Akun yang di Crawl sebagai Key, dan list followernya kedalam sebuah "Set" di redis
2. Follower yang belum menjadi key (belum pernah di Crawl) akan dikirimkan ke OutQueue
3. Sumber data dari "localdb.log"

"""


import pika
#import json # Belum Json euy dari Tim MQ

import redis
from configparser import ConfigParser

queconn = 0


try :
    config = ConfigParser()
    config.read_file(open('config.ini'))
    que_host = config['queue']['host']
    que_portmq = config['queue']['port']
    que_uid = config['queue']['username']
    que_pass = config['queue']['password']
    redis_host = config['redis']['host']
    redis_port = config['redis']['port']
    redis_pass = config['redis']['password']
    url = 'amqp://'+ que_uid +':'+ que_pass +'@'+ que_host +':'+ que_portmq
except Exception as er:
    print(er)


def parsedata(body): # Resplit the output from the mq
    a = body.strip().split(' ')
    return a


try:
    r = redis.Redis(host=redis_host, port=redis_port, db=0,password=redis_pass) #Try to connect to redis server
except Exception as er:
    print(er)#Print the exception error


try:
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    channel = connection.channel() # start a channel
except Exception as er:
    print(er)
    # sys.exit(1)
                        
        
f = open('localdb.log','r')
for data in f:
    z = parsedata(data)
    PIC = z[0]  #Still dont know where to put this 
    root = z[1]
    foll = z[2]
    
    if (r.sismember(root, foll)) == 0: # Check if the follower value have been added to the key
        r.sadd(root,foll) #Add follower to key value
        print("Add value '%s' to key '%s' " % (foll,root))
        if (r.exists(foll)) == 0:  # Check if the follower have been crawled and added to the key list
            channel.basic_publish(exchange='', routing_key='OutQueue', body=foll) # Post the value to the Out Queue if not yet available in key
            print("Send '%s' to OutQueue " % (foll))
    else:
        pass

f.close()
    
       
    
