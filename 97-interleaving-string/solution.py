class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        table = [[False] * (m+1) for _ in range(n+1)]
        table[0][0] = True
        for i in range(1, n+1):
            table[i][0] = table[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, m+1):
            table[0][j] = table[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, n+1):
            for j in range(1, m+1):
                table[i][j] = (table[i-1][j] and s1[i-1] == s3[i-1+j]) or\
                              (table[i][j-1] and s2[j-1] == s3[i-1+j])
        return table[n][m]


# s = Solution()
# print(s.isInterleave("", "a", "a"))
# print(s.isInterleave("", "dbbc", "dbbc"))
# print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
# print(s.isInterleave("", "", "a"))
# print(s.isInterleave("", "", ""))
# print(s.isInterleave("s", "", ""))
# print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
# print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
