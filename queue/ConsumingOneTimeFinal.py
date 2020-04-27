#By : Rhesa/13216006
#Richard/23219059
#Queue Team

import pika, os, time #Importing all the necessary elements
import sys,json,configparser

from configparser import ConfigParser #Import configParser

CONF = "C:/Users/USER/Desktop/JarkomTest/SendConsumeQueue/config.ini" #Use config.ini for config

def Parse(Box): #Function to form a parsing
   String = Box[2:-1] #Erase the first and second character (which always be b and ') and erase last character (which always be ')
   return String

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

[username,password,host,port] = ReadConfig() #Save on global variable

url = ''.join(['amqp://',username,':',password,'@',host,':',port]) #Build URL Cloudamqp

#Checking the arguments
numberargs = len(sys.argv)
if (numberargs < 2):
    sys.stderr.write("Correct Usage: " + sys.argv[0] + " TargetQueue\n")
    exit(1)

QueueTarget = sys.argv[1] #From CLI 

#Using pika library
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue=QueueTarget) # Declare a queue

method_frame,header_frame,body = channel.basic_get(QueueTarget) #Consuming Process

if method_frame == None: #If the Queue is empty
    connection.close()
    String = str(body)
else: #If the Queue is not empty
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    connection.close()
    Box = str(body)
    String = Parse(Box) #Parsing the body

sys.stdout.write(String) #Print the string to a file
#If you want to save it on txt, use pytohn3 ConsumingOneTimeV3 > name of txt file


