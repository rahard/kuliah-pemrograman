#By : Rhesa/13216006

import pika, os, logging #Importing all the necessary elements
import sys
logging.basicConfig()

QueueTarget = "OutQueue" #Target Queue, can be InQueue or OutQueue

#Checking the arguments
numberargs = len(sys.argv)
if (numberargs < 4):
    sys.stderr.write("Correct Usage: " + sys.argv[0] + " IDSubmit Root Follower\n")
    exit(1)

#Checking Environment Variable
try:
   url = os.environ["CLOUDAMPQ_URL"] #Set Queue Address at environment variable
except KeyError:
   sys.stderr.write("Environment variabel has not been set")
   sys.exit(1)

#Using pika library
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue=QueueTarget) # Declare a queue

pesan = sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] #From CLI Arguments
print(pesan)
channel.basic_publish(exchange='', routing_key=QueueTarget, body=pesan) #Sending Process
print ("[x] Message sent to " + QueueTarget)

connection.close()
