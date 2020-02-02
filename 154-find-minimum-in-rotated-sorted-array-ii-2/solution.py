from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)

        if nums[0] < nums[-1]:
            return nums[0]

        def b_search(lo, hi):
            if lo == hi:
                return nums[lo]
            if nums[lo] < nums[hi]:
                return nums[lo]

            assert nums[lo] >= nums[hi]
            if lo + 1 == hi:
                return nums[hi]

            mid = (lo + hi) // 2
            cand = nums[mid]
            if nums[lo] <= nums[mid]:
                while mid != hi and nums[mid] == nums[mid+1]:
                    mid += 1
                if mid == hi:
                    cand = min(cand, nums[mid])
                else:
                    cand = min(cand, b_search(mid, hi))
            if nums[mid] <= nums[hi]:
                while mid != lo and nums[mid] == nums[mid-1]:
                    mid -= 1
                if lo == mid:
                    cand = min(cand, nums[mid])
                else:
                    cand = min(cand, b_search(lo, mid))
            return cand
        return b_search(0, n-1)


# s = Solution()
# print(s.findMin([3, 1, 3]))
# print(s.findMin([1, 3, 5]))
# print(s.findMin([2, 2, 2, 0, 1]))
# print(s.findMin([3,4,5,1,2]))
# print(s.findMin([4,5,6,7,0,1,2]))