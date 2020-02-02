from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)

        if nums[0] < nums[-1]:
            return nums[0]

        def b_search(lo, hi):
            if nums[lo] < nums[hi]:
                return lo

            if lo + 1 == hi:
                return hi

            mid = (lo + hi) // 2
            if nums[lo] < nums[mid]:
                return b_search(mid, hi)
            else:
                return b_search(lo, mid)
        min_i = b_search(0, n-1)
        return nums[min_i]


# s = Solution()
# print(s.findMin([3,4,5,1,2]))
# print(s.findMin([4,5,6,7,0,1,2]))
