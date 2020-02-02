from typing import List
import collections


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        seen = set()

        q = collections.deque()
        q.append((0, 0, 0, 0))

        def next_loc(ii, jj, q, score):
            is_obs = grid[ii][jj]
            if is_obs:
                q.append((ii, jj, c+1, score+1))
            else:
                q.append((ii, jj, c, score+1))

        while q:
            i, j, c, score = q.popleft()

            if c > k:
                continue
            if i == n-1 and j == m-1:
                return score
            if (i, j, c) in seen:
                continue
            seen.add((i, j, c))

            if 0 < i:
                next_loc(i-1, j, q, score)
            if i < n-1:
                next_loc(i+1, j, q, score)
            if 0 < j:
                next_loc(i, j-1, q, score)
            if j < m-1:
                next_loc(i, j+1, q, score)

        return -1

# s = Solution()
# print(s.shortestPath(
# [[0,0,0],
#  [1,1,0],
#  [0,0,0],
#  [0,1,1],
#  [0,0,0]], 1))
# print(s.shortestPath(
#     [[0, 1, 1],
#      [1, 1, 1],
#      [1, 0, 0]],
#     1
# ))
# print(s.shortestPath(
#     [[0,1,0,0,0,1,0,0],
#      [0,1,0,1,0,1,0,1],
#      [0,0,0,1,0,0,1,0]],
# 1))
