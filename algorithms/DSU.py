class UnionFind:
    """Optimized Union-Find (Disjoint Set Union) with path compression and union by rank."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # optional: track number of disjoint sets

    def find(self, x: int) -> int:
        """Find the representative (root) of the set containing x with path compression."""
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        # Path compression (flatten tree)
        while x != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x: int, y: int) -> bool:
        """Union two sets by rank. Returns True if merged, False if already in the same set."""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        # Attach smaller rank tree under larger one
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1  # maintain number of connected components
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if two elements belong to the same set."""
        return self.find(x) == self.find(y)

    def size(self) -> int:
        """Return the number of disjoint sets."""
        return self.count


# Example usage
if __name__ == "__main__":
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    print(uf.connected(0, 2))  # True
    print(uf.connected(3, 5))  # False
    print("Number of sets:", uf.size())
