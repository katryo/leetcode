from typing import List
from collections import defaultdict


class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def rc_to_up_left(r, c):
            left_bottom = False
            if r > c:
                r, c = c, r
                left_bottom = True
            assert r <= c
            col = c - r

            if left_bottom:
                return col
            else:
                return col + N

        def rc_to_up_right(r, c):
            return r + c

        search_table = defaultdict(set)

        c_for_r = defaultdict(int)
        r_for_c = defaultdict(int)
        up_left = defaultdict(int)
        up_right = defaultdict(int)

        for lamp in lamps:
            row, col = lamp[0], lamp[1]
            c_for_r[row] += 1
            r_for_c[col] += 1
            up_left[rc_to_up_left(row, col)] += 1
            up_right[rc_to_up_right(row, col)] += 1
            search_table[row].add(col)

        ans = []
        for q in queries:
            r, c = q[0], q[1]
            if c_for_r[r] > 0 or r_for_c[c] > 0 or up_left[rc_to_up_left(r, c)] > 0 or up_right[rc_to_up_right(r, c)] > 0:
                ans.append(1)
            else:
                ans.append(0)

            for r_del in range(r-1, r+1):
                for c_del in range(c-1, c+1):
                    if c_del < 0 or c_del > N or r_del < 0 or r_del > N:
                        continue
                    if c_del in search_table[r_del]:
                        search_table[r_del].remove(c_del)
                        c_for_r[r_del] -= 1
                        r_for_c[c_del] -= 1
                        up_left[rc_to_up_left(r_del, c_del)] -= 1
                        up_right[rc_to_up_right(r_del, c_del)] -= 1
        return ans


# s = Solution()
# print(s.gridIllumination(5, [[0, 0], [4, 4]], [[1, 1], [1, 0]]))
