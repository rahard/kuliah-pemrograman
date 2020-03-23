# example_consumer.py
import pika, os, time


# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
#url = 'amqp://dppueivp:8gHNY8X_xNkryB9lIx-vQWdyqa_-hTAT@clam.rmq.cloudamqp.com/dppueivp'
try:
   url = os.environ["CLOUDAMPQ_URL"]
except KeyError:
   print("Environment variabel belum diset")
   sys.exit(1)

print(url)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='InQueue') # Declare a queue

  
# set up subscription on the queue
method_frame,header_frame,body = channel.basic_get('InQueue')

if method_frame.NAME == 'Basic.GetEmpty':
    connection.close()
    print("nothing")
else:
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    connection.close()
    print(body)


