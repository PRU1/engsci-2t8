import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0

    previous_nodes = {node : None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq) # remember pq is a tuple
        
        if current_distance > distances[current_node]: # we've already found a better path
            continue

        for neighbour, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                previous_nodes[neighbour] = current_node
                heapq.heappush(pq, (distance, neighbour)) # push neighbour node to the queue

    return distances, previous_nodes
        

# Example graph as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

distances, previous_nodes = dijkstra(graph, 'A')
print("Shortest distances:", distances)
