from copy import deepcopy

class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        if not price:
            return -1

        needs6 = [0] * 6
        for i, need in enumerate(needs):
            needs6[i] = need

        # special6 = [[0, 0, 0, 0, 0, 0, 0]]
        special6 = []

        for i, sp in enumerate(special):
            while len(sp) < 7:
                sp.insert(-1, 0)
            special6.append(sp)

        prices = [0] * 6
        for i in range(len(price)):
            prices[i] = price[i]

        table = [-1] * 7
        for item in range(5):
            table = [deepcopy(table) for _ in range(7)]

        table[0][0][0][0][0][0] = 0

        def min_price(a, b, c, d, e, f):
            if a < 0 or b < 0 or c < 0 or d < 0 or e < 0 or f < 0:
                return float('inf')
            if table[a][b][c][d][e][f] != -1:
                return table[a][b][c][d][e][f]
            cand = float('inf')
            for sp in special6:
                aa, bb, cc, dd, ee, ff, pr = sp
                cand = min(cand, min_price(a - aa, b - bb, c - cc, d - dd, e - ee, f - ff) + pr)
            cand = min(cand, min_price(a - 1, b, c, d, e, f) + prices[0])
            cand = min(cand, min_price(a, b - 1, c, d, e, f) + prices[1])
            cand = min(cand, min_price(a, b, c - 1, d, e, f) + prices[2])
            cand = min(cand, min_price(a, b, c, d - 1, e, f) + prices[3])
            cand = min(cand, min_price(a, b, c, d, e - 1, f) + prices[4])
            cand = min(cand, min_price(a, b, c, d, e, f - 1) + prices[5])

            table[a][b][c][d][e][f] = cand
            return cand

        need6 = [0] * 6
        for i, n in enumerate(needs):
            need6[i] = n
        return min_price(need6[0], need6[1], need6[2], need6[3], need6[4], need6[5])


s = Solution()
print(s.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))
print(s.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))
print(s.shoppingOffers([9,9], [[1,1,1]], [6,6]))

