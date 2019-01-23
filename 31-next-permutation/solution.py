class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if sorted(nums, reverse=True) == nums:
            nums.sort()
            return

        def increment(start):
            i_min_gt_start = start + 1
            for i in range(start+2, len(nums)):
                if nums[start] < nums[i] < nums[i_min_gt_start]:
                    i_min_gt_start = i
            nums[start], nums[i_min_gt_start] = nums[i_min_gt_start], nums[start]
            nums[start+1:] = sorted(nums[start+1:])

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                increment(i)
                return


s = Solution()
# ns = [5,4,7,5,3,2]
ns = [3,2,1]
s.nextPermutation(ns)
print(ns)
