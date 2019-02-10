class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        if X >= Y:
            return X - Y

        if Y % 2 == 0:
            return self.brokenCalc(X, Y // 2) + 1
        else:
            return self.brokenCalc(X, Y + 1) + 1


# s = Solution()
# print(s.brokenCalc(2, 3))
# print(s.brokenCalc(5, 8))
# print(s.brokenCalc(3, 10))
# print(s.brokenCalc(1024, 1))
# print(s.brokenCalc(10, 19))
# print(s.brokenCalc(10, 21))
