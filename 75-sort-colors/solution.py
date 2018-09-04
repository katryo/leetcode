class Solution(object):
    def sortColors(self, nums):
        left = 0
        right = len(nums)-1
        cur = 0
        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
                cur -= 1
            cur += 1
        return nums


    # def sortColors(self, nums):
    #     n0 = 0
    #     n1 = 0
    #     n2 = 0
    #
    #     for i in range(len(nums)):
    #         n = nums[i]
    #         if n == 0:
    #             n0 += 1
    #         if n == 1:
    #             n1 += 1
    #         if n == 2:
    #             n2 += 1
    #     for i in range(n0):
    #         nums[i] = 0
    #
    #     for i in range(n0, n0+n1):
    #         nums[i] = 1
    #     for i in range(n0+n1, n0+n1+n2):
    #         nums[i] = 2
    #     return nums


s = Solution()
print(s.sortColors([1, 2, 2, 0, 0, 2]))
print(s.sortColors([2, 2, 2, 2]))
print(s.sortColors([2, 0, 1, 2]))
print(s.sortColors([0, 0, 0, 0]))
