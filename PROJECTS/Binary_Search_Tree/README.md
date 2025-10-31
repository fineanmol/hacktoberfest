# Binary Search Tree Implementation

A comprehensive Binary Search Tree (BST) implementation in Python with visualization capabilities.

## Features

- **Core BST Operations**: Insert, Delete, Search
- **Tree Traversals**: Inorder, Preorder, Postorder
- **Tree Analysis**: Height calculation, Balance checking
- **Visualization**: Interactive tree visualization using matplotlib
- **Educational**: Well-documented code with examples

## Usage

```python
from bst import BinarySearchTree

# Create a new BST
bst = BinarySearchTree()

# Insert values
bst.insert(50)
bst.insert(30)
bst.insert(70)

# Search for a value
result = bst.search(30)

# Get traversals
inorder = bst.inorder_traversal()
preorder = bst.preorder_traversal()
postorder = bst.postorder_traversal()

# Visualize the tree
bst.visualize()
```

## Requirements

- Python 3.6+
- matplotlib
- numpy

## Installation

```bash
pip install matplotlib numpy
```

## Algorithm Complexity

- **Insert**: O(log n) average, O(n) worst case
- **Delete**: O(log n) average, O(n) worst case  
- **Search**: O(log n) average, O(n) worst case
- **Traversal**: O(n)

## Contributing

This project is part of Hacktoberfest contributions. Feel free to:
- Add more tree algorithms (AVL, Red-Black)
- Implement iterative versions of operations
- Add more visualization features
- Improve the UI/UX

## License

This project is open source and available under the MIT License.
