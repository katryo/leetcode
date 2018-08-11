# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        if not obstacleGrid[0]:
            return 0

        table = [[-1] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        table[0][0] = 1

        def paths(row, col):
            if row < 0 or col < 0 or row >= len(obstacleGrid) or col >= len(obstacleGrid[0]):
                return 0
            if obstacleGrid[row][col]:
                return 0
            if table[row][col] != -1:
                return table[row][col]
            ret = paths(row-1, col) + paths(row, col-1)
            table[row][col] = ret
            return ret

        ans = paths(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        return ans

# s = Solution()
# grid = [
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0],
#     [1, 0, 0]
# ]
# print(s.uniquePathsWithObstacles(grid))

