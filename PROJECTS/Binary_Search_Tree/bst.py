"""
Binary Search Tree Implementation with Visualization
Author: AI Assistant
GitHub: https://github.com/fineanmol/hacktoberfest
Language: Python
Description: A comprehensive BST implementation with insertion, deletion, traversal, and visualization
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np


class TreeNode:
    """Node class for Binary Search Tree"""
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class BinarySearchTree:
    """Binary Search Tree implementation with visualization"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert a value into the BST"""
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        """Helper method for insertion"""
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        
        return node
    
    def delete(self, val):
        """Delete a value from the BST"""
        self.root = self._delete(self.root, val)
    
    def _delete(self, node, val):
        """Helper method for deletion"""
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node to be deleted found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children: get inorder successor
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        
        return node
    
    def _min_value_node(self, node):
        """Find the node with minimum value"""
        current = node
        while current.left:
            current = current.left
        return current
    
    def search(self, val):
        """Search for a value in the BST"""
        return self._search(self.root, val)
    
    def _search(self, node, val):
        """Helper method for search"""
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)
    
    def inorder_traversal(self):
        """Inorder traversal of the BST"""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        """Helper method for inorder traversal"""
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)
    
    def preorder_traversal(self):
        """Preorder traversal of the BST"""
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, node, result):
        """Helper method for preorder traversal"""
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
    
    def postorder_traversal(self):
        """Postorder traversal of the BST"""
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, node, result):
        """Helper method for postorder traversal"""
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)
    
    def height(self):
        """Get the height of the BST"""
        return self._height(self.root)
    
    def _height(self, node):
        """Helper method to calculate height"""
        if not node:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def is_balanced(self):
        """Check if the BST is balanced"""
        return self._is_balanced(self.root)
    
    def _is_balanced(self, node):
        """Helper method to check balance"""
        if not node:
            return True
        
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return self._is_balanced(node.left) and self._is_balanced(node.right)
    
    def visualize(self, title="Binary Search Tree"):
        """Visualize the BST using matplotlib"""
        if not self.root:
            print("Tree is empty!")
            return
        
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Calculate positions for all nodes
        positions = self._calculate_positions()
        
        # Draw the tree
        self._draw_tree(ax, self.root, positions, 5, 9, 2)
        
        ax.set_title(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def _calculate_positions(self):
        """Calculate positions for all nodes"""
        positions = {}
        self._assign_positions(self.root, positions, 5, 9, 2)
        return positions
    
    def _assign_positions(self, node, positions, x, y, level_width):
        """Assign positions to nodes"""
        if not node:
            return
        
        positions[node.val] = (x, y)
        
        if node.left:
            self._assign_positions(node.left, positions, 
                                 x - level_width, y - 1, level_width * 0.6)
        if node.right:
            self._assign_positions(node.right, positions, 
                                 x + level_width, y - 1, level_width * 0.6)
    
    def _draw_tree(self, ax, node, positions, x, y, level_width):
        """Draw the tree recursively"""
        if not node:
            return
        
        # Draw current node
        circle = plt.Circle((x, y), 0.3, color='lightblue', ec='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, str(node.val), ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Draw connections to children
        if node.left:
            left_x = x - level_width
            left_y = y - 1
            ax.plot([x, left_x], [y-0.3, left_y+0.3], 'k-', linewidth=2)
            self._draw_tree(ax, node.left, positions, left_x, left_y, level_width * 0.6)
        
        if node.right:
            right_x = x + level_width
            right_y = y - 1
            ax.plot([x, right_x], [y-0.3, right_y+0.3], 'k-', linewidth=2)
            self._draw_tree(ax, node.right, positions, right_x, right_y, level_width * 0.6)


def demo_bst():
    """Demonstrate BST functionality"""
    print("=== Binary Search Tree Demo ===\n")
    
    # Create BST
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    print(f"Inserting values: {values}")
    for val in values:
        bst.insert(val)
    
    # Display traversals
    print(f"\nInorder traversal: {bst.inorder_traversal()}")
    print(f"Preorder traversal: {bst.preorder_traversal()}")
    print(f"Postorder traversal: {bst.postorder_traversal()}")
    
    # Search operations
    search_val = 40
    result = bst.search(search_val)
    print(f"\nSearching for {search_val}: {'Found' if result else 'Not found'}")
    
    # Tree properties
    print(f"\nTree height: {bst.height()}")
    print(f"Is balanced: {bst.is_balanced()}")
    
    # Delete operation
    delete_val = 30
    print(f"\nDeleting {delete_val}...")
    bst.delete(delete_val)
    print(f"Inorder after deletion: {bst.inorder_traversal()}")
    
    # Visualize the tree
    print("\nVisualizing the tree...")
    bst.visualize("Binary Search Tree - Final State")


if __name__ == "__main__":
    demo_bst()
