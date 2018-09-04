class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        def word_to_structure(word):
            ret = [0] * 52
            for i, c in enumerate(word):
                number = (ord(c) - ord('a')) + 26 * (i%2)
                ret[number] += 1
            return tuple(ret)

        seen = set()
        for word in A:
            structure = word_to_structure(word)
            seen.add(structure)
        return len(seen)


# s = Solution()
# print(s.numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))

