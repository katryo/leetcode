from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)
        total = sum(weights)

        small = max(weights)
        big = total

        def try_with(limit):
            cur_total = 0
            days = 0
            for i in range(n):
                cur_total += weights[i]
                if cur_total > limit:
                    days += 1
                    cur_total = weights[i]
            if cur_total > 0:
                days += 1
            return days <= D

        while small < big:
            mid = (small + big) // 2

            if mid == small:
                if try_with(mid):
                    return mid
                else:
                    return big

            if try_with(mid):
                big = mid
            else:
                small = mid
        return small


# s = Solution()
# print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
# print(s.shipWithinDays([3,2,2,4,1,4], 3))
# print(s.shipWithinDays([1,2,3,1,1], 4))
