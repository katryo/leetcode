class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        valid_words = []

        for word in d:
            p_word = 0

            for i in range(len(s)):
                if word[p_word] == s[i]:
                    p_word += 1
                if p_word == len(word):
                    valid_words.append(word)
                    break

        ans = ""
        for word in valid_words:
            if len(ans) < len(word):
                ans = word
                continue
            if len(ans) == len(word):
                ans = min(ans, word)

        return ans


s = Solution()
print(s.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
print(s.findLongestWord("abpcplea", ["a","b","c"]))
