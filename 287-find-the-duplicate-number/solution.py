class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slower = nums[0]
        faster = nums[0]
        while True:
            slower = nums[slower]
            faster = nums[nums[faster]]
            if slower == faster:
                break

        third = nums[0]
        while third != slower:
            third = nums[third]
            slower = nums[slower]
        return nums[slower]


s = Solution()
print(s.findDuplicate([1, 2, 3, 1]))