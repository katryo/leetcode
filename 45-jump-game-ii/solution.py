class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        far_most = 0
        counter = 0
        while right < len(nums)-1:
            for i in range(left, right+1):
                far_most = max(far_most, nums[i] + i)
            left = right+1
            right = far_most
            counter += 1
        return counter


s = Solution()
print(s.jump([2,3,1,1,4]))