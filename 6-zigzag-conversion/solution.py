from itertools import chain


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = [[] for _ in range(min(len(s), numRows))]

        r = 0
        DOWN = 0
        UP = 1
        di = DOWN
        for char in s:
            rows[r].append(char)
            if r == numRows-1:
                di = UP
            elif r == 0:
                di = DOWN
            if di == UP:
                r -= 1
            elif di == DOWN:
                r += 1


        anslist = []

        for row in rows:
            anslist += row

        return ''.join(anslist)




s = Solution()
# print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 1))
