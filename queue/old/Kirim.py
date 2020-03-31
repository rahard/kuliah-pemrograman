# example_publisher.py
import pika, os, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
#url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
#url = 'amqp://dppueivp:8gHNY8X_xNkryB9lIx-vQWdyqa_-hTAT@clam.rmq.cloudamqp.com/dppueivp'
try:
   url = os.environ["CLOUDAMPQ_URL"]
except KeyError:
   print("Environment variabel belum diset")
   sys.exit(1)

params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='InQueue') # Declare a queue
# send a message

for i in range (1,5):
    pesan = "'rhesa','root','follower "+str(i)+"'"
    channel.basic_publish(exchange='', routing_key='InQueue', body=pesan) #routing key adalah target queue
    print ("[x] Message sent to consumer")
connection.close()
