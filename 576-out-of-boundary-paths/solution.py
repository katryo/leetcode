# https://leetcode.com/problems/out-of-boundary-paths/discuss/102993/Python-Straightforward-with-Explanation


class Solution:
    def findPaths(self, m, n, N, i, j):
        table = [[0] * n for _ in range(m)]
        table[i][j] = 1

        ans = 0
        MOD = 10 ** 9 + 7
        for _ in range(N):
            new_table = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if -1 < nr < m and -1 < nc < n:
                            new_table[nr][nc] += table[r][c]
                            new_table[nr][nc] %= MOD
                        else:
                            ans += table[r][c]
                            ans %= MOD
            table = new_table
        return ans


s = Solution()
print(s.findPaths(1, 3, 3, 0, 1))


    # def findPaths(self, m, n, N, i, j):
    #     """
    #     :type m: int
    #     :type n: int
    #     :type N: int
    #     :type i: int
    #     :type j: int
    #     :rtype: int
    #     """
    #
    #     if m == 1 and n == 1:
    #         if N > 0:
    #             return 4
    #         else:
    #             return 0
    #     if N == 0:
    #         return 0
    #     I = i
    #     J = j
    #     table = [[-1] * n for _ in range(m)]
    #
    #     for i in range(m):
    #         for j in range(n):
    #             count = 0
    #             if i == 0:
    #                 count += 1
    #             if i == m - 1:
    #                 count += 1
    #             if j == 0:
    #                 count += 1
    #             if j == n - 1:
    #                 count += 1
    #             table[i][j] = count
    #
    #     ans = table[I][J]
    #     for _ in range(2, N + 1):
    #         new_table = [[-1] * n for _ in range(m)]
    #         for i in range(m):
    #             for j in range(n):
    #                 new_table[i][j] = 0
    #                 if i > 0:
    #                     new_table[i][j] += table[i - 1][j]
    #                 if i < m - 1:
    #                     new_table[i][j] += table[i + 1][j]
    #                 if j > 0:
    #                     new_table[i][j] += table[i][j - 1]
    #                 if j < n - 1:
    #                     new_table[i][j] += table[i][j + 1]
    #                 new_table[i][j] %= (10 ** 9 + 7)
    #         table = new_table
    #         ans += table[I][J]
    #         ans %= (10 ** 9 + 7)
    #
    #     return ans