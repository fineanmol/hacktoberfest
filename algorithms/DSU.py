class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # used for union by rank

    def find(self, x):
        # Path compression optimization
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank optimization
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # already connected

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

# Example usage:
uf = UnionFind(6)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print(uf.find(0), uf.find(2))  # same group
print(uf.find(3), uf.find(5))  # different groups
