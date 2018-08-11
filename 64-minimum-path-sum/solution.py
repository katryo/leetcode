class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return 0

        table = [[-1] * len(grid[0]) for _ in range(len(grid))]

        table[0][0] = grid[0][0]

        for i in range(1, len(grid)):
            table[i][0] = table[i-1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            table[0][j] = table[0][j-1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                table[i][j] = min(table[i-1][j], table[i][j-1]) + grid[i][j]
        return table[len(grid)-1][len(grid[0])-1]

# s = Solution()
# grid = [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# print(s.minPathSum(grid))

