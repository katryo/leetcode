class Solution(object):
    def combinationSum4(self, nums, target):
        if target == 0:
            return 1
        ans = 0
        for n in nums:
            ans += self.combinationSum4(nums, target-n)
        return ans


    # def combinationSum4(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     if not nums:
    #         if target == 0:
    #             return 1
    #         else:
    #             return 0
    #
    #     nums.sort()
    #     table = [[0] * len(nums) for _ in range(target + 1)]
    #     for i, num in enumerate(nums):
    #         if num <= target:
    #             table[num][i] = 1
    #     for i in range(1, target + 1):
    #         for j in range(len(nums)):
    #             for k, num in enumerate(nums):
    #                 if i + num <= target:
    #                     table[i + num][k] += table[i][j]
    #     return sum(table[target])


s = Solution()
print(s.combinationSum4([3, 33, 333], 33333))