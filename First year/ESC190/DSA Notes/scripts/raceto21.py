class Node:
    def __init__(self,data):
        self.data = data
        self.neighbours = [] 

class Graph:
    def __init__(self):
        self.nodes = [] 

def generate_neighbours(x):
    n1 = x+1; n2 = x+2
    neighbours = []
    if n1 <= 21:
        neighbours.append(n1)
    if n2 <= 21:
        neighbours.append(n2)
    return neighbours


def bfs21(): 
    # starting node is 0
    queue = [0]
    # visited set not needed because you aren't backtracking
    counter = 0
    while len(queue) > 0: 
        myval = queue.pop(0)
        if myval == 21:
            counter += 1
        # leaf nodes
        queue.extend(generate_neighbours(myval))

    return counter

def filter_neighbours(neighbours):
    res = []
    for n in neighbours:
        if n[-1] <= 21:
            res.append(n)
    
    return res
def bfs21qilin():
    # starting node: [0]
    # don't have node.neighbours: need to generate them
    # don't need to worry about returning to visited nodes,
    # since cannot go back from +1 or +2 to a previous game state

    counter = 0
    queue = [[0]]
    while len(queue) > 0:
        node = queue.pop(0)
        if node[-1] == 21:
            print(node); counter += 1
        neighbours = filter_neighbours([node + [node[-1] + 1], node + [node[-1] + 2]])
        queue.extend(neighbours)

    return counter

        
print(bfs21())
# print(bfs21qilin())