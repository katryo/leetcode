class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count_map = dict()
        count_map[0] = -1
        count = 0
        ans = 0
        for i, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1
            if count in count_map:
                ans = max(ans, i - count_map[count])
            else:
                count_map[count] = i
        return ans

# s = Solution()
# print(s.findMaxLength([0, 1]))
# print(s.findMaxLength([0, 1, 0]))
# print(s.findMaxLength([0, 1, 0, 1]))
# print(s.findMaxLength([0, 1, 1, 1]))
# print(s.findMaxLength([0, 1, 1, 1, 1, 0, 1]))
# print(s.findMaxLength([1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1]))
