#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt

graph = nx.DiGraph()
f = open("nodes.txt","r")

for line in f:
    n1 = line[0]
    n2 = line[6]
    graph.add_node(n1)
    graph.add_node(n2)
    graph.add_edge(n1,n2)
 
#print(graph.nodes)    
    
nx.draw_circular(graph)
nx.draw_networkx_labels(graph, pos=nx.circular_layout(graph))
plt.show()