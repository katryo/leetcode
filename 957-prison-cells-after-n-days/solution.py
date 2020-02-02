from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cache = {}
        cache[tuple(cells)] = 0

        num_tup = {}
        num_tup[0] = tuple(cells)
        for j in range(1, N+1):
            future = [0] * 8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    future[i] = 1
            cells = future
            t_cells = tuple(cells)
            if t_cells in cache:
                prev = cache[t_cells]
                cur = j
                rest = (N - prev) % (cur - prev)
                return list(num_tup[rest + prev])

            cache[t_cells] = j
            num_tup[j] = t_cells
        return cells


# s = Solution()
# print(s.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))
# print(s.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0],  1000000000))
