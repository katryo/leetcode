class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # I 1
        # V 5
        # X 10
        # L 50
        # C 100
        # D 500
        # M 1000

        ans = []
        for large, largec, middle, middlec, small, smallc in ((1000, 'M', 500, 'D', 100, 'C'),
                                                              (100, 'C', 50, 'L', 10, 'X'),
                                                              (10, 'X', 5, 'V', 1, 'I')):
            times, num = divmod(num, large)
            ans += [largec] * times

            if num >= large-small:
                ans += smallc + largec
                num -= large-small

            if num >= middle:
                ans += middlec
                num -= middle

            if num >= middle-small:
                ans += smallc + middlec
                num -= middle-small
        ans += ['I'] * num
        return ''.join(ans)


# s = Solution()
# print(s.intToRoman(3))
# print(s.intToRoman(4))
# print(s.intToRoman(9))
# print(s.intToRoman(58))
# print(s.intToRoman(1994))
#
#




