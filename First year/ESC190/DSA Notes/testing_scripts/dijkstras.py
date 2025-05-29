class Node:
    def __init__(self,name):
        self.name = name
        self.connections = []
        self.visited = False
    
    def connect(node1, node2, weight):
        node1.connections.append({"node": node1, "weight": weight})
        node1.connections.append({"node": node2, "weight": weight})

def get_all_connections(node):
    connections = [] 
    q = [node]
    node.visited = True
    
    while len(q) > 0:
        cur = q.pop(0)
        connections.append(cur)
        for con in cur.connections: # this is basically a bfs
            if con["node"].visited == False:
                q.append(con["node"])
                con["node"].visited = True

    return connections

def dijkstra(node):
    # have a set of visited nodes
    # store the distances to every node
    # first stor them to infinity
    # while your unexplored node list is nonempty, keep on exploring
    S = [node] # visited nodes
    d = {node.name: 0} # dictionary of distances. starting node is set as 0
    unexplored = get_all_connections(node)

    # set all nodes to infinity
    for n in unexplored:
        if n.name not in d:
            d[n.name] = float('inf')
    
    # do algorithm until everything is explored
    while len(unexplored) > 0:
        cur = unexplored.pop(0)
        for con in cur.connections:
            if con["node"] not in S: # if you have not visited it yet
                d[con["node"].name] = min(con["weight"]+d[cur.name], d[con["node"].name])
        
        S.append(cur)
    
    return d