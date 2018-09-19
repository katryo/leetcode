class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        mid = (len(nums) - 1) // 2
        if mid == 0:
            return min(nums[0], nums[1])

        def see_left(idx):
            i = idx
            while i > 0 and nums[i - 1] == nums[i]:
                i = i - 1
            return i

        def see_right(idx):
            i = idx
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i = i + 1
            return i

        mid_left = see_left(mid)
        mid_right = see_right(mid)
        if mid_right < len(nums) - 1 and nums[mid_right] > nums[mid_right + 1]:
            return nums[mid_right + 1]
        if mid_left > 0 and nums[mid_left - 1] > nums[mid_left]:
            return nums[mid_left]

        if nums[0] > nums[mid_left]:
            return self.findMin(nums[:mid_left])
        if nums[mid_right] > nums[len(nums) - 1]:
            return self.findMin(nums[mid_right + 1:])
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))

