from collections import deque, defaultdict


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        RED = -1
        BLUE = 1

        red_graph = defaultdict(set)
        for src, dst in red_edges:
            red_graph[src].add(dst)

        blue_graph = defaultdict(set)
        for src, dst in blue_edges:
            blue_graph[src].add(dst)

        graph = {RED: red_graph, BLUE: blue_graph}

        def bfs(first):
            q = deque()
            q.append((0, first, 0))
            seen = {RED: set(), BLUE: set()}
            ret = [float('inf')] * n
            while q:
                cur, color, length = q.popleft()
                if cur in seen[color]:
                    continue
                seen[color].add(cur)
                ret[cur] = min(ret[cur], length)
                c_graph = graph[color]
                for child in c_graph[cur]:
                    q.append((child, -color, length + 1))
            return ret

        red_shortest = bfs(RED)
        # print('red', red_shortest)
        blue_shortest = bfs(BLUE)
        # print('blue', blue_shortest)

        ans = [0] * n

        for i in range(n):
            ans[i] = min(red_shortest[i], blue_shortest[i])
            if ans[i] == float('inf'):
                ans[i] = -1
        return ans