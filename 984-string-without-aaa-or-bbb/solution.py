class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        total = A + B
        ans = []
        while len(ans) < total and A and B:
            if len(ans) > 1 and ans[-2] == ans[-1] == 'b':
                ans.append('a')
                A -= 1
            elif len(ans) > 1 and ans[-2] == ans[-1] == 'a':
                ans.append('b')
                B -= 1
            elif A > B:
                ans.append('a')
                A -= 1
            else:
                ans.append('b')
                B -= 1
        while A:
            ans.append('a')
            A -= 1
        while B:
            ans.append('b')
            B -= 1
        return ''.join(ans)


# s = Solution()
# print(s.strWithout3a3b(2, 6))
