class Solution:
    def minDistance(self, word1, word2):
        table = [[-1] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0 or j == 0:
                    table[i][j] = max(i, j)
                elif word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = min(table[i-1][j], table[i][j-1]) + 1
        return table[len(word1)][len(word2)]

    def minDistance3(self, word1, word2):
        table = [0] * (len(word2)+1)
        for i in range(len(word1)+1):
            new_table = [0] * (len(word2)+1)
            for j in range(len(word2)+1):
                if i == 0 or j == 0:
                    new_table[j] = max(i, j)
                elif word1[i-1] == word2[j-1]:
                    new_table[j] = table[j-1]
                else:
                    new_table[j] = min(table[j], new_table[j-1]) + 1
            table = new_table
        return table[len(word2)]


    def minDistance2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return max(len(word1), len(word2))
        table = [[-1] * len(word2) for _ in range(len(word1))]

        def step(i, j):
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if table[i][j] != -1:
                return table[i][j]
            if word1[i] == word2[j]:
                table[i][j] = step(i - 1, j - 1)
                return table[i][j]
            smaller = min(step(i - 1, j), step(i, j - 1))
            table[i][j] = smaller + 1
            return smaller + 1

        return step(len(word1) - 1, len(word2) - 1)


s = Solution()
print(s.minDistance("abc", "aaabbbccc"))
print(s.minDistance2("abc", "aaabbbccc"))
print(s.minDistance3("abc", "aaabbbccc"))
