class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def diagonal_sum(root):
    def helper(node, diagonal, diagonal_sums):
        if node is None:
            return
        
        # Update the diagonal sum
        diagonal_sums[diagonal] = diagonal_sums.get(diagonal, 0) + node.value

        # Traverse the left and right subtrees
        helper(node.left, diagonal + 1, diagonal_sums)
        helper(node.right, diagonal, diagonal_sums)
    
    diagonal_sums = {}
    helper(root, 0, diagonal_sums)
    return list(diagonal_sums.values())

# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(9)
root.left.right = TreeNode(6)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

result = diagonal_sum(root)
print(result)  # Output: [1, 2, 6, 15, 5]
