import sys


class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        1 2 3 4 5 6 7 8 9 10
        """

        dp = [[-1 for _ in range(n+2)] for _ in range(n+2)]
        # dp[i][j]: required money given [i:j+1]
        # e.g. dp[5][7] => money given [5, 6, 7]
        # dp[1][n] is our goal

        for i in range(n-1, 0, -1):
            for j in range(i+1, n+2):  # i < j
                if i + 1 == j:
                    dp[i][j] = 0
                    continue
                if i + 2 == j:
                    dp[i][j] = i
                    continue
                # i < k < j
                min_v = sys.maxsize
                for k in range(i+1, j-1):
                    v = k + max(dp[i][k], dp[k+1][j])
                    min_v = min(min_v, v)
                dp[i][j] = min_v
        return dp[1][n+1]


if __name__ == '__main__':
    s = Solution()
    print(s.getMoneyAmount(7))
    print(s.getMoneyAmount(10))
    print(s.getMoneyAmount(4))
    print(s.getMoneyAmount(5))
