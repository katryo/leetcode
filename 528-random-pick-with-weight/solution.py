from random import randrange


class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weights = w
        self.sum_weights = [0] * len(w)
        if not w:
            return
        self.sum_weights[0] = w[0]
        for i in range(1, len(w)):
            self.sum_weights[i] = self.sum_weights[i-1] + self.weights[i]
        self.total = self.sum_weights[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        r = randrange(1, self.total+1) # [1, self.total]
        lo = 0
        hi = len(self.weights)-1

        # [lo, hi]
        while lo < hi:
            mid = (lo+hi) // 2
            if self.sum_weights[mid] < r:
                lo = mid+1
            else:
                hi = mid
        return lo


# obj = Solution([2, 5, 12])
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
# print(obj.pickIndex())
