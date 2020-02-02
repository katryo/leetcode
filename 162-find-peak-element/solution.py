from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left != right:
            if left + 1 == right:
                if nums[left] < nums[right]:
                    return right
                else:
                    return left

            mid = (left + right) // 2
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                left = mid+1
            elif nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            else:
                right = mid-1

        return left


# s = Solution()
# print(s.findPeakElement([1, 2, 3, 1]))
# print(s.findPeakElement([1,2,1,3,5,6,4]))



