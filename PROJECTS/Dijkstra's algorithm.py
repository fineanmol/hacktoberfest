import heapq

def dijkstra(graph, start):
    # Initialize distances and visited set
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()

    # Priority queue to store vertices with their distances
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if we have already processed this vertex
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If we find a shorter path to the neighbor, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

for vertex, distance in shortest_distances.items():
    print(f'Shortest distance from {start_vertex} to {vertex} is {distance}')
