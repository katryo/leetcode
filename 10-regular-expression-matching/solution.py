"""
https://leetcode.com/problems/regular-expression-matching;

https://leetcode.com/problems/wildcard-matching
"""


class Solution:
    def isMatch(self, s, p):
        # if (s, p) == ('', '') then return True
        # if (s, p) == ('a', '') then return False
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[-1][-1] = True  # dp[len(s)][len(p)] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                # some text, empty pattern, then False
                # empty text, some pattern, then True/False e.g. pattern == '.*' text == '' then True
                is_1st_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (is_1st_match and dp[i+1][j])
                else:
                    dp[i][j] = is_1st_match and dp[i+1][j+1]
        return dp[0][0]

    def isMatchRec(self, s, p):
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                ans = i == len(s)
            else:
                is_1st_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                if j+1 < len(p) and p[j+1] == '*':
                    ans = dp(i, j+2) or (is_1st_match and dp(i+1, j))
                else:
                    ans = is_1st_match and dp(i+1, j+1)
            memo[i, j] = ans
            return ans
        return dp(0, 0)

# s = Solution()
# print(s.isMatch('aa', 'a'))
# print(s.isMatchRec('aa', 'a*'))
# print(s.isMatch('abbbbb', 'ab*'))
# print(s.isMatch('ab', '.*'))
# print(s.isMatch('aab', 'c*a*b'))
# print(s.isMatch('mississippi', 'mis*is*p*'))
# print(s.isMatch('mississippi', 'mis*is*ip*i'))
