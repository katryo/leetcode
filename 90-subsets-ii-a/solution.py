class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [[]]
        length = 1

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                length = len(ans)
            for j in range(len(ans)-length, len(ans)):
                ans.append(ans[j] + [nums[i]])
        return ans


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))