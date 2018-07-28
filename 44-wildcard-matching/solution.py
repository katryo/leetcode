class Solution:
    def isMatch(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        ts = 0
        ps = 0
        star = -1
        match = 0

        # adceb
        #  ^    ts
        # ^     match: starting idx * matches
        # *a*b
        #  ^    ps
        # ^     star

        while ts < len(text):
            if ps < len(pattern) and (text[ts] == pattern[ps] or pattern[ps] == '?'):
                ts += 1
                ps += 1
            elif ps < len(pattern) and pattern[ps] == '*':
                match = ts
                star = ps
                ps += 1
            elif star != -1:
                ps = star + 1
                match += 1
                ts = match
            else:
                return False

        while ps < len(pattern) and pattern[ps] == '*':
            ps += 1
        if ps == len(pattern):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"))
    print(s.isMatch("ho", 'ho**'))
    print(s.isMatch("aa", 'a'))
    print(s.isMatch("aa", '*'))
    print(s.isMatch("aa", 'a*'))
    print(s.isMatch("cb", '?a'))
    print(s.isMatch("acdcb", "a*c?b"))
    print(s.isMatch("adceb", "*a*b"))

