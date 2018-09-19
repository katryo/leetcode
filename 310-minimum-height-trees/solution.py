from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n, edges):
        if not edges:
            return [n-1]
        children = defaultdict(list)
        degrees = defaultdict(int)
        for edge in edges:
            children[edge[0]].append(edge[1])
            children[edge[1]].append(edge[0])
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1

        noincomings = []
        unvisited = set(range(n))
        for i in range(n):
            if degrees[i] == 1:
                noincomings.append(i)

        while len(unvisited) > 2:
            next_noincomings = []
            for node in noincomings:
                unvisited.remove(node)
                for child in children[node]:
                    if child in unvisited:
                        degrees[child] -= 1
                        if degrees[child] == 1:
                            next_noincomings.append(child)
            noincomings = next_noincomings
        return list(unvisited)

    # def findMinHeightTrees(self, n, edges):
    #     """
    #     :type n: int
    #     :type edges: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     if not edges:
    #         return [n - 1]
    #     children = defaultdict(list)
    #     for edge in edges:
    #         children[edge[0]].append(edge[1])
    #         children[edge[1]].append(edge[0])
    #
    #     noincomings = []
    #     for parent in children:
    #         if len(children[parent]) == 1:
    #             noincomings.append((parent, 0))
    #
    #     ans = []
    #     cur_depth = -1
    #     while noincomings:
    #         cur, depth = noincomings.pop()
    #         if depth == cur_depth:
    #             ans.append(cur)
    #         elif depth > cur_depth:
    #             cur_depth = depth
    #             ans = [cur]
    #         for child in children[cur]:
    #             children[child].remove(cur)
    #             if len(children[child]) == 1:
    #                 noincomings.insert(0, (child, depth+1))
    #         children.pop(cur)
    #     return ans


s = Solution()
print(s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(s.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
