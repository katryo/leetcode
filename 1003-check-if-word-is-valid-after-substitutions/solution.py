class Solution:
    def isValid(self, S: str) -> bool:
        if S == 'abc':
            return True
        for i in range(len(S)-3):
            if S[i:i+3] == 'abc':
                return self.isValid(S[:i] + S[i+3:])
        return False

    def isValid2(self, S: str) -> bool:
        if len(S) % 3 != 0:
            return False

        n = len(S)
        table = [[-1] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            table[i][i] = 1

        # return True if S[i:j] is valid
        def rec(i, j):
            if i > j:
                return False
            if table[i][j] != -1:
                return table[i][j]
            if S[i:i + 3] == 'abc' and rec(i + 3, j) == 1:
                table[i][j] = 1
                return True
            if S[i:i + 2] == 'ab' and S[j - 1] == 'c' and rec(i + 2, j - 1) == 1:
                table[i][j] = 1
                return True
            if S[i] == 'a' and S[j - 2:j] == 'bc' and rec(i + 1, j - 2) == 1:
                table[i][j] = 1
                return True
            if S[j - 3:j] == 'abc' and rec(i, j - 3) == 1:
                table[i][j] = 1
                return True
            table[i][j] = 0
            return False

        ans = rec(0, n)
        for r in table:
            print(r)
        return ans


s = Solution()
print(s.isValid("aabcbabcc"))

print(s.isValid("aabcbc"))
print(s.isValid("abc"))
print(s.isValid("aabcbc"))
print(s.isValid("abcabc"))
print(s.isValid("abcabcababcc"))
print(s.isValid("aabcbcabc"))

print(s.isValid("abccba"))
print(s.isValid("cababc"))
print(s.isValid("cbbbbcaaaccbaabccabacabcacbabbabbcbacabacabcabbccbccbccbcaccbacaabaaababacbbccabbcbcbabbcbabcacabcbababcaccbcbbbaaabbcbccaaabcbababaaaccbacbbcaabbacbbbabcccacbaacacccbcccbbbbccaaabaaababcbbaacbcccaaabcbacccaacbbbaabababbbbababcbaaaabbcacbacaaabbcacbccbbbbaabcacbccababaaaacbabbbaaccbccaacacccaaabacaaaacacbbaabcabcbcccbcabaaaccbcbaaaccaacbabcaabbccacbbcbbbcaccbaccacaabcbcccacacaccaabbcaaababbbbbbcabcbbacabbbbbaabcbabbbccaabccabccaaaccabcbcbabbcaccabcbaabaaabacccacacabbaccbabbbacaaabacacabacbcabaabaccacbbaacbcaccaccbacbaacbcbabccbcacbbbcabaabaabbabbcbbbcbbaabababcacacacbcabbccbbbacacccbbbbbbcbabaacacbbbaccbcaaccaccabbabbcbaababbcacaababaababcccbbcaaaabccabbbcbbaacacabaabbaabcaabaacaabcbaaabaccbbcbaaababcacaacabcbbbbabaccbabbccacbbbcbacccbbbcabaaaacacaacbbcabbbbaacacababccaaacaccaaaacbabbcacaabaacaaabcacaabcaaaaaaacbbabbababcbbccbabbabaccbbcccacaabcbccacaacbacbcccbabababababbacbabacbcccccbbcbcbabbbbaacbbabacccbcccbcaccabacaacbbbabacccccbcbbbacaccacccbccbbbcbcbaacbbaabaacbacabacacaaaccaaacabbbaabcaacacbaaabcbbbbcaacaaccbbbccbababcbcacbcbcbbaabcacbbcacaacacccababbcacbbcaaccaacbbabccabbccbacacaccccccbcbbcbabcabbcaabbaabaccababcbcbcbabbcabcbabacaababcbcacbaacbcccbbbcbaacabcccbbabccacaaaaccaabccbbaabababcacabbaccbbacbcbcaacabbaccccabbccbbcabcbcccaabcccbabbacabccaacababcaaaacccbabcccabcccabccbacaacabcbbaacbaacbbcbaaaacbbcaccbacaccaaaccabaaabcbabababbcbbcbacbabaacbbbaacabbbaacbaccccaaccccabcabaabaccacaaacabbbbcbccccbcacaacbcbbbcbabcbccaaabbaccbaacccbaacbbbbcccacbcacabccbbcbabbccabbbaabaacbbacacacccbcbcbaabcccacbccbbcacaababbcbaaabaccaaaaacbbbacaaaaabbacaabacbcaccaacbacbaaaabcbaaabcccccbcacbccacbccccaacaaccbbcbabcbaacbbabbbbaabcacbaaacbbcabcbcbbbcabbbbcbcbacccbcaacaccccbcccacbbbbbacbccaabcbabcacacbbaccbbbaccbcaacacabaaccbccabbccbacbaacbbbbacacccabbbbabaaaabcbabcccacccababbabcabbbaabacbcbaaccccacbbbccccacaaaacabaacaccaabccacbbbccaabbccccbccbbbabacbabacbabcbaccbabbaccaccbabcababbbbcbbcabababaacaccacbacccabcacbbbcccacacabcabccaacbacbcaccbaaaacbbccccccaabbabcbaaaacbbbaabbcacabaccabbcbbbbabbccabcccccbbcbbcccbbacacbaaacccccbbcaacaacabbbcacaaaaaacabacbbbbbacbbacbbcbbbcbbaccaacbcbaaaabbbababbbccccaabacbcaacacbbcacccaacccccbbccbbbbbacbabcabbcacccbcbabbaabbacaabaacabcccbbbbcacabbbaacaaacbabbaccaacabbcbbaaabaccaccacccbbbacaccacbabbaacabbcbbcbbccbbbacbbacbbbabcaababaacbaacaabbacbabbccccaccccaabbaaabcccabccbccaaacbbccabbbcbaaaacabbbbbbcbbacbbcccbbabbacbbccbccccccaabacaabaaaccccaabcacbbccbbabccaacccaababbccbabcbabcccbbabaaaababaabbbcbabbccaacbacccaabccababccabcbbcccaacabbbcbaaabbcaacbbbaabaacbbacbbcacbcabccbbccbcbcbbcbaacacbbbbcacbabbaacccaccbacbbcabbbbabcabaabbcaacabbbbbbccbacacaaacabaacbcbacbaaacabcbbcbbbabaccabaaaacaaaaaacaccbccaabaabcaaabaaababcabcccbbcacbcacaabbaaacbbbbcbabaabaabacacaaccbaacabcacbaaabbacccbccaabbaccabbbbacbcbccbcbbcbcbcbcabcccbccaacacccccbbbabbabcbcbabbacaabcbaabbacbcaccacacccacbabbabacababcbaccaabcbacabbacaaaabccbbbbcaabbccbcccccbccacaababcccacbcbcbccabbcbcbcccccccacaaccbbccccbbbcabbacaacacbbabcaacacbcccacbcbcbaaaaccaabaaabcabcaacaacabaacccabaabbaac"))
