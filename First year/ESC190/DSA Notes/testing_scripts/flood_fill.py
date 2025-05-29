def floodFill(image, sr, sc, color):
    originColour = image[sr][sc]
    # image[sr][sc]=color
    visited = []
    queue = []
    queue.append((sr, sc))
    rowCount = len(image)
    colCount = len(image[0]) 

    while (len(queue) > 0):
        # add up to four cells to queue
        # first check if you can access them
        cur = queue[0]
        if image[cur[0]][cur[1]] != originColour:
            del queue[0]
        else:
            up=cur[0]; down=cur[0]; left=cur[1]; right=cur[1]
            up = up-1 if up-1 >= 0 else up
            down = down+1 if down+1 < rowCount else down
            left = left-1 if left-1 >= 0 else left
            right = right+1 if right+1 < colCount else right
            # add these four cells to the queue

            if image[up][cur[1]] == originColour and (up,cur[1]) not in visited:
                queue.append((up, cur[1]))
                visited.append((up, cur[1]))
            if image[down][cur[1]] == originColour and (down,cur[1]) not in visited:
                queue.append((down, cur[1]))
                visited.append((down, cur[1]))
            if image[cur[0]][left] == originColour and (cur[0], left) not in visited:
                queue.append((cur[0], left))
                visited.append((cur[0], left))
            if image[cur[0]][right] == originColour and (cur[0], right) not in visited:
                queue.append((cur[0], right))
                visited.append((cur[0], right))
            
            image[cur[0]][cur[1]] = color
            del queue[0]

    return image 
    
image = [[0,0,0],[0,0,0]]
image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, color = 1,1,2

image = floodFill(image,sr,sc,color)

print(image)
