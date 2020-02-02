import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        random.shuffle(nums)

        pivot = nums[0]
        smaller = []
        same = []
        greater = []
        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num == pivot:
                same.append(num)
            else:
                smaller.append(num)
        if k <= len(greater):
            return self.findKthLargest(greater, k)
        elif k <= len(greater) + len(same):
            return same[0]
        return self.findKthLargest(smaller, k - (len(greater) + len(same)))


# s = Solution()
# print(s.findKthLargest([3,2,1,5,6,4], 2))
# print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))

