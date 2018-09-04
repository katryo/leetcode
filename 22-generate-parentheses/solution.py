class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ret = []

        def helper(string, left, right):
            if len(string) == 2*n:
                ret.append(string)
                return
            if left > right:
                helper(string+')', left, right+1)
            if left < n:
                helper(string+'(', left+1, right)

        helper('', 0, 0)
        return ret


# s = Solution()
# print(s.generateParenthesis(3))