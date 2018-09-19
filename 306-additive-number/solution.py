class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def generate_fib(a, b, length):
            fib = a + b
            while len(fib) < length:
                new_b = int(a) + int(b)
                fib += str(new_b)
                a, b = b, new_b
            return fib[:length]

        for i in range(1, len(num) // 3 * 2 + 1):
            for j in range(i+1, len(num) // 3 * 2 + 1):
                first = num[:i]
                second = num[i:j]
                if len(first) > 1 and first[0] == '0' or len(second) > 1 and second[0] == '0':
                    continue
                fib = generate_fib(first, second, len(num))
                if fib == num:
                    return True
        return False


# s = Solution()
# print(s.isAdditiveNumber('199100199'))
# print(s.isAdditiveNumber('112358'))
# print(s.isAdditiveNumber('1123589'))
# print(s.isAdditiveNumber('123'))
# print(s.isAdditiveNumber("1023"))
# print(s.isAdditiveNumber("101"))
# print(s.isAdditiveNumber("19910011992"))
# print(s.isAdditiveNumber("199111992"))

