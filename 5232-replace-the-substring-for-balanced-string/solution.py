class Solution:
    def balancedString(self, s: str) -> int:
        counter = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        n = len(s)
        quarter = n // 4

        for c in s:
            counter[c] += 1

        def balanced():
            for target in 'QWER':
                if counter[target] > quarter:
                    return False
            return True

        if balanced():
            return 0

        n = len(s)
        left = 0
        min_len = n
        for right in range(n):
            counter[s[right]] -= 1
            while balanced():
                min_len = min(min_len, (right - left + 1))
                counter[s[left]] += 1
                left += 1
        return min_len


# s = Solution()
# print(s.balancedString('WWEQERQWQWWRWWERQWEQ'))
#
# print(s.balancedString('QWER'))
# print(s.balancedString('QQWE'))
# print(s.balancedString('QQQW'))
# print(s.balancedString('QQQQ'))



