class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_len = len(s)
        t_len = len(t)
        table = [[0] * (s_len+1) for _ in range(t_len+1)]
        for j in range(s_len):
            table[0][j] = 1

        fact_memo = {0: 1}

        def factorial(a):
            if a in fact_memo:
                return fact_memo[a]
            ans = factorial(a-1) * a
            fact_memo[a] = ans
            return ans

        for T in range(1, t_len+1):
            for S in range(1, s_len+1):
                if s[S-1] == t[T-1]:
                    table[T][S] = table[T-1][S-1] + table[T][S-1]
                else:
                    table[T][S] = table[T][S-1]

        return table[t_len][s_len]


# s = Solution()
# print(s.numDistinct("rabbbit", "rabbit"))
# print(s.numDistinct("babgbag", "bag"))
