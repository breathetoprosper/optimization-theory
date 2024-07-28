import heapq

# Define the graph based on the given distances
graph = {
    'ISEG': {'A': 40, 'B': 60, 'C': 50},
    'A': {'B': 10, 'D': 70},
    'B': {'C': 20},
    'C': {'T': 50},
    'D': {'T': 10},
    'T': {}
}

def dijkstra(graph, start, end):
    # Priority queue to store (distance, node)
    pq = [(0, start)]
    # Distances dictionary to store the shortest path to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Path dictionary to store the path taken to reach each node
    path = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If the current distance is greater than the stored distance, continue
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct path from start to end
    current_node = end
    shortest_path = []
    while current_node:
        shortest_path.insert(0, current_node)
        current_node = path[current_node]

    return distances[end], shortest_path

# Solve for the shortest path from ISEG to T
shortest_distance, shortest_path = dijkstra(graph, 'ISEG', 'T')
print(f"The shortest distance is {shortest_distance}")
print(f"The shortest path is {' -> '.join(shortest_path)}")
