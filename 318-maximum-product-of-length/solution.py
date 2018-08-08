# Given a string array words, find the maximum value of length(word[i]) * length(word[j])
# where the two words do not share common letters.
# You may assume that each word will contain only lower case letters.
# If no such two words exist, return 0.
#
# Example 1:
#
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# Example 2:
#
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# Example 3:
#
# Input: ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0

        bin_words = [0] * len(words)
        for i in range(len(words)):
            word = words[i]
            bin_word = 0
            for char in word:
                alpha_idx = ord(char) - ord('a')
                bin_word |= (1 << alpha_idx)
            bin_words[i] = bin_word

        ans = 0
        for i in range(1, len(words)):
            for j in range(i):
                if bin_words[i] & bin_words[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans

#
# s = Solution()
# print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))

