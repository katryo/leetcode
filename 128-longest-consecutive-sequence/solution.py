class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)

        ans = 0
        for num in nums:
            if num-1 not in nums_set:
                start = num
                while num + 1 in nums_set:
                    num += 1
                ans = max(ans, num-start+1)
        return ans

    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     d = {}
    #
    #     for num in nums:
    #         if num in d:
    #             continue
    #
    #         val = d.get(num+1, 0) + d.get(num-1, 0) + 1
    #         d[num] = val
    #
    #         if num+1 in d:
    #             upper_edge = num+1 + d[num+1] - 1
    #             d[upper_edge] = val
    #         if num-1 in d:
    #             lower_edge = num-1 - d[num-1] + 1
    #             d[lower_edge] = val
    #
    #     ans = 0
    #     for num in nums:
    #         ans = max(ans, d[num])
    #     return ans


# s = Solution()
# print(s.longestConsecutive([1,2,0,1]))
# print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
# print(s.longestConsecutive([]))
