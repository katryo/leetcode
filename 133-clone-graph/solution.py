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
        new_graph = {}

        def clone_dfs(nd):  # 2
            new_node = UndirectedGraphNode(nd.label)
            new_graph[nd.label] = new_node
            for nei in nd.neighbors:
                if nei.label in new_graph:
                    new_node.neighbors.append(new_graph[nei.label])
                else:
                    new_nei = clone_dfs(nei)
                    new_node.neighbors.append(new_nei)
            return new_node

        new_root = clone_dfs(node)
        return new_root


nodem1 = UndirectedGraphNode(-1)
node1 = UndirectedGraphNode(1)
nodem1.neighbors.append(node1)

s = Solution()

clonedm1 = s.cloneGraph(nodem1)

print(clonedm1.label)
print(clonedm1.neighbors)
print(clonedm1.neighbors[0].label)

