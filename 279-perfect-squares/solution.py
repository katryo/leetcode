from math import sqrt

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [-1] * (n+1)
        table[1] = 1
        for i in range(2, n+1):
            cand = 1000000000000000
            j = 1
            while i - j**2 >= 0:
                cand = min(cand, table[i - j**2] + 1)
                j += 1
            table[i] = cand
        return table[n]


s = Solution()
print(s.numSquares(1))
print(s.numSquares(2))
print(s.numSquares(3))
print(s.numSquares(4))
print(s.numSquares(12))
print(s.numSquares(6665))
print(s.numSquares(13))
print(s.numSquares(99))
print(s.numSquares(100))
