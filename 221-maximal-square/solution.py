class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        table = [0] * len(matrix[0])

        ans = 0
        for j in range(len(matrix[0])):
            if matrix[0][j] == '1':
                table[j] = 1
                ans = 1

        for i in range(1, len(matrix)):
            prev = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    tmp = table[j]
                    if j == 0:
                        table[j] = 1
                    else:
                        table[j] = min(table[j-1], table[j], prev) + 1
                    ans = max(ans, table[j])
                    prev = tmp
                else:
                    prev = table[j]
                    table[j] = 0
        return ans ** 2


if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare([['1', '1'], ['1', '1']]))
    print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(s.maximalSquare([["1", "0", "1", "1", "1"], ["0", "1", "0", "1", "0"], ["1", "1", "0", "1", "1"], ["1", "1", "0", "1", "1"],
     ["0", "1", "1", "1", "1"]]))

    # ["1","0","1","0","0"],
    # ["1","0","1","1","1"],
    # ["1","1","1","1","1"],
    # ["1","0","0","1","0"]

    # [
    # ["1","0","1","1","1"],
    # ["0","1","0","1","0"],
    # ["1","1","0","1","1"],
    # ["1","1","0","1","1"],
    # ["0","1","1","1","1"]]

    # def maximalSquare(self, matrix):
    #     if not matrix or not matrix[0]:
    #         return 0
    #     table = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    #
    #     ans = 0
    #     for j in range(len(matrix[0])):
    #         if matrix[0][j] == '1':
    #             table[0][j] = 1
    #             ans = 1
    #     for i in range(len(matrix)):
    #         if matrix[i][0] == '1':
    #             table[i][0] = 1
    #             ans = 1
    #
    #     for i in range(1, len(matrix)):
    #         for j in range(1, len(matrix[0])):
    #             if matrix[i][j] == '1':
    #                 table[i][j] = min(table[i-1][j], table[i][j-1], table[i-1][j-1]) + 1
    #                 ans = max(ans, table[i][j])
    #     return ans ** 2


    # def maximalSquare(self, matrix):
        # """
        # :type matrix: List[List[str]]
        # :rtype: int
        # """
        # if not matrix or not matrix[0]:
        #     return 0
        # right = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # down = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        #
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0]) - 1, -1, -1):
        #         if matrix[i][j] == '1':
        #             if j == len(matrix[0]) - 1:
        #                 right[i][j] = 1
        #             else:
        #                 right[i][j] = right[i][j + 1] + 1
        #
        # for i in range(len(matrix) - 1, -1, -1):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == '1':
        #             if i == len(matrix) - 1:
        #                 down[i][j] = 1
        #             else:
        #                 down[i][j] = down[i + 1][j] + 1
        #
        # def max_sq_size(r, c):
        #     size = min(down[r][c], right[r][c])
        #     if not size:
        #         return 0
        #     for i in range(1, size):
        #         size = min(size, i + min(down[r + i][c + i], right[r + i][c + i]))
        #     return size
        #
        # retval = 0
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         retval = max(retval, max_sq_size(i, j))
        # return retval ** 2