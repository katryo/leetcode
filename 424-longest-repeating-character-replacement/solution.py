import collections


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0

        counts = collections.defaultdict(int)
        start = 0
        ans = 0
        max_count = 0
        for end in range(len(s)):
            char = s[end]
            counts[char] += 1
            max_count = max(max_count, counts[char])

            if end - start - (max_count - 1) > k:
                counts[s[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)
        return ans


s = Solution()
# print(s.characterReplacement("abab", 2))
# print(s.characterReplacement("abaa", 1))
# print(s.characterReplacement("abaaaaaabbaaaaa", 2))
print(s.characterReplacement("zzaaaabcdefghijka", 3))
