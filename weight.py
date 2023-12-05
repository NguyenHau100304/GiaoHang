def getWeight(G, route):
    trongso = 0

    for i in range(len(route)-1):
        u, v = route[i], route[i+1]
        edge_data = G.get_edge_data(u, v)
        travel_time = edge_data[0]['travel_time']
        trongso += travel_time
    return trongso
