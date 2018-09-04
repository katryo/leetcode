class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.build_results(nums, target, 4, [], results)
        return results

    def build_results(self, nums, target, num_of_chosen, result, results):
        if num_of_chosen > len(nums) or num_of_chosen < 2:
            return
        if num_of_chosen == 2:
            left = 0
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
            return

        for i in range(len(nums)-num_of_chosen+1):
            if nums[i] * num_of_chosen > target or nums[-1] * 4 < target:
                return
            self.build_results(nums[i+1:], target-nums[i], num_of_chosen-1, result+[nums[i]], results)


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([0, 0, 0, 0], 0))
