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

def bfs21():
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
def filter_neighbours(neighbours_list):
    res = [] 
    for neighbour in neighbours_list:
        if neighbour[-1] <= 21:
            res.append(neighbour)
    return res

def dfs21(starting_position):
    # don't need to track what is visited
    # put things in stack from 3 --> 1, that gets you a  g r e e d y  approach
    # will hopefully get you the shortest path to VICTORYYYYYYY

    # approaches you can take
        # explore all possible paths and store them. sort them. find the shortest possible path. 
    master_list = []
    # every node you explore, append a new list to master_list
    stack = [[starting_position]]
    while len(stack) > 0:
        cur = stack.pop()
        if cur[-1] == 21:
            master_list.append(cur)
        # generate neighbours
        neighbours = filter_neighbours([cur + [cur[-1]+1], cur + [cur[-1]+2], cur + [cur[-1]+3]])
        stack.extend(neighbours)

    # you win if you take the even number move
    # filter out the ways you win
    youWins = []
    for win in master_list:
        if len(win)-1 % 2 == 0: 
            youWins.append(win)
    # find the smallest length win
    mysuperduperwin = 9999999999

    for mywin in youWins:
        mysuperduperwin = min(len(mywin), mysuperduperwin)
    yaya = []
    for mywin in youWins:
        if len(mywin) == mysuperduperwin:
            yaya.append(mywin)

    return yaya

print(dfs21(0))
