#Queue Checker, menggunakan HTTP API dari management plugin untuk RabbitMQ
#menampilkan jlh pesan ready, pesan published dan pesan consumed
#Rhesa      13216006
#Richard    23219059

import sys,  json, requests

if len(sys.argv) < 5:
    print("Usage: rabbitmqchecker.py username password host queuename")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
server = sys.argv[3]
queue_name = sys.argv[4]
print("Username: ", sys.argv[1]) #untuk penggunaan debugging, ditampilkan seluruh data yg dipakai
print("Password: ", sys.argv[2])
print("Host    : ", sys.argv[3])
print("Queue   : ", sys.argv[4])

port = "15672" #port 15672 utk http
vhost = "%2f" #untuk nama vhost yang "/" diganti dengan %2f

url1 = "http://%s:%s/api/queues/%s/%s" % (server, port, vhost, queue_name) #mengikuti format http://host:port/api/queues/vhost/queuename
#url2 = "http://%s:%s/api/overview" % (server, port) tidak dipakai. sebelumnya digunakan untuk debugging HTTP API

fetcher = requests.get(url1, auth=(username,password)) #mendapatkan HTTP Response dengan menggunakan plugin requests untuk python
result = fetcher.json() #hasil http request (json) disimpan
rabbitmq_readymessage = result['messages_ready']                #mengambil value messages yg ready 
rabbitmq_jlhdelivered = result['message_stats']['deliver_get']  #mengambil value messages yg delivered, sub value dari message_stats
rabbitmq_jlhpublished = result['message_stats']['publish']      #mengambil value messages yg sudah di publish, sub value dari message_stats
print("Jumlah Pesan Ready: %s, Pesan Published: %s, Pesan Consumed: %s" % (rabbitmq_readymessage, rabbitmq_jlhpublished, rabbitmq_jlhdelivered))   #menampilkan informasi yang sudah ditarik melalui HTTP API
