class Solution:
    def isMatch(self, s, p):
        table = [[-1] * (len(p)+1) for _ in range(len(s)+1)]
        table[0][0] = 1

        for j in range(2, len(p)+1):
            if table[0][j-2] == 1 and p[j-1] == '*':
                table[0][j] = 1
            else:
                table[0][j] = 0

        def rec_is_match(i, j):
            if i < 0 or j < 0:
                return 0
            if table[i][j] != -1:
                return table[i][j]

            if p[j-1] != '*':
                if (p[j-1] == '.' or s[i-1] == p[j-1]) and rec_is_match(i-1, j-1) == 1:
                    table[i][j] = 1
                else:
                    table[i][j] = 0
            else:
                if rec_is_match(i, j-2) == 1:
                    table[i][j] = 1
                else:
                    if (s[i-1] == p[j-2] or p[j-2] == '.') and rec_is_match(i-1, j) == 1:
                        table[i][j] = 1
                    else:
                        table[i][j] = 0
            return table[i][j]

        return rec_is_match(len(s), len(p)) == 1


s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("aab", "c*a*b"))
