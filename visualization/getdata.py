from flask import Flask, jsonify, render_template, url_for
import os, sys
import redis
import networkx as nx
import configparser
import json, community
from networkx.readwrite import json_graph
from networkx.algorithms import centrality as cn

'''
############# code create by Agus Raharja 20-04-2020 #############
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
        rurl = config.get('redis', 'REDIS_URL')
        rport = config.get('redis', 'REDIS_PORT')
        rpass = config.get('redis', 'REDIS_PASS')
    except KeyError:
        sys.stderr.write("Tidak Bisa Membuka File" + namafile +"\n")
        sys.exit(1)

    #Networkx graph configuration
    G = nx.Graph()

    #Redis graph configuration
    r = redis.Redis(host=rurl, port=rport, db=0 , password=rpass)

    #list redis keys
    for k in r.keys('*'):   
        #get value from redis keys
        value = str(r.get(k))

        #delete the header format (b') from value
        panjang =len(value)
        value = value[2:(panjang-1)]

        #split the value
        arrvalue = value.split(',')
        
        #change data type to string
        root = str(k)
        
        #delete the header format (b') from root
        panjangkey =len(root)
        root = root[2:(panjangkey-1)]
        
            
        for follower in arrvalue :
            # create edges list from key and value
            G.add_edge(root, follower)

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
    
    return data1


if __name__ == '__main__':
    app.debug = True
    app.run()
    url_for('static', filename='data.json')
