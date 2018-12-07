class Solution:
    def isMatch(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length = len(text)
        if len(pattern) > pattern.count('*') + len(text):
            return False
        table = [[True] + [False] * length for _ in range(len(pattern)+1)]

        for i in range(len(pattern)):
            table[i+1][0] = table[i][0] and pattern[i] == '*'

        for i in range(len(pattern)):
            if pattern[i] == '*':
                for j in range(length):
                    table[i+1][j+1] = table[i+1][j] or table[i][j+1]
            else:
                for j in range(length):
                    table[i+1][j+1] = table[i][j] and (pattern[i] == text[j] or pattern[i] == '?')

        return table[-1][-1]


# if __name__ == '__main__':
#     s = Solution()
#     print(s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"))
#     print(s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaabab", "a*******b"))
#     print(s.isMatch("aab", "a*"))
#     print(s.isMatch("ho", 'ho**'))
#     print(s.isMatch("aa", 'a'))
#     print(s.isMatch("aa", '*'))
#     print(s.isMatch("aa", 'a*'))
#     print(s.isMatch("cb", '?a'))
#     print(s.isMatch("acdcb", "a*c?b"))
#     print(s.isMatch("adceb", "*a*b"))
#     print(s.isMatch("a", "c*"))

