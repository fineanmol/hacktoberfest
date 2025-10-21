# Graph Algorithms Visualization Tool

An interactive Python tool for visualizing and understanding various graph algorithms with step-by-step animations.

## Features

### Supported Algorithms
- **Breadth-First Search (BFS)**: Level-by-level traversal visualization
- **Depth-First Search (DFS)**: Deep traversal with backtracking visualization
- **Dijkstra's Algorithm**: Shortest path finding with distance updates
- **Prim's MST**: Minimum spanning tree construction
- **Kruskal's MST**: Alternative MST algorithm with union-find
- **Topological Sort**: Directed acyclic graph ordering

### Visualization Features
- **Step-by-step Animation**: Watch algorithms execute in real-time
- **Interactive Graphs**: Create custom graphs or use random generation
- **Color-coded Elements**: Different colors for visited nodes, current processing, and paths
- **Weight Display**: Edge weights shown for weighted algorithms
- **Multiple Layouts**: Automatic graph layout optimization

## Installation

```bash
pip install matplotlib networkx numpy
```

## Usage

### Basic Usage

```python
from graph_visualizer import GraphVisualizer

# Create visualizer
viz = GraphVisualizer()

# Add nodes and edges
viz.add_node('A')
viz.add_node('B')
viz.add_edge('A', 'B', weight=5)

# Run algorithms
viz.bfs_visualization('A')
viz.dfs_visualization('A')
viz.dijkstra_visualization('A', 'B')
```

### Random Graph Generation

```python
# Create a random weighted graph
viz.add_random_graph(num_nodes=10, num_edges=15, weighted=True)

# Visualize the graph
viz.visualize_graph("Random Graph")
```

### Interactive Mode

```python
# Run interactive demo
from graph_visualizer import interactive_demo
interactive_demo()
```

## Algorithm Details

### Breadth-First Search (BFS)
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Use Case**: Shortest path in unweighted graphs, level-order traversal

### Depth-First Search (DFS)
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Use Case**: Path finding, cycle detection, topological sorting

### Dijkstra's Algorithm
- **Time Complexity**: O((V + E) log V) with binary heap
- **Space Complexity**: O(V)
- **Use Case**: Single-source shortest path in weighted graphs

### Prim's MST
- **Time Complexity**: O(E log V)
- **Space Complexity**: O(V)
- **Use Case**: Minimum spanning tree construction

### Kruskal's MST
- **Time Complexity**: O(E log E)
- **Space Complexity**: O(V)
- **Use Case**: Alternative MST algorithm using union-find

## Examples

### Example 1: Basic Graph Operations

```python
viz = GraphVisualizer()

# Create a simple graph
viz.add_node(0)
viz.add_node(1)
viz.add_node(2)
viz.add_edge(0, 1, 3)
viz.add_edge(1, 2, 2)
viz.add_edge(0, 2, 5)

# Visualize
viz.visualize_graph("Simple Graph")

# Run BFS from node 0
viz.bfs_visualization(0)
```

### Example 2: Shortest Path Finding

```python
# Create a weighted graph
viz.add_random_graph(num_nodes=6, num_edges=10, weighted=True)

# Find shortest path from node 0 to node 5
viz.dijkstra_visualization(0, 5)
```

### Example 3: Minimum Spanning Tree

```python
# Create a connected graph
viz.add_random_graph(num_nodes=8, num_edges=15, weighted=True)

# Find MST using Prim's algorithm
viz.prim_mst_visualization()

# Find MST using Kruskal's algorithm
viz.kruskal_mst_visualization()
```

## Customization

### Visual Customization
- Modify colors in the `visualize_graph` method
- Adjust animation speed by changing `time.sleep()` values
- Customize node sizes and edge widths

### Algorithm Extension
- Add new algorithms by extending the `GraphVisualizer` class
- Implement custom visualization methods
- Add support for directed graphs

## Educational Value

This tool is perfect for:
- **Computer Science Students**: Understanding graph algorithms visually
- **Algorithm Interviews**: Practicing graph problems with visual feedback
- **Educators**: Teaching graph algorithms with interactive examples
- **Developers**: Debugging graph-based applications

## Contributing

Areas for improvement:
- Add more graph algorithms (A*, Bellman-Ford, Floyd-Warshall)
- Implement graph editing interface
- Add algorithm complexity analysis
- Create web-based version
- Add support for dynamic graphs
- Implement graph metrics and analysis

## Requirements

- Python 3.6+
- matplotlib
- networkx
- numpy

## License

This project is open source and available under the MIT License.
