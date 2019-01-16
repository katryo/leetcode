class Solution:
    def __init__(self):
        self.dic = {}
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1, s2) in self.dic:
            return self.dic[s1, s2]
        n = len(s1)
        if n != len(s2):
            self.dic[s1, s2] = False
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            self.dic[s1, s2] = False
            return False
        if n < 4:
            return True

        assert n >= 4
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        self.dic[s1, s2] = False
        return False


s = Solution()
print(s.isScramble("great", "rgeat"))
print(s.isScramble("abcde", "caebd"))
print(s.isScramble("abab", "bbaa"))
