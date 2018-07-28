class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        def can_eat(k):
            ans = 0
            for pile in piles:
                ans += pile // k
                if pile % k > 0:
                    ans += 1
            return ans <= H

        def bsearch(mi, ma):
            # it is certain that can_eat(ma)
            # not sure about can_eat(mi)
            if mi >= ma:
                return mi

            mid = (mi + ma) // 2
            if can_eat(mid):
                return bsearch(mi, mid)
            else:
                return bsearch(mid+1, ma)

        minimum = sum(piles) // H
        if sum(piles) % H > 0:
            minimum += 1
        maximum = max(piles)

        return bsearch(minimum, maximum)
s = Solution()
print(s.minEatingSpeed([3,6,7,11], 8))
print(s.minEatingSpeed([30,11,23,4,20], 5))
print(s.minEatingSpeed([30,11,23,4,20], 6))
print(s.minEatingSpeed([3,6,7,11], 8))
