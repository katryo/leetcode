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
        table = [True] + [False] * length
        for i in range(len(pattern)):
            if pattern[i] == '*':
                for j in range(1, length+1):
                    table[j] = table[j-1] or table[j]
            else:
                for j in reversed(range(length)):
                    table[j] = table[j-1] and (pattern[i] == text[j] or pattern[i] == '?')
            table[0] = table[0] and pattern[i] == '*'
        return table[-1]


if __name__ == '__main__':
    s = Solution()
    # print(s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"))
    # print(s.isMatch("ho", 'ho**'))
    print(s.isMatch("aa", 'a'))
    print(s.isMatch("aa", '*'))
    print(s.isMatch("aa", 'a*'))
    print(s.isMatch("cb", '?a'))
    print(s.isMatch("acdcb", "a*c?b"))
    print(s.isMatch("adceb", "*a*b"))

