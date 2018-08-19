class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        prev_product = 1
        for i in range(len(nums)):
            ans[i] = prev_product
            prev_product *= nums[i]

        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * right_product
            right_product *= nums[i]
        return ans


s = Solution()
print(s.productExceptSelf([3, 5, 6, 2, 3]))
