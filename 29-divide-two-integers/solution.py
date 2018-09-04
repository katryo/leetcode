class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        nagated = False
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        if dividend < 0:
            dividend = -dividend
            nagated = True
        if divisor < 0:
            divisor = -divisor
            nagated = True

        sub = divisor
        quo = 0
        times = 1
        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub
                quo += times
                sub <<= 1
                times <<= 1
            else:
                sub >>= 1
                times >>= 1
        if nagated:
            quo = - quo
        return min(max(-2147483648, quo), 2147483647)


# s = Solution()
# print(s.divide(10, 3))
# print(s.divide(10, -3))
# print(s.divide(-10, 3))
# print(s.divide(-10, -3))
