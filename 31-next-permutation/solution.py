class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def bubble_sort_from(idx):
            for i in range(len(nums), idx+1, -1):
                for j in range(idx+1, i):
                    if nums[j-1] > nums[j]:
                        nums[j-1], nums[j] = nums[j], nums[j-1]

        seen = [(nums[len(nums) - 1], len(nums) - 1)]
        for right_i in range(len(nums) - 1, 0, -1):
            left_i = right_i - 1
            if nums[left_i] < nums[right_i]:
                swapped_i = right_i
                for num, idx in seen:
                    if nums[swapped_i] > num > nums[left_i]:
                        swapped_i = idx
                nums[left_i], nums[swapped_i] = nums[swapped_i], nums[left_i]
                bubble_sort_from(left_i+1)
                return
            else:
                seen.append((nums[left_i], left_i))

        for i in range(len(nums) // 2):
            nums[i], nums[-1 - i] = nums[-1 - i], nums[i]


# s = Solution()
# ns = [5,4,7,5,3,2]
# s.nextPermutation(ns)
# print(ns)
