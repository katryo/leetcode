class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return n

        def left_to_right(m):
            if m <= 2:
                return m
            return right_to_left(m // 2) * 2

        def right_to_left(m):
            if m == 1:
                return 1
            if m == 2:
                return 1
            if m % 2:
                return left_to_right(m // 2) * 2
            else:
                return left_to_right(m // 2) * 2 - 1

        return left_to_right(n)


s = Solution()
print(s.lastRemaining(9))
