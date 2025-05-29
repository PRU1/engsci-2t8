import LL
import ds
# Want: the same kind of functions as we have in Graph
# Want to repreesnt the data using adjacency list

# for each node, keep a list of its neighbours (i.e. nodes connected to it)
# use linked lists in order to store the neighbours


#     1
#   / \
# 2    3

# 1: 2->3  # could also be 3->2
# 2: 1
# 3: 1

class adjList:
    def __init__(self, num_nodes = 0):
        self.nodes = [] # initialize an empty list that will store nodes
        self.node_names = {} # dictionary of node names
        self.node_names_rev = {} # reversed I guess??
        self.num_nodes = num_nodes 
        # initialize your list
        for i in range(self.num_nodes):
            self.nodes.append(LL.LL()) # each node has a linked list
        
    def add_node(self, name):
        self.node_names[name] = len(self.nodes) # len(self.nodes) is the next available index
        self.node_names_rev[len(self.nodes)] = name  # bidirectional class
        self.nodes.append(LL.LL())
        self.num_nodes += 1
    
    def is_edge(self, i, j):
        return self.nodes[i].is_in(j) #is_in defined in LL.py
    
    def is_edge_name (self, name1, name2):
        return self.is_edge(self.node_names[name1], self.node_names[name2]) # don't need reversed?
    def put_edge(self, i, j):
        self.nodes[i].insert(0,j) # interesting to use 0

    def put_edge_name(self, name1, name2):
        return self.put_edge(self.node_names[name1], self.node_names[name2])

    def remove_edge(self, i, j):
        self.nodes[i].remove(j)

import numpy as np 
class adjMatrix:
    def __init__(self, num_nodes):
        self.adj_matrix = np.zeros((num_nodes, num_nodes)) # declare 2x2 matrix

    def is_edge(self, i, j):
        return self.adj_matrix[i][j] == 1
    
    def put_edge(self, i, j):
        self.adj_matrix[i][j] = 1

    def remove_edge(self, i, j):
        self.adj_matrix[i][j] = 0

def breadth_first_traversal(g, start_name): # I'm pretty sure this assumes linked list
    start_i = g.node_names[start_name]
    visited = [False] * g.num_nodes # [False, False, False, ...]
    DS = ds.Queue()
    DS.add(start_i)
    # keep getting a node for DS, adding all its neighbours to DS, and visiting the node
    while not DS.is_empty():
        cur = DS.get()
        if not visited[cur]:
            print(g.node_names_rev[cur])
            visited[cur] = True
            # Now add all the neighbours (nodes with an edge from cur) to DS
            # to be visited later
            cur = g.nodes[cur].head
            while cur:
                if not visited[cur.data]:
                    DS.add(cur.data)
                cur = cur.next

def breadth_first_traversalv2(g, start_name, target_name): # I'm pretty sure this assumes linked list
    counter = 0

    start_i = g.node_names[start_name]
    visited = [False] * g.num_nodes # [False, False, False, ...]
    DS = ds.Queue()
    DS.add(start_i)
    # keep getting a node for DS, adding all its neighbours to DS, and visiting the node
    while not DS.is_empty():
        counter += 1
        cur = DS.get()
        if not visited[cur]:
            # print(g.node_names_rev[cur])
            if (g.node_names_rev[cur] == target_name):
                return counter
            visited[cur] = True
            # Now add all the neighbours (nodes with an edge from cur) to DS
            # to be visited later
            cur = g.nodes[cur].head
            while cur:
                if not visited[cur.data]:
                    DS.add(cur.data)
                cur = cur.next

    # if counter == LL_size(g.node_names):
        # return -100
        
def DFS_rec(g, cur, visited = None):
    if visited == None:
        visited = [False] * g.num_nodes
    
    cur_i = g.node_names[cur]
    cur_neighbour = g.nodes[cur_i].head
    visited[cur_i] = True
    print(cur)
    while cur_neighbour:
        if not visited[cur_neighbour.data]:
            DFS_rec(g, g.node_names_rev[cur_neighbour.data], visited)
        cur_neighbour = cur_neighbour.next

def DFS_it(g, start_name): # I'm pretty sure this assumes linked list

    # go to a node
    # add all neighbhours to our queue
    # go through our queue
    # repeat

    start_i = g.node_names[start_name]
    visited = [False] * g.num_nodes # [False, False, False, ...]
    DS = ds.Stack()
    DS.add(start_i)
    # keep getting a node for DS, adding all its neighbours to DS, and visiting the node
    while not DS.is_empty():
        cur = DS.get()
        if not visited[cur]:
            print(g.node_names_rev[cur])
            visited[cur] = True
            # Now add all the neighbours (nodes with an edge from cur) to DS
            # to be visited later
            cur = g.nodes[cur].head
            while cur:
                if not visited[cur.data]:
                    DS.add(cur.data)
                cur = cur.next


def DFS_recv2(g, cur, target, visited = None, counter = 0):
    if visited == None:
        visited = [False] * g.num_nodes
    
    cur_i = g.node_names[cur]
    cur_neighbour = g.nodes[cur_i].head
    visited[cur_i] = True
    print(cur, counter)
    if cur == target:
        print("found")
        return counter
    while cur_neighbour:
        if not visited[cur_neighbour.data]:
            DFS_recv2(g, g.node_names_rev[cur_neighbour.data], target, visited, counter = counter + 1)
        cur_neighbour = cur_neighbour.next
        # size of depth


def dfs_recursive(g, cur, visited = None): # I dunno why this doesn't work
     # base case
     if visited == None:
         visited = [False] * g.num_nodes

     # recursive case
     else: 
         cur_i = g.node_names[cur]
         cur_neighbour = g.nodes[cur_i].head # head interesting
         visited[cur_i] = True 
         print(cur)
         while cur_neighbour:
             if not visited[cur_neighbour.data]:
                 dfs_recursive(g, g.nodes_names.rev[cur_neighbour.data], visited)
             cur_neighbour = cur_neighbour.next


def dsf_iterative(g, cur):
    dict = g.node_names
    for key in dict:
        dict[key] = False

    stack = []
    
    stack.append(cur)
    
    while (len(stack)):
        s = stack[-1]
        stack.pop()
        if not dict[s]:
            print(s)
            dict[s] = True
            
        for node in cur.node_names_rev:
            if not dict[node]:
                stack.append(node)

if __name__ == '__main__':
    # g = Graph(4) # Graph.__init__(g, 4)
    # g.put_edge(1, 2) # Graph.put_edge(g, 1, 2)
    # print(g.is_edge(1, 2))



    # setting up a matrix
    # import numpy as np
    # M = np.array((10, 10)) # a 10x10 matrix
    # M = np.zeros((10, 10)) # an all-zero 10x10 matrix
    # M[0][1] # row 0, column 1

    airports = adjList()
    airports.add_node("CYYZ")
    airports.add_node("CYVR")
    airports.add_node("CPC3")

    airports.add_node("CNT7")

    airports.add_node("CYTR")

    airports.add_node("CZBM")

    airports.add_node("CYUL")

    airports.add_node("CYJN")


    
    airports.put_edge_name("CYVR", "CNT7")
    airports.put_edge_name("CYYZ", "CYVR")
    airports.put_edge_name("CYYZ", "CPC3")
    airports.put_edge_name("CYYZ", "CYTR")

    airports.put_edge_name("CYTR", "CZBM")
    airports.put_edge_name("CYYZ", "CYUL")
    airports.put_edge_name("CYTR", "CPC3")


    #breadth_first_traversalv2(airports, "YVR")
    #dfs_recursive(airports, "YYZ", visited=None)
    # print(breadth_first_traversalv2(airports, "YYZ", "JFK"))
    # DFS_rec(airports, "YYZ")

    # DFS_recv2(airports, "YYZ", "YVR")
    DFS_it(airports, "CYYZ")
    # dsf_iterative(airports, "YYZ")


    #    YYZ
    #  / ^  \
    # v  /    v
    # YVR     JFK