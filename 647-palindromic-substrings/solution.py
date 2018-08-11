class Solution(object):
    # def countSubstrings(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     if not s:
    #         return 0
    #     if len(s) == 1:
    #         return 1
    #
    #     is_palindrome = [[-1] * len(s) for _ in range(len(s))]
    #
    #     for i in range(len(s)):
    #         is_palindrome[i][i] = 1
    #
    #     for i in range(1, len(s)):
    #         if s[i-1] == s[i]:
    #             is_palindrome[i-1][i] = 1
    #         else:
    #             is_palindrome[i-1][i] = 0
    #
    #     def fill(i, j):
    #         if is_palindrome[i][j] != -1:
    #             return is_palindrome[i][j]
    #         if s[i] == s[j]:
    #             inner_result = fill(i+1, j-1)
    #             if inner_result == 1:
    #                 is_palindrome[i][j] = 1
    #             else:
    #                 is_palindrome[i][j] = 0
    #         else:
    #             is_palindrome[i][j] = 0
    #
    #         return is_palindrome[i][j]
    #
    #     ans = 0
    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             result = fill(i, j)
    #             ans += result
    #     return ans

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1

        def count_layers(left, right):
            ret = 0
            if s[left] == s[right]:
                ret += 1
            else:
                return ret
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
                ret += 1
            return ret

        ans = 0
        # check the all centers
        for i in range(len(s)):
            ans += count_layers(i, i)

        for i in range(len(s)-1):
            ans += count_layers(i, i+1)
        return ans


# s = Solution()
# print(s.countSubstrings("ab"))
# print(s.countSubstrings("abc"))
# print(s.countSubstrings("aaa"))

