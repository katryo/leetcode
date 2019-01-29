class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        def is_pal(i, j):
            if i == 0:
                return s[:j+1] == s[j::-1]
            else:
                return s[i:j+1] == s[j:i-1:-1]

        n = len(s)
        table = [x for x in range(n)]

        for i in range(n):
            for j in range(i, n):
                if is_pal(i, j):
                    if i == 0:
                        table[j] = 0
                    else:
                        table[j] = min(table[j], table[i-1]+1)
        return table[n-1]



# s = Solution()
# print(s.minCut('cbbbcc'))
# print(s.minCut('cdd'))
# print(s.minCut('abcba'))
# print(s.minCut('a'))
# print(s.minCut('aab'))
