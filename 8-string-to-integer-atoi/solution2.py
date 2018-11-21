class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        start = -1
        is_minus = False
        starts_with_special = False
        for i, char in enumerate(str):
            if char == '+':
                if starts_with_special:
                    return 0
                starts_with_special = True
                continue
            if char == '-':
                if starts_with_special:
                    return 0
                starts_with_special = True
                is_minus = True
                continue
            if char.isnumeric():
                start = i
                break
            if char == ' ':
                if starts_with_special:
                    return 0
                continue
            else:
                return 0
        if start == -1:
            return 0

        idx = start
        ans = 0

        while True:
            ans *= 10
            ans += int(str[idx])
            idx += 1
            if idx >= len(str):
                break
            if not str[idx].isnumeric():
                break

        if is_minus:
            ans = -ans
            if ans < - 2**31:
                return - 2**31
            else:
                return ans
        else:
            if ans > 2**31-1:
                return 2**31-1
            else:
                return ans


# s = Solution()
# print(s.myAtoi("+1"))
# print(s.myAtoi("++1"))
# print(s.myAtoi("+-1"))
# print(s.myAtoi("0-1"))
# print(s.myAtoi("   00012"))
# print(s.myAtoi("42"))
# print(s.myAtoi("   -42"))
# print(s.myAtoi("4193 with words"))
# print(s.myAtoi("words and 987"))
# print(s.myAtoi("-91283472332"))
# print(s.myAtoi("1091283472332"))
