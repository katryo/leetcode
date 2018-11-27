from collections import defaultdict

class DSU:
    def __init__(self, size):
        self.parents = list(range(size))

    def union(self, a, b):
        # If we have time, reimplement it in a better way
        a_parent = self.find(a)
        b_parent = self.find(b)

        self.parents[a_parent] = b_parent

    def find(self, idx):
        parent = self.parents[idx]
        if parent == idx:
            return idx
        result = self.find(parent)
        self.parents[idx] = result
        return result


class Solution:
    def removeStones(self, stones):
        dsu = DSU(20000)

        for row, col in stones:
            dsu.union(row, col+10000)

        islands = len({dsu.find(row) for row, col in stones })
        return len(stones)-islands


s = Solution()
print(s.removeStones([[0,0], [0,2],[2,0],[1, 1]]))