from collections import defaultdict


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        colors = {}
        RED = 0
        BLUE = 1

        graph = defaultdict(set)
        for dislike in dislikes:
            graph[dislike[0]].add(dislike[1])
            graph[dislike[1]].add(dislike[0])

        # Returns it is a b-graph
        def dfs(node, color):
            if node in colors:
                return colors[node] == color
            colors[node] = color
            return all(dfs(child, color ^ 1) for child in graph[node])

        for num in range(1, N + 1):
            if num in colors:
                continue
            if not dfs(num, RED):
                return False
        return True

#
# s = Solution()
# print(s.possibleBipartition(4, [[1,2],[1,3],[2,4]]))
# print(s.possibleBipartition(3, [[1,2],[1,3],[2,3]]))
# print(s.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))

