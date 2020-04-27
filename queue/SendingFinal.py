#By : Rhesa/13216006
#Richard/23219059
#Queue Team

import pika, os, logging #Importing all the necessary elements
import sys,json,configparser 

from configparser import ConfigParser #Import configParser

logging.basicConfig()

CONF = "C:/Users/USER/Desktop/JarkomTest/SendConsumeQueue/config.ini" #Use config.ini for config

def ReadConfig():
    config = ConfigParser()
    success = config.read(CONF)
    if(len(success)<1):
        sys.stderr.write("Failed to read "+ CONF + "\n")
        sys.exit(1)
    #Read Queue Section
    username = config.get('queue','username')
    password = config.get('queue','password')
    host = config.get('queue','host')
    port = config.get('queue','port')
    return(username,password,host,port) #Return value for Queue Config

[username,password,host,port] = ReadConfig() #Save it on global variable

url = ''.join(['amqp://',username,':',password,'@',host,':',port]) #Build URL Cloudamqp

#Checking the arguments 
numberargs = len(sys.argv)
if(numberargs > 1) :
    if(sys.argv[1] == 'InQueue'):
        if (numberargs < 5):
            sys.stderr.write("Correct Usage for InQueue: " + sys.argv[0] + " InQueue IDSubmit Root Follower\n")
            exit(1)
    elif(sys.argv[1] == 'OutQueue'):
        if (numberargs < 3):
            sys.stderr.write("Correct Usage for OutQueue: " + sys.argv[0] + " OutQueue Follower\n")
            exit(1)
    else :
        sys.stderr.write("Correct TargetQueue Name = InQueue or OutQueue\n")
        exit(1)
else :
    sys.stderr.write("Correct Usage: \nFor OutQueue : " + sys.argv[0] + " OutQueue Follower \nFor InQueue : " + sys.argv[0] + " InQueue IDSubmit Root Follower\n") 
    exit(1)

QueueTarget = sys.argv[1] #From CLI
#Using pika library
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue=QueueTarget) # Declare a queue

if(QueueTarget == 'OutQueue'):
    pesan = sys.argv[2]
else : #IF QueueTarget is InQueue
    pesan = sys.argv[2] + ' ' + sys.argv[3] + ' ' + sys.argv[4] #From CLI Arguments

print(pesan)
channel.basic_publish(exchange='', routing_key=QueueTarget, body=pesan) #Sending Process
print ("[x] Message sent to " + QueueTarget + "\n")

connection.close()
