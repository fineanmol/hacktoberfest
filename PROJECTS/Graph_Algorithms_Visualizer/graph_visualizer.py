"""
Graph Algorithms Visualization Tool
Author: AI Assistant
GitHub: https://github.com/fineanmol/hacktoberfest
Language: Python
Description: Interactive visualization tool for graph algorithms including BFS, DFS, Dijkstra's, and more
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import networkx as nx
from collections import deque, defaultdict
import heapq
import random
import time


class GraphVisualizer:
    """Interactive graph visualization with multiple algorithms"""
    
    def __init__(self):
        self.graph = nx.Graph()
        self.pos = {}
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.animation_frames = []
        self.current_frame = 0
        
    def add_node(self, node):
        """Add a node to the graph"""
        self.graph.add_node(node)
        self._update_layout()
    
    def add_edge(self, u, v, weight=1):
        """Add an edge between nodes u and v"""
        self.graph.add_edge(u, v, weight=weight)
        self._update_layout()
    
    def add_random_graph(self, num_nodes=10, num_edges=15, weighted=True):
        """Generate a random graph for demonstration"""
        self.graph.clear()
        
        # Add nodes
        for i in range(num_nodes):
            self.graph.add_node(i)
        
        # Add random edges
        edges_added = 0
        while edges_added < num_edges:
            u = random.randint(0, num_nodes - 1)
            v = random.randint(0, num_nodes - 1)
            if u != v and not self.graph.has_edge(u, v):
                weight = random.randint(1, 10) if weighted else 1
                self.graph.add_edge(u, v, weight=weight)
                edges_added += 1
        
        self._update_layout()
    
    def _update_layout(self):
        """Update the layout of the graph"""
        if len(self.graph.nodes()) > 0:
            self.pos = nx.spring_layout(self.graph, k=3, iterations=50)
    
    def visualize_graph(self, title="Graph Visualization", highlight_nodes=None, highlight_edges=None):
        """Visualize the current graph"""
        self.ax.clear()
        
        # Draw all nodes
        nx.draw_networkx_nodes(self.graph, self.pos, 
                              node_color='lightblue', 
                              node_size=500,
                              ax=self.ax)
        
        # Highlight specific nodes if provided
        if highlight_nodes:
            nx.draw_networkx_nodes(self.graph, self.pos, 
                                  nodelist=highlight_nodes,
                                  node_color='red', 
                                  node_size=700,
                                  ax=self.ax)
        
        # Draw all edges
        nx.draw_networkx_edges(self.graph, self.pos, 
                              edge_color='gray',
                              width=2,
                              ax=self.ax)
        
        # Highlight specific edges if provided
        if highlight_edges:
            nx.draw_networkx_edges(self.graph, self.pos, 
                                  edgelist=highlight_edges,
                                  edge_color='red',
                                  width=4,
                                  ax=self.ax)
        
        # Draw labels
        nx.draw_networkx_labels(self.graph, self.pos, 
                              font_size=12, 
                              font_weight='bold',
                              ax=self.ax)
        
        # Draw edge weights
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.pos, 
                                    edge_labels,
                                    font_size=10,
                                    ax=self.ax)
        
        self.ax.set_title(title, fontsize=16, fontweight='bold')
        self.ax.axis('off')
        plt.tight_layout()
        plt.show()
    
    def bfs_visualization(self, start_node):
        """Breadth-First Search with step-by-step visualization"""
        if start_node not in self.graph.nodes():
            print(f"Node {start_node} not found in graph!")
            return
        
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        bfs_order = [start_node]
        
        # Initial visualization
        self.visualize_graph(f"BFS Starting from Node {start_node}")
        time.sleep(1)
        
        while queue:
            current = queue.popleft()
            
            # Visualize current node being processed
            self.visualize_graph(f"BFS: Processing Node {current}", 
                               highlight_nodes=[current])
            time.sleep(0.8)
            
            # Process neighbors
            for neighbor in self.graph.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    bfs_order.append(neighbor)
                    
                    # Visualize new discovery
                    self.visualize_graph(f"BFS: Discovered Node {neighbor}", 
                                       highlight_nodes=[current, neighbor])
                    time.sleep(0.8)
        
        # Final result
        self.visualize_graph(f"BFS Complete! Order: {bfs_order}", 
                           highlight_nodes=bfs_order)
        print(f"BFS traversal order: {bfs_order}")
        return bfs_order
    
    def dfs_visualization(self, start_node):
        """Depth-First Search with step-by-step visualization"""
        if start_node not in self.graph.nodes():
            print(f"Node {start_node} not found in graph!")
            return
        
        visited = set()
        dfs_order = []
        
        def dfs_recursive(node):
            visited.add(node)
            dfs_order.append(node)
            
            # Visualize current node being processed
            self.visualize_graph(f"DFS: Processing Node {node}", 
                               highlight_nodes=[node])
            time.sleep(0.8)
            
            for neighbor in self.graph.neighbors(node):
                if neighbor not in visited:
                    # Visualize edge being explored
                    self.visualize_graph(f"DFS: Exploring Edge {node}-{neighbor}", 
                                       highlight_nodes=[node, neighbor],
                                       highlight_edges=[(node, neighbor)])
                    time.sleep(0.8)
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_node)
        
        # Final result
        self.visualize_graph(f"DFS Complete! Order: {dfs_order}", 
                           highlight_nodes=dfs_order)
        print(f"DFS traversal order: {dfs_order}")
        return dfs_order
    
    def dijkstra_visualization(self, start_node, end_node=None):
        """Dijkstra's shortest path algorithm with visualization"""
        if start_node not in self.graph.nodes():
            print(f"Node {start_node} not found in graph!")
            return
        
        # Initialize distances
        distances = {node: float('inf') for node in self.graph.nodes()}
        distances[start_node] = 0
        previous = {}
        pq = [(0, start_node)]
        visited = set()
        
        # Initial visualization
        self.visualize_graph(f"Dijkstra's Algorithm Starting from Node {start_node}")
        time.sleep(1)
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            # Visualize current node being processed
            self.visualize_graph(f"Dijkstra: Processing Node {current} (dist: {current_dist})", 
                               highlight_nodes=[current])
            time.sleep(0.8)
            
            # Check if we reached the target
            if end_node and current == end_node:
                break
            
            # Process neighbors
            for neighbor in self.graph.neighbors(current):
                if neighbor not in visited:
                    edge_weight = self.graph[current][neighbor].get('weight', 1)
                    new_dist = current_dist + edge_weight
                    
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        previous[neighbor] = current
                        heapq.heappush(pq, (new_dist, neighbor))
                        
                        # Visualize edge relaxation
                        self.visualize_graph(f"Dijkstra: Relaxing Edge {current}-{neighbor} (new dist: {new_dist})", 
                                           highlight_nodes=[current, neighbor],
                                           highlight_edges=[(current, neighbor)])
                        time.sleep(0.8)
        
        # Show final distances
        self.visualize_graph(f"Dijkstra Complete! Distances: {distances}", 
                           highlight_nodes=list(visited))
        
        # If end node specified, show path
        if end_node and end_node in previous:
            path = []
            current = end_node
            while current is not None:
                path.append(current)
                current = previous.get(current)
            path.reverse()
            
            # Visualize shortest path
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            self.visualize_graph(f"Shortest Path from {start_node} to {end_node}: {path}", 
                               highlight_nodes=path,
                               highlight_edges=path_edges)
            print(f"Shortest path: {path}")
            print(f"Distance: {distances[end_node]}")
        
        return distances, previous
    
    def prim_mst_visualization(self):
        """Prim's Minimum Spanning Tree algorithm with visualization"""
        if len(self.graph.nodes()) == 0:
            print("Graph is empty!")
            return
        
        start_node = list(self.graph.nodes())[0]
        mst_edges = []
        mst_nodes = {start_node}
        pq = []
        
        # Add edges from start node
        for neighbor in self.graph.neighbors(start_node):
            weight = self.graph[start_node][neighbor].get('weight', 1)
            heapq.heappush(pq, (weight, start_node, neighbor))
        
        # Initial visualization
        self.visualize_graph(f"Prim's MST Algorithm Starting from Node {start_node}")
        time.sleep(1)
        
        while pq and len(mst_nodes) < len(self.graph.nodes()):
            weight, u, v = heapq.heappop(pq)
            
            if v in mst_nodes:
                continue
            
            # Add edge to MST
            mst_edges.append((u, v))
            mst_nodes.add(v)
            
            # Visualize new MST edge
            self.visualize_graph(f"Prim's MST: Added Edge {u}-{v} (weight: {weight})", 
                               highlight_nodes=list(mst_nodes),
                               highlight_edges=mst_edges)
            time.sleep(0.8)
            
            # Add edges from new node
            for neighbor in self.graph.neighbors(v):
                if neighbor not in mst_nodes:
                    edge_weight = self.graph[v][neighbor].get('weight', 1)
                    heapq.heappush(pq, (edge_weight, v, neighbor))
        
        # Final MST visualization
        self.visualize_graph(f"Prim's MST Complete! Edges: {mst_edges}", 
                           highlight_nodes=list(mst_nodes),
                           highlight_edges=mst_edges)
        
        total_weight = sum(self.graph[u][v].get('weight', 1) for u, v in mst_edges)
        print(f"MST edges: {mst_edges}")
        print(f"Total weight: {total_weight}")
        
        return mst_edges
    
    def kruskal_mst_visualization(self):
        """Kruskal's Minimum Spanning Tree algorithm with visualization"""
        if len(self.graph.nodes()) == 0:
            print("Graph is empty!")
            return
        
        # Union-Find data structure
        parent = {node: node for node in self.graph.nodes()}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True
            return False
        
        # Get all edges sorted by weight
        edges = [(self.graph[u][v].get('weight', 1), u, v) 
                for u, v in self.graph.edges()]
        edges.sort()
        
        mst_edges = []
        
        # Initial visualization
        self.visualize_graph("Kruskal's MST Algorithm Starting")
        time.sleep(1)
        
        for weight, u, v in edges:
            if union(u, v):
                mst_edges.append((u, v))
                
                # Visualize new MST edge
                self.visualize_graph(f"Kruskal's MST: Added Edge {u}-{v} (weight: {weight})", 
                                   highlight_edges=mst_edges)
                time.sleep(0.8)
                
                if len(mst_edges) == len(self.graph.nodes()) - 1:
                    break
        
        # Final MST visualization
        self.visualize_graph(f"Kruskal's MST Complete! Edges: {mst_edges}", 
                           highlight_edges=mst_edges)
        
        total_weight = sum(weight for weight, _, _ in edges if (_, _) in mst_edges)
        print(f"MST edges: {mst_edges}")
        print(f"Total weight: {total_weight}")
        
        return mst_edges
    
    def topological_sort_visualization(self):
        """Topological sort visualization (for directed graphs)"""
        # Convert to directed graph for topological sort
        if not isinstance(self.graph, nx.DiGraph):
            print("Converting to directed graph for topological sort...")
            self.graph = self.graph.to_directed()
        
        # Calculate in-degrees
        in_degree = {node: 0 for node in self.graph.nodes()}
        for u, v in self.graph.edges():
            in_degree[v] += 1
        
        # Initialize queue with nodes having no incoming edges
        queue = deque([node for node in self.graph.nodes() if in_degree[node] == 0])
        topo_order = []
        
        # Initial visualization
        self.visualize_graph("Topological Sort Starting")
        time.sleep(1)
        
        while queue:
            current = queue.popleft()
            topo_order.append(current)
            
            # Visualize current node being processed
            self.visualize_graph(f"Topological Sort: Processing Node {current}", 
                               highlight_nodes=[current])
            time.sleep(0.8)
            
            # Process neighbors
            for neighbor in self.graph.neighbors(current):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Final result
        self.visualize_graph(f"Topological Sort Complete! Order: {topo_order}", 
                           highlight_nodes=topo_order)
        print(f"Topological order: {topo_order}")
        
        return topo_order


def demo_graph_algorithms():
    """Demonstrate various graph algorithms"""
    print("=== Graph Algorithms Visualization Demo ===\n")
    
    # Create visualizer
    viz = GraphVisualizer()
    
    # Create a sample graph
    print("Creating a sample graph...")
    viz.add_random_graph(num_nodes=8, num_edges=12, weighted=True)
    
    # Show initial graph
    viz.visualize_graph("Initial Graph")
    
    # Demonstrate BFS
    print("\n1. Breadth-First Search (BFS)")
    viz.bfs_visualization(0)
    
    # Demonstrate DFS
    print("\n2. Depth-First Search (DFS)")
    viz.dfs_visualization(0)
    
    # Demonstrate Dijkstra's algorithm
    print("\n3. Dijkstra's Shortest Path Algorithm")
    viz.dijkstra_visualization(0, 7)
    
    # Demonstrate Prim's MST
    print("\n4. Prim's Minimum Spanning Tree")
    viz.prim_mst_visualization()
    
    # Demonstrate Kruskal's MST
    print("\n5. Kruskal's Minimum Spanning Tree")
    viz.kruskal_mst_visualization()
    
    print("\n=== Demo Complete ===")


def interactive_demo():
    """Interactive demo where user can choose algorithms"""
    viz = GraphVisualizer()
    
    print("=== Interactive Graph Algorithms Demo ===")
    print("1. Create random graph")
    print("2. Add custom nodes/edges")
    print("3. Run BFS")
    print("4. Run DFS")
    print("5. Run Dijkstra's algorithm")
    print("6. Run Prim's MST")
    print("7. Run Kruskal's MST")
    print("8. Run Topological Sort")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter your choice (0-8): ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            nodes = int(input("Number of nodes: ") or "8")
            edges = int(input("Number of edges: ") or "12")
            viz.add_random_graph(nodes, edges, True)
            viz.visualize_graph("Random Graph Created")
        elif choice == '2':
            print("Add nodes (comma-separated):")
            nodes = input().strip().split(',')
            for node in nodes:
                if node.strip():
                    viz.add_node(node.strip())
            
            print("Add edges (format: u,v,weight):")
            edges = input().strip().split(';')
            for edge in edges:
                if edge.strip():
                    parts = edge.strip().split(',')
                    if len(parts) >= 2:
                        u, v = parts[0].strip(), parts[1].strip()
                        weight = int(parts[2].strip()) if len(parts) > 2 else 1
                        viz.add_edge(u, v, weight)
            
            viz.visualize_graph("Custom Graph Created")
        elif choice == '3':
            start = input("Start node: ").strip()
            viz.bfs_visualization(start)
        elif choice == '4':
            start = input("Start node: ").strip()
            viz.dfs_visualization(start)
        elif choice == '5':
            start = input("Start node: ").strip()
            end = input("End node (optional): ").strip() or None
            viz.dijkstra_visualization(start, end)
        elif choice == '6':
            viz.prim_mst_visualization()
        elif choice == '7':
            viz.kruskal_mst_visualization()
        elif choice == '8':
            viz.topological_sort_visualization()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    # Run the demo
    demo_graph_algorithms()
    
    # Uncomment the line below for interactive mode
    # interactive_demo()
