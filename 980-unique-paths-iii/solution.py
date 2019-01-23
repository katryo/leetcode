class Solution:
    def __init__(self):
        self.g = None
        self.counter = 0

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.g = grid
        a, b, x, y = -1, -1, -1, -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    a, b = i, j
                elif grid[i][j] == 0:
                    self.counter += 1
        self.counter += 1 # for 1
        return self.rec(a, b)

    def rec(self, a, b):
        if self.g[a][b] == 2:
            if self.counter == 0:
                return 1
            else:
                return 0

        ans = 0

        self.counter -= 1
        self.g[a][b] = -1
        if a > 0 and self.g[a-1][b] != -1:
            ans += self.rec(a-1, b)
        if a < len(self.g)-1 and self.g[a+1][b] != -1:
            ans += self.rec(a+1, b)
        if b > 0 and self.g[a][b-1] != -1:
            ans += self.rec(a, b-1)
        if b < len(self.g[0])-1 and self.g[a][b+1] != -1:
            ans += self.rec(a, b+1)
        self.g[a][b] = 0
        self.counter += 1
        return ans


# s = Solution()
# g = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# g = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# g = [[0,1],[2,0]]
# g = [[1,0,0,2]]
# print(s.uniquePathsIII(g))
