import sys,  json, requests, time
#import sys,  json, requests, time, msvcrt

if len(sys.argv) < 5:
    print("Usage: rabbitmqchecker.py username password host queuename")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
server = sys.argv[3]
queue_name = sys.argv[4]
print("Username: ", sys.argv[1])
print("Password: ", sys.argv[2])
print("Host    : ", sys.argv[3])
print("Queue   : ", sys.argv[4])

port = "15672"
vhost = "%2f"
#path = "/api/queues/%s/%s" % (vhost, queue_name)
url1 = "http://%s:%s/api/queues/%s/%s" % (server, port, vhost, queue_name)
url2 = "http://%s:%s/api/overview" % (server, port)
data = "-u %s:%s" % (username,password)

while 1:
    fetcher = requests.get(url1, auth=(username,password))
    result = fetcher.json()
    rabbitmq_readymessage = result['messages_ready']
    rabbitmq_jlhdelivered = result['message_stats']['deliver_get']
    rabbitmq_jlhpublished = result['message_stats']['publish']
    print("Jumlah Pesan Ready: %s, Pesan Published: %s, Pesan Consumed: %s" % (rabbitmq_readymessage, rabbitmq_jlhpublished, rabbitmq_jlhdelivered))
    time.sleep(1)
