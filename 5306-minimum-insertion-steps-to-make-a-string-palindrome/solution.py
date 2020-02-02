class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        rs = s[::-1]

        dp = [[0] * (n+1) for _ in range(n+1)]

        # dp[i][j]: longest common subsequence of s[0] .. s[i-1] (first i chars), rs[0] .. rs[j-1] (first j chars)

        for i in range(n):
            for j in range(n):
                if s[i] == rs[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return n - dp[n][n]


# s = Solution()
# print(s.minInsertions('mbadm'))
# print(s.minInsertions('leetcode'))
# print(s.minInsertions('g'))
# print(s.minInsertions('no'))
