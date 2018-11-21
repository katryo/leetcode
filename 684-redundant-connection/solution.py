# https://leetcode.com/problems/redundant-connection/solution/
# https://leetcode.com/problems/redundant-connection/discuss/108002/Unicode-Find-(5-short-lines)
from collections import defaultdict

class DSU:
    def __init__(self):
        self.parents = list(range(1001))
        self.ranks = [0] * 1001

    def find(self, target):
        if self.parents[target] != target:
            ret = self.find(self.parents[target])
            self.parents[target] = ret
            return ret
        return target

    # Return True if already united
    def union(self, a, b):
        ar = self.find(a)
        br = self.find(b)
        if ar == br:
            return True

        if self.ranks[ar] > self.ranks[br]:
            self.parents[br] = ar
        elif self.ranks[ar] < self.ranks[br]:
            self.parents[ar] = br
        else:
            self.parents[br] = ar
            self.ranks[ar] += 1
        return False


class Solution:
    def findRedundantConnection(self, edges):
        tree = ''.join(map(chr, range(1001)))
        ans = [1, 2]
        for u, v in edges:
            if tree[u] == tree[v]:
                ans = [u, v]
            tree = tree.replace(tree[u], tree[v])
        return ans

    # def findRedundantConnection(self, edges):
    #     dsu = DSU()
    #     ans = []
    #     for edge in edges:
    #         if dsu.union(edge[0], edge[1]):
    #             ans = [edge[0], edge[1]]
    #     return ans

    # def findRedundantConnection(self, edges):
    #
    #     graph = defaultdict(set)
    #
    #     # Returns true is it finds a cycle
    #     def dfs(source, target):
    #         if source not in seen:
    #             seen.add(source)
    #             if source == target:
    #                 return True
    #             return any(dfs(nei, target) for nei in graph[source])
    #
    #
    #     ans = [1, 2]
    #     for u, v in edges:
    #         seen = set()
    #         if u in graph and v in graph:
    #             if dfs(u, v):
    #                 ans = [u, v]
    #         graph[u].add(v)
    #         graph[v].add(u)
    #     return ans



    # def findRedundantConnection(self, edges):
    #     """
    #     :type edges: List[List[int]]
    #     :rtype: List[int]
    #     """
    #
    #     graph = defaultdict(list)
    #     for edge in edges:
    #         graph[edge[0]].append(edge[1])
    #         graph[edge[1]].append(edge[0])
    #
    #     visited = {1}
    #
    #     def dfs(node, path, prev):
    #         path.append(node)
    #         for nei in graph[node]:
    #             if path == [] or nei != prev:
    #                 if nei in visited:
    #                     return path + [nei]
    #                 visited.add(nei)
    #                 result = dfs(nei, path, node)
    #                 if result:
    #                     return result
    #         path.pop()
    #         return []
    #
    #     cycle_with_tail = dfs(1, [], 0)
    #     last_num = cycle_with_tail[-1]
    #     cycle = cycle_with_tail[cycle_with_tail.index(last_num):]
    #
    #     ans = [1, 2]
    #     for edge in edges:
    #         for i in range(len(cycle)-1):
    #             node_a = cycle[i]
    #             node_b = cycle[i+1]
    #             if node_a > node_b:
    #                 node_a, node_b = node_b, node_a
    #             if node_a == edge[0] and node_b == edge[1]:
    #                 ans = [edge[0], edge[1]]
    #
    #     return ans


s = Solution()
print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
print(s.findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]))
