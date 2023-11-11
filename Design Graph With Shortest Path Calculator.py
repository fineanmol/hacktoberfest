import collections
import heapq

class Graph:
    def __init__(self, n, edges):
        self.graph = collections.defaultdict(list)
        for edge in edges:
            from_node, to_node, cost = edge
            self.graph[from_node].append((to_node, cost))

    def addEdge(self, edge):
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1, node2):
        heap = [(0, node1)]  # (cost, node)
        visited = set()
        while heap:
            current_cost, current_node = heapq.heappop(heap)
            if current_node == node2:
                return current_cost
            if current_node not in visited:
                visited.add(current_node)
                for neighbor, cost in self.graph[current_node]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (current_cost + cost, neighbor))
        return -1

# Example Usage:
edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
g = Graph(4, edges)
print(g.shortestPath(3, 2))  # Output: 6
g.addEdge([1, 3, 4])
print(g.shortestPath(0, 3))  # Output: 6
