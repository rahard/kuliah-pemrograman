import pika, os, time
import sys
QueueTarget = "InQueue" #Target Queue

try:
   url = os.environ["CLOUDAMPQ_URL"] #Set Queue Address at environment variable
except KeyError:
   print("Environment variabel has not been set")
   sys.exit(1)

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue=QueueTarget) # Declare a queue

  
# set up subscription on the queue
method_frame,header_frame,body = channel.basic_get(QueueTarget)

if method_frame.NAME == 'Basic.GetEmpty':
    connection.close()
    print("nothing")
else:
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    connection.close()
    String = body
    print(String)


