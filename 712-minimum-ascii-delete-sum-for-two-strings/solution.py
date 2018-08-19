class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        if not s1 and not s2:
            return 0
        if not s1:
            return sum([ord(c) for c in s2])
        if not s2:
            return sum([ord(c) for c in s1])
        table = [[-1] * (len(s2)+1) for _ in range(len(s1))]

        if s1[0] == s2[0]:
            table[0][0] = 0
        else:
            table[0][0] = ord(s1[0]) + ord(s2[0])

        def cost(i, j):
            if i == -1:
                return sum(ord(c) for c in s2[:j+1])
            if j == -1:
                return sum(ord(c) for c in s1[:i+1])
            if table[i][j] != -1:
                return table[i][j]
            if s1[i] == s2[j]:
                table[i][j] = cost(i-1, j-1)
                return table[i][j]
            table[i][j] = min(cost(i-1, j)+ord(s1[i]), cost(i, j-1)+ord(s2[j]))
            return table[i][j]

        return cost(len(s1)-1, len(s2)-1)


# s = Solution()
# print(s.minimumDeleteSum("", "eat"))
# print(s.minimumDeleteSum("sea", ""))
# print(s.minimumDeleteSum("", ""))
# print(s.minimumDeleteSum("sea", "eat"))
# print(s.minimumDeleteSum("delete", "leet"))

