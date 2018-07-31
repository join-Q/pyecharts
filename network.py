import networkx as nx 
from networkx.readwrite import json_graph
from pyecharts import Graph 
g=nx.Graph()
g.add_node('G1',name="gateway 1")
g.add_node('N2',name="Node 2")
g.add_node('N3',name="Node 3")
g.add_edge('G1','N2')
g.add_edge('G1','N3')
g_data=json_graph.node_link_data(g)
eg=Graph('设备最新拓扑图')
eg.add("Device",nodes=g_data['nodes'],links=g_data["links"])
eg.render()

