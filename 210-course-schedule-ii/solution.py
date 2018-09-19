import collections

class Solution:
    def findOrder(self, numCourses, prerequisites):
        inbounds = collections.defaultdict(set)
        outbounds = collections.defaultdict(set)

        for pair in prerequisites:
            inbounds[pair[0]].add(pair[1])
            outbounds[pair[1]].add(pair[0])

        noinbounds = [num for num in range(numCourses) if not inbounds[num]]

        ans = []
        while noinbounds:
            removed = noinbounds.pop()
            ans.append(removed)
            for child in outbounds[removed]:
                inbounds[child].remove(removed)
                if not inbounds[child]:
                    noinbounds.append(child)
            outbounds.pop(removed)
        if len(ans) == numCourses:
            return ans
        return []




    # def findOrder(self, numCourses, prerequisites):
        # """
        # :type numCourses: int
        # :type prerequisites: List[List[int]]
        # :rtype: List[int]
        # """
        #
        # outbound = defaultdict(list)
        # inbound = defaultdict(list)
        # for pre in prerequisites:
        #     inbound[pre[0]].append(pre[1])
        #     outbound[pre[1]].append(pre[0])
        #
        # nodes = {n for n in range(numCourses)}
        #
        # def dfs_noinbound():
        #     node = next(iter(nodes))
        #     visited = {node}
        #     while node in inbound and inbound[node]:
        #         node = inbound[node][0]
        #         if node in visited:
        #             return None
        #         visited.add(node)
        #     if node in outbound:
        #         children = outbound[node]
        #         for child in children:
        #             inbound[child].remove(node)
        #             if not inbound[child]:
        #                 del inbound[child]
        #         del outbound[node]
        #     nodes.remove(node)
        #     return node
        #
        #     # returns the node with no inbound edge
        #     # If is has a loop, return None
        #
        # ans = []
        # while nodes:
        #     noinbound = dfs_noinbound()
        #     if noinbound is None:
        #         return []
        #     ans.append(noinbound)
        # return ans


s = Solution()
print(s.findOrder(2, [[1,0]]))
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
