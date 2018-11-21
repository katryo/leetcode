class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        table = [-1] * (len(S)+1)
        table[0] = 1
        last_idx = {}
        MOD = 10 ** 9 + 7

        for i in range(len(S)):
            c = S[i]
            decrement = 0
            if c in last_idx:
                decrement = table[last_idx[c]]
            table[i+1] = (table[i] * 2 - decrement) % MOD
            last_idx[c] = i
        return table[len(S)]-1


# s = Solution()
# print(s.distinctSubseqII("abc"))
# print(s.distinctSubseqII("aba"))
# print(s.distinctSubseqII("aaa"))
# print(s.distinctSubseqII("abcdefghijklmnopol"))
