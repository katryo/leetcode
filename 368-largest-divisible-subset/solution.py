# from copy import deepcopy
from collections import defaultdict

class Solution(object):
    maxcount_set = (0, set())

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)

        print(dp)
        return []


s = Solution()
print(s.largestDivisibleSubset([1, 2, 3]))
print(s.largestDivisibleSubset([1, 2, 4, 8]))
print(s.largestDivisibleSubset([1, 2, 4, 8, 9, 72]))
