class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        up_matrix = [[0] * (n+1) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0:
                        up_matrix[i][j] = 1
                    else:
                        up_matrix[i][j] = up_matrix[i-1][j]+1

        for row in up_matrix:
            print(row)

        # area_matrix = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            stack = [-1]

            for j in range(n+1):
                while stack and up_matrix[i][stack[-1]] > up_matrix[i][j]:
                    idx = stack.pop()
                    height = up_matrix[i][idx]
                    width = j - stack[-1] - 1
                    ans = max(ans, height * width)
                stack.append(j)
        return ans


# s = Solution()
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# print(s.maximalRectangle(matrix))


