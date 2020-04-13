#By : Rhesa/13216006

import pika, os, time #Importing all the necessary elements
import sys
QueueTarget = "InQueue" #Target Queue, can be InQueue or OutQueue

def Parse(Box): #Function to form a parsing
   String = Box[2:-1] #Erase the first and second character (which always be b and ') and erase last character (which always be ')
   return String


#Checking the arguments
numberargs = len(sys.argv)
if (numberargs < 2):
    sys.stderr.write("Correct Usage: " + sys.argv[0] + " AddressOfOutputFile\n")
    exit(1)

#Checking Environment Variable
try:
   url = os.environ["CLOUDAMPQ_URL"] #Set Queue Address at environment variable
except KeyError:
   sys.stderr.write("Environment variabel has not been set")
   sys.exit(1)

file1 = open(sys.argv[1],"a") #The address of the file is in the CLI

#Example address : c:/Users/USER/Desktop/JarkomTest/ConsumeFinal.txt

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

print(String) #Print the string
file1.write(String+"\n") #Write on an external files
file1.close() #to change file access modes 


