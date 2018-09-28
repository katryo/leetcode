class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        lengths = [-1] * len(strs)
        for i, st in enumerate(strs):
            lengths[i] = len(st)

        def is_substr(target, larger):
            i = 0
            for ch in larger:
                if i < len(target) and ch == target[i]:
                    i += 1
            return i == len(target)

        # def is_substr(target, larger):
        #     lar = 0
        #     for tar in range(len(target)):
        #         while lar < len(larger) and larger[lar] != target[tar]:
        #             lar += 1
        #         if lar == len(larger):
        #             return False
        #         lar += 1
        #     return True

        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                if strs[i] == strs[j]:
                    lengths[i] = -1
                    lengths[j] = -1
                if len(strs[i]) > len(strs[j]) and is_substr(strs[j], strs[i]):
                    lengths[j] = -1
                if len(strs[i]) < len(strs[j]) and is_substr(strs[i], strs[j]):
                    lengths[i] = -1

        return max(lengths)


s = Solution()
print(s.findLUSlength(["abc","def","ghi"]))
print(s.findLUSlength(["abc","def","gh"]))
print(s.findLUSlength(["aaa","aaa","aa"]))
