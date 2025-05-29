def filter_neighbours(neighbours):
    res = []
    for n in neighbours:
        if n[-1] <= 21:
            res.append(n)

    return res
def bfs21():
    # starting node: [0]
    # don't have node.neighbours: need to generate them
    # don't need to worry about returning to visited nodes,
    # since cannot go back from +1 or +2 to a previous game state

    queue = [[0]]
    while len(queue) > 0:
        node = queue.pop(0)
        if node[-1] == 21:
            print(node)
        neighbours = filter_neighbours([node + [node[-1] + 1], node + [node[-1] + 2]])
        queue.extend(neighbours)

def dfs21():
    # starting node: [0]
    # don't have node.neighbours: need to generate them
    # don't need to worry about returning to visited nodes,
    # since cannot go back from +1 or +2 to a previous game state

    queue = [[0]]
    while len(queue) > 0:
        node = queue.pop(0)
        if node[-1] == 21:
            print(node)
        neighbours = filter_neighbours([node + [node[-1] + 1], node + [node[-1] + 2]])
        queue.extend(neighbours)
# recursive approach:

def gen_neighbours(x):
    n1 = x+1
    n2 = x+2
    n3 = x+3
    neighbours = []
    if n1 <= 21:
        neighbours.append(n1)
    if n2 <= 21:
        neighbours.append(n2)
    if n3 <= 21:
        neighbours.append(n3)
    return neighbours

def dfs21():
    queue = [0]
    counter = 0
    while len(queue) > 0:
        print(len(queue))
        if queue[0] == 21:
            counter += 1
        # generate leaf nodes
        queue.extend(gen_neighbours(queue[0]))
        queue.pop(0)
    return counter

def testingFunc():
    #testing will this give en arror;
    a = 10
    for i in range(5):
        pass
    # it's good at showing errors, but not what the error is.
    # + no intellisense, which is kind of sad :(

def test():
    a = [1,3,4,45]
    a.append(x)
    what = a.pop(4)
    print(what + "is going on")
