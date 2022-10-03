// BREADTH FIRST SEARCH 

Breadth-first search is a graph traversal algorithm that starts traversing the graph from the root node and explores all the neighboring nodes. Then, it selects the nearest node and explores all the unexplored nodes. While using BFS for traversal, any node in the graph can be considered as the root node.

Implementation of BFS traversal:
Follow the below method to implement BFS traversal.

Declare a queue and insert the starting vertex.
Initialize a visited array and mark the starting vertex as visited.
Follow the below process till the queue becomes empty:
Remove the first vertex of the queue.
Mark that vertex as visited.
Insert all the unvisited neighbours of the vertex into the queue.



