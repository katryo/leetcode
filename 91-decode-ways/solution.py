class Solution(object):
    def numDecodings(self, s):
        if not s:
            return 0
        prev = 1
        prevprev = 0
        for i in range(1, len(s)+1):
            cur = 0
            if s[i-1] != '0':
                cur += prev
            two_digits = s[i-2:i]
            if i > 1 and '09' < two_digits < '27':
                cur += prevprev
            prevprev = prev
            prev = cur
        return prev


s = Solution()
print(s.numDecodings("142"))
