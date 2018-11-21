from collections import defaultdict
from copy import deepcopy
from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []

        counter = Counter(words)

        unit = len(words[0])
        ans = []
        window = unit * len(words)

        for margin in range(unit):
            sub_counter = Counter()
            score = 0

            for cur in range(margin, margin+window, unit):
                word = s[cur:cur+unit]
                if word in counter:
                    sub_counter[word] += 1
                    if sub_counter[word] <= counter[word]:
                        score += 1

            if score == len(words):
                ans.append(margin)

            for start in range(margin, len(s), unit):
                removed_word = s[start:start+unit]
                if removed_word in counter:
                    sub_counter[removed_word] -= 1
                    if sub_counter[removed_word] < counter[removed_word]:
                        score -= 1

                added_word = s[start+window: start+window+unit]
                if added_word in counter:
                    sub_counter[added_word] += 1
                    if sub_counter[added_word] <= counter[added_word]:
                        score += 1
                if score == len(words):
                    ans.append(start+unit)
        return ans


# s = Solution()
# # # print(s.findSubstring("", []))
# print(s.findSubstring("barfoothefoobarman", ["bar", "foo"]))
# print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))s = Solution()
# # # print(s.findSubstring("", []))
# print(s.findSubstring("barfoothefoobarman", ["bar", "foo"]))
# print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
