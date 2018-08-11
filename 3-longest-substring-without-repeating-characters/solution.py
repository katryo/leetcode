class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     if not s:
    #         return 0
    #     table = [-1] * len(s)
    #     # table[i]: max length in [0, i] that ends at i
    #     table[0] = 1
    #
    #     prev = [-1] * len(s)
    #     prev_dic = dict()
    #     for i in range(len(s)):
    #         if s[i] in prev_dic:
    #             prev[i] = prev_dic[s[i]]
    #         prev_dic[s[i]] = i
    #     for i in range(1, len(s)):
    #         if prev[i] == -1:
    #             table[i] = table[i-1] + 1
    #         else:
    #             if i - prev[i] > table[i-1]:
    #                 table[i] = table[i-1] + 1
    #             else:
    #                 table[i] = i - prev[i]
    #     return max(table)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        start = 0
        ans = 1
        seen = {s[0]: 0}
        # window is [start, end)
        for end in range(1, len(s)):
            if s[end] in seen:
                next_start = seen[s[end]]
                start = next_start+1
            ans = max(ans, end-start+1)
            seen[s[end]] = end
        return ans


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
