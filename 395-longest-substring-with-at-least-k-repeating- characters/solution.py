from collections import Counter
from copy import deepcopy


class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def all_k(c):
            for key in c:
                if c[key] < k:
                    return False
            return True

        def letter_less_than_k(c):
            for letter in c:
                if c[letter] < k:
                    return letter
            return ''


        counter = Counter()
        for i in range(len(s)):
            counter[s[i]] += 1

        if all_k(counter):
            return len(s)

        letter = letter_less_than_k(counter)
        cands = s.split(letter)
        return max([self.longestSubstring(cand, k) for cand in cands])


s = Solution()
print(s.longestSubstring("ababbc", 2))
print(s.longestSubstring("aaabb", 3))
