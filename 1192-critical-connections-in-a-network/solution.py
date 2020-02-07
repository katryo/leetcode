from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for src, dest in connections:
            graph[src].add(dest)
            graph[dest].add(src)

        lowest = [0] * n
        seen = set()
        ans = []

        def dfs(rank, prev_vtx, cur_vtx):
            seen.add(cur_vtx)
            lowest[cur_vtx] = rank

            for child in graph[cur_vtx]:
                if child == prev_vtx:
                    continue
                if child not in seen:
                    dfs(rank+1, cur_vtx, child)
                if lowest[child] == rank + 1:
                    ans.append([cur_vtx, child])
                lowest[cur_vtx] = min(lowest[cur_vtx], lowest[child])
            return lowest

        dfs(0, -1, 0)
        return ans


s = Solution()
print(s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
