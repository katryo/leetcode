from copy import deepcopy


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not n:
            return -1
        m = len(grid[0])
        if not m:
            return -1
        turn = 0
        while True:
            next_grid = deepcopy(grid)
            has_fresh = False

            # Scan the grid
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        has_fresh = True
                    if grid[i][j] == 2:
                        # For each turn, update the grid.
                        if 0 < i and grid[i - 1][j] == 1:
                            next_grid[i - 1][j] = 2
                        if i < n - 1 and grid[i + 1][j] == 1:
                            next_grid[i + 1][j] = 2
                        if 0 < j and grid[i][j - 1] == 1:
                            next_grid[i][j - 1] = 2
                        if j < m - 1 and grid[i][j + 1] == 1:
                            next_grid[i][j + 1] = 2
            # If there is no fresh orange, returns the minutes
            if not has_fresh:
                return turn

            is_next_different = False
            for i in range(n):
                for j in range(m):
                    if grid[i][j] != next_grid[i][j]:
                        is_next_different = True
                    # If there is no update, returns -1
            if not is_next_different:
                return -1
            turn += 1
            grid = next_grid

