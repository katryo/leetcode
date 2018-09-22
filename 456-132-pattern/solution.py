# https://leetcode.com/problems/132-pattern/solution/

class Solution:
    def find132pattern(self, nums):
        last_cand = float('-inf')
        stack = []
        for num in reversed(nums):
            if num < last_cand:
                return True
            while stack and stack[-1] < num:
                last_cand = stack.pop()

            stack.append(num)

    # def find132pattern(self, nums):
    #     if len(nums) < 3:
    #         return False
    #
    #     min_so_far = [nums[0]] * len(nums)
    #     for i in range(1, len(nums)):
    #         min_so_far[i] = min(min_so_far[i-1], nums[i])
    #
    #     stack = []
    #     for i in range(len(nums)-1, 0, -1):
    #         if nums[i] > min_so_far[i-1]:
    #             while stack and stack[-1] <= min_so_far[i-1]:
    #                 stack.pop()
    #             if stack and min_so_far[i-1] < stack[-1] < nums[i]:
    #                 return True
    #             stack.append(nums[i])
    #     return False


    # def find132pattern(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     intervals = []
    #     i = 1
    #     start = 0
    #     while i < len(nums):
    #         if nums[i-1] >= nums[i]:
    #             if start < i-1:
    #                 intervals.append([nums[start], nums[i-1]])
    #             start = i
    #         for interval in intervals:
    #             if interval[0] < nums[i] < interval[1]:
    #                 return True
    #         i += 1
    #     return False


s = Solution()
print(s.find132pattern([1, 2, 3, 4]))
print(s.find132pattern([3, 1, 4, 2]))
print(s.find132pattern([-1, 3, 2, 0]))
print(s.find132pattern([3,5,0,3,4]))
