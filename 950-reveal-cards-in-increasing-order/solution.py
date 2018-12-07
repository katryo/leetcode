class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if not deck:
            return []
        deck.sort()
        l = len(deck)

        ans = [0] * l

        smaller_half = deck[:l//2]
        idx = 0
        for i in range(len(smaller_half)):
            ans[idx] = smaller_half[i]
            idx += 2

        if len(deck[1//2:]) == 1:
            rest = deck[1//2:]
        else:
            rest = self.deckRevealedIncreasing(deck[l//2:])
        if len(deck) % 2:
            ans[l-1] = rest[0]
            rest_i = 1
            for i in range(1, l, 2):
                ans[i] = rest[rest_i]
                rest_i += 1
        else:
            rest_i = 0
            for i in range(1, l, 2):
                ans[i] = rest[rest_i]
                rest_i += 1

        return ans


s = Solution()
# print(s.deckRevealedIncreasing([1,2,3,4]))
print(s.deckRevealedIncreasing([1,2,3,4,5,6]))
# print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))
