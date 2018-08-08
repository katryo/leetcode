class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # 4 ** 10 == 2 ** 20 == 1024 * 1024

        def nuc_to_int(nuc):
            if nuc == 'A':
                return 0
            if nuc == 'T':
                return 1
            if nuc == 'G':
                return 2
            else:
                return 3

        def dna_to_int(dna):
            ret = 0
            for i in range(len(dna)):
                ret += nuc_to_int(dna[i]) * (4 ** i)
            return ret

        if len(s) < 10:
            return []
        cur = s[:10]
        found = {dna_to_int(cur)}
        ans = set()
        for i in range(10, len(s)):
            cur = cur[1:] + s[i]
            num = dna_to_int(cur)
            if num in found:
                ans.add(cur)
            found.add(num)
        return list(ans)

s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
