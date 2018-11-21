class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.backtrack(nums, target, results, 4, [])
        return results

    def backtrack(self, nums, target, results, total, current):
        if total > len(nums):
            return # Impossible

        if len(current) + 2 == total:
            # Choose two numbers
            left = 0
            right = len(nums)-1
            while left < right:
                summed = nums[left] + nums[right]
                if summed == target:
                    results.append(sorted(current + [nums[left]] + [nums[right]]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    continue
                if summed < target:
                    left += 1
                else:
                    right -= 1
            return

        diff = total - len(current)
        for i in range(diff):
            if nums[i] * total > target or nums[-1] * total < target:
                return
            self.backtrack(nums[1+i:], target-nums[i], results, total-1, current + [nums[i]])
        return


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([0, 0, 0, 0], 0))
