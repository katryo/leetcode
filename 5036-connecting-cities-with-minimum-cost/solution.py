from typing import List
from collections import defaultdict


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        parents = list(range(N))
        cost_conns = [(item[2], item[0]-1, item[1]-1) for item in connections]
        cost_conns.sort()

        def get_root_and_path(a):
            path = []
            while parents[a] != a:
                path.append(a)
                a = parents[a]
            path.append(a)
            return path

        def merge(a, b):
            a_root_path = get_root_and_path(a)
            b_root_path = get_root_and_path(b)

            root = a_root_path[-1]
            for p in a_root_path:
                parents[p] = root
            for p in b_root_path:
                parents[p] = root

        ans = 0
        for cost_conn in cost_conns:
            cost, a, b = cost_conn
            if get_root_and_path(a)[-1] == get_root_and_path(b)[-1]:
                continue
            ans += cost
            merge(a, b)

        root = get_root_and_path(0)[-1]
        for i in range(N):
            if get_root_and_path(i)[-1] != root:
                return -1
        return ans


# s = Solution()
# print(s.minimumCost(4, [[1,2,3],[3,4,4]]))
