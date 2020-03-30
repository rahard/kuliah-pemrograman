import pika, os, logging
import sys
logging.basicConfig()

QueueTarget = "InQueue" #Target Queue

#Checking the arguments
numberargs = len(sys.argv)
if (numberargs < 4):
    print("Correct Usage: " + sys.argv[0] + " IDSubmit Root Follower")
    exit(1)

#Checking Environment Variable
try:
   url = os.environ["CLOUDAMPQ_URL"] #Set Queue Address at environment variable
except KeyError:
   print("Environment variabel has not been set")
   sys.exit(1)

params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue=QueueTarget) # Declare a queue

pesan = sys.argv[1] + ',' + sys.argv[2] + ',' + sys.argv[3] #From Arguments
print(pesan)
channel.basic_publish(exchange='', routing_key=QueueTarget, body=pesan) #routing key is the target queue
print ("[x] Message sent to " + QueueTarget)

connection.close()
