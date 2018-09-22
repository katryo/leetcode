from collections import defaultdict
from collections import deque


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # graph = { 'a': {'b': 2.0, 'c': 6.0} }
        graph = defaultdict(dict)
        for equation, value in zip(equations, values):
            graph[equation[0]][equation[0]] = 1.0
            graph[equation[1]][equation[1]] = 1.0
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1 / value

        for start in graph:
            for end in graph[start]:
                for end2 in graph[start]:
                    graph[end][end2] = graph[end][start] * graph[start][end2]
        return [graph[start].get(end, -1) for start, end in queries]


class Solution2:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # graph = { 'a': [('b', 2.0), ('c', 6.0)]}
        graph = defaultdict(dict)
        for equation, value in zip(equations, values):
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1 / value

        def bfs(begin, goal):
            if begin not in graph or goal not in graph:
                return -1.0
            if goal in graph[begin]:
                return graph[begin][goal]
            seen = {begin}
            val = 1.0
            queue = deque()
            queue.insert(0, (begin, 1.0))
            while queue:
                node, v = queue.pop()
                if node == goal:
                    return v
                for child in graph[node]:
                    if child in seen:
                        continue
                    val = graph[node][child]
                    seen.add(child)
                    graph[begin][child] = v * val
                    queue.insert(0, (child, v * val))
            return -1.0

        ans = []
        for start, end in queries:
            ans.append(bfs(start, end))
        return ans