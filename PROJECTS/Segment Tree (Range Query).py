class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.n = n
        self.tree = [0] * (2 * n)
        # Build tree
        for i in range(n):
            self.tree[n + i] = data[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos >>= 1
            self.tree[pos] = self.tree[pos << 1] + self.tree[pos << 1 | 1]

    def query(self, left, right):
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left & 1:
                result += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                result += self.tree[right]
            left >>= 1
            right >>= 1
        return result

# Example
data = [1,3,5,7,9,11]
st = SegmentTree(data)
print(st.query(1,4))  # Output: 15 (3+5+7)
st.update(1, 10)
print(st.query(1,4))  # Output: 22 (10+5+7)
