from flask import Flask, render_template, url_for
import sys
import networkx as nx
import json
import community
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

    #Networkx graph configuration
    G = nx.Graph()

    infile = open('redisdb.log')      # open the file for reading

    for line in infile:      # go through the input file, one line at a time
        line = line.strip()     # remove the newline character at the endof each line
        root,follower = line.split(',')       # split up line around comma characters
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
    
    return ''


if __name__ == '__main__':
    sys.stderr.write("=============================== MEMBUAT VISUALISASI DATA FOLLOWER INSTAGRAM DENGAN GRAPH ======================================\n")
    sys.stderr.write("========= NB : Tampilkan visualisasi dengan membuka link yang terbentuk setelah menjalankan program pada browser anda ========= \n")
    app.debug = True
    app.run()
    url_for('static', filename='data.json')
