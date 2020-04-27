from flask import Flask, jsonify, render_template, url_for
import os, sys
import redis
import networkx as nx
import configparser
import json, community
from networkx.readwrite import json_graph
from networkx.algorithms import centrality as cn

'''
############# code create by Agus Raharja n Arief N R 26-04-2020 #############
Create dinamics graph using networkx and d3 library
'''

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    #read requirement file
    try:
        namafile = 'config.ini'
        config = configparser.ConfigParser()
        config.read_file(open(namafile))
        redis_host = config['redis']['host']
        redis_port = config['redis']['port']
        redis_pass = config['redis']['password']
    except KeyError:
        sys.stderr.write("Tidak Bisa Membuka File" + namafile +"\n")
        sys.exit(1)

    #Networkx graph configuration
    G = nx.Graph()

    #Redis graph configuration
    r = redis.Redis(host=redis_host, port=redis_port, db=0,password=redis_pass)

    #list redis keys
    for k in r.keys('*'):   
        #get value from redis keys
        value = k.decode("utf-8") 
    
        #change data type to string
        root = k.decode("utf-8")        
        #print("Root : " + root + "\n Follower : " ) 
        for follower in (r.smembers(value)):
            # create edges list from key and value
            G.add_edge(root, follower.decode("utf-8"))
            #print(follower.decode("utf-8"))
        #print('----------------------------------')    

    # Initialize graph, add nodes and edges, calculate modularity and centrality.
    groups = community.best_partition(G)
    degree = cn.degree_centrality(G)

    # Add node attributes for name, modularity, and three types of centrality.
    nx.set_node_attributes(G, groups,'group')
    nx.set_node_attributes(G, degree,'degree')

    # create json dictionary format for networkx edges
    data1 = json_graph.node_link_data(G)

    #output json file
    with open('static/data.json', 'w') as output:
        json.dump(data1, output, sort_keys=True, indent=4, separators=(',',':'))
    
    return ''


if __name__ == '__main__':
    app.debug = True
    app.run()
    url_for('static', filename='data.json')
