class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        opener = 0
        closer = 0
        ans = 0

        for s in S:
            if s == '(':
                opener += 1
            else:
                closer += 1
            if closer > opener:
                opener += 1
                ans += 1
        return ans + (opener - closer)


s = Solution()
print(s.minAddToMakeValid(""))
print(s.minAddToMakeValid("())"))
print(s.minAddToMakeValid(")))"))
print(s.minAddToMakeValid("((("))
print(s.minAddToMakeValid("()"))
print(s.minAddToMakeValid("()))(("))


    # def minAddToMakeValid(self, S):
    #     """
    #     :type S: str
    #     :rtype: int
    #     """
    #
    #     length = len(S)
    #     table = [[-1] * length for _ in range(length)]
    #
    #     def helper(i, j):
    #         if i > j:
    #             return 0
    #         if i == j:
    #             return 1
    #         if table[i][j] != -1:
    #             return table[i][j]
    #         if S[i] == '(':
    #             if S[j] == ')':
    #                 inner = helper(i + 1, j - 1)
    #                 table[i][j] = inner
    #             else:
    #                 # (xxxx(
    #                 inner = helper(i + 1, j)
    #                 table[i][j] = inner + 1
    #         else:  # S[i] == ')'
    #             if S[j] == '(':
    #                 inner = helper(i + 1, j - 1)
    #                 table[i][j] = inner + 2
    #             else:  # )xxxx)
    #                 inner = helper(i, j - 1)
    #                 table[i][j] = inner + 1
    #         return table[i][j]
    #
    #     return helper(0, len(S) - 1)