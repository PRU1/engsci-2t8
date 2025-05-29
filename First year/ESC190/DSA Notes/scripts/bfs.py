class Node:
    def __init__(self,data):
        self.data = data
        self.neighbours = [] 

class Graph:
    def __init__(self):
        self.nodes = [] 
        
def bfs(graph):
    visited = set() # empty set
    queue = [0]
    # search all neighbours and add to queue
    # let's just say you start at graph.nodes[0]
    queue[0] = graph.nodes[0]
    while (len(queue) > 0):
        node = queue.pop(0)
        if node not in visited:
            print(node.data)
            visited.add(node)
            queue.extend(node.neighbours)
    
    
def dfs(graph):
    visited = set() # empty set
    queue = [0]
    # search all neighbours and add to queue
    # let's just say you start at graph.nodes[0]
    queue[0] = graph.nodes[0]
    while (len(queue) > 0):
        node = queue.pop()
        if node not in visited:
            print(node.data)
            visited.add(node)
            queue.extend(node.neighbours)

    
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.neighbours = [B]
B.neighbours = [A, E, D, C]
C.neighbours = [B, D]
D.neighbours = [B, C, E]
E.neighbours = [B, D, F]
F.neighbours = [E]

graph = Graph()
graph.nodes = [C, B, D, A, E, F]

bfs(graph)