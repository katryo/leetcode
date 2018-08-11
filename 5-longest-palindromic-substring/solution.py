class Solution(object):
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #
    #     if not s:
    #         return ""
    #     if len(s) == 1:
    #         return s
    #
    #     table = [[-1] * len(s) for _ in range(len(s))]
    #
    #     def palindrome_length(left, right):
    #         if left == right:
    #             return 1
    #         if table[left][right] != -1:
    #             return table[left][right]
    #         if s[left] == s[right]:
    #             if left + 1 == right:
    #                 ret = 2
    #             elif palindrome_length(left+1, right-1) == right-left-1:
    #                 ret = 2 + palindrome_length(left+1, right-1)
    #             else:
    #                 ret = max(palindrome_length(left+1, right),
    #                           palindrome_length(left, right-1))
    #         else:
    #             ret = max(palindrome_length(left+1, right),
    #                       palindrome_length(left, right-1))
    #         table[left][right] = ret
    #         return ret
    #
    #     max_length = palindrome_length(0, len(s)-1)
    #     i = 0
    #     j = len(s)-1
    #     while i < j and palindrome_length(i+1, j) == max_length:
    #         i += 1
    #     while i < j and palindrome_length(i, j-1) == max_length:
    #         j -= 1
    #
    #     return s[i:j+1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        def expand(left, right):
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            return s[left:right+1]

        def expand_odd(center):
            return expand(center, center)

        def expand_even(center_left):
            if s[center_left] == s[center_left+1]:
                return expand(center_left, center_left+1)
            else:
                return ""

        ans = s[0]
        for i in range(len(s)-1):
            candidate = expand_odd(i)
            if len(candidate) > len(ans):
                ans = candidate
            candidate_even = expand_even(i)
            if len(candidate_even) > len(ans):
                ans = candidate_even
        return ans


s = Solution()
print(s.longestPalindrome("abcda"))
print(s.longestPalindrome("ac"))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("abcdbcbaw"))

thousand = "z" * 1000
print(s.longestPalindrome(thousand))
