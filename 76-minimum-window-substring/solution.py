from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_occurence = defaultdict(int)
        for char in t:
            t_occurence[char] += 1
        match_count = 0 # If match_count == len(t) then the window contains T
        cur = defaultdict(int)

        ans = (-1, len(s)-1)
        left = 0
        for right in range(len(s)):
            r_char = s[right]
            cur[r_char] += 1
            if cur[r_char] <= t_occurence[r_char]:
                match_count += 1
            while match_count == len(t):
                if (ans[1]-ans[0]) > right-left:
                    ans = (left, right)

                l_char = s[left]
                cur[l_char] -= 1
                if cur[l_char] < t_occurence[l_char]:
                    match_count -= 1
                left += 1
        if ans == (-1, len(s)-1):
            return ''
        return s[ans[0]:ans[1]+1]


# s = Solution()
# print(s.minWindow("a", "a"))
# print(s.minWindow("bb", "bb"))
# print(s.minWindow("ADOBECODEBANC", "ABC"))
