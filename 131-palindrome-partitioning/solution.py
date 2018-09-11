from copy import deepcopy

class Solution(object):
    pal_dict = {}

    def is_palindrome(self, s):
        return s == s[::-1]

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def backtrack(text, cur, results):
            if not text:
                results.append(deepcopy(cur))
                return
            for i in range(1, len(text)+1):
                if self.is_palindrome(text[:i]):
                    backtrack(text[i:], cur + [text[:i]], results)

        ans = []
        backtrack(s, [], ans)
        return ans


# s = Solution()
# print(s.partition('ab'))
# print(s.partition('abbab'))
# print(s.partition("amanaplanacanalpanama"))
