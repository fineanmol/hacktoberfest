from collections import deque

# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def bottomView(self, root):
        if not root:
            return []

        # Queue stores pairs: (node, horizontal_distance)
        q = deque([(root, 0)])
        hd_map = {}  # hd -> node value

        while q:
            node, hd = q.popleft()
            # For bottom view, we overwrite previous values
            hd_map[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        # Sort by horizontal distance
        return [hd_map[k] for k in sorted(hd_map)]
