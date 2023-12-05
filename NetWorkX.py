import networkx as nx
import osmnx as ox
from weight import getWeight

ox.config(use_cache=True, log_console=True)

osmpath = 'data\graph.osm'
place = 'Vietnam, district 5'
# get a graph
#G = ox.graph_from_place(place)
G = ox.graph_from_xml(osmpath)

# impute missing edge speed and add travel times
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)


#orig = int(input("Nhap id node 1: "))
#dest = int(input("Nhap id node 2:"))

orig = 5794928475
dest = 366368807

# calculate shortest path minimizing travel time
#orig, dest = list(G)[0], list(G)[100]
route = nx.shortest_path(G, orig, dest, 'travel_time', "dijkstra")


print("Trong so duong di: ", getWeight(G, route))

# create folium web map
route_map = ox.plot_route_folium(G, route)



html_file_path = 'route_map.html'
route_map.save(html_file_path)
import webbrowser
webbrowser.open(html_file_path)