# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        graph = {}

        def helper(cur):
            new_cur = UndirectedGraphNode(cur.label)

            for nei in cur.neighbors:
                clone_nei = UndirectedGraphNode(nei.label)
                clone_cur.neighbors.append(clone_nei)
                if not nei in visited:
                    helper(nei, clone_nei)

        return helper(node)


# nodem1 = UndirectedGraphNode(-1)
# node1 = UndirectedGraphNode(1)
# nodem1.neighbors.append(node1)
#
# s = Solution()
#
# clonedm1 = s.cloneGraph(nodem1)
#
# print(clonedm1.label)
# print(clonedm1.neighbors)
# print(clonedm1.neighbors[0].label)

a = input()

print(a)