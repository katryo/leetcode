# https://leetcode.com/problems/wiggle-subsequence/solution/

class Solution(object):
    def wiggleMaxLength5(self, nums):
        if len(nums) < 2:
            return len(nums)
        if nums[0] == nums[1]:
            ans = 1
        else:
            ans = 2
        prediff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if (prediff <= 0 < diff) or (diff < 0 <= prediff):
                ans += 1
                prediff = diff
        return ans


    def wiggleMaxLength4(self, nums):
        if len(nums) < 2:
            return len(nums)

        down = up = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                up = down + 1
            elif nums[i-1] > nums[i]:
                down = up + 1
        return max(up, down)


    def wiggleMaxLength3(self, nums):
        if len(nums) < 2:
            return len(nums)

        down = up = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                up = down + 1
            elif nums[i-1] > nums[i]:
                down = up + 1
        return max(up, down)


    def wiggleMaxLength2(self, nums):
        if len(nums) < 2:
            return len(nums)

        down = [0] * len(nums)
        up = [0] * len(nums)
        down[0] = 1
        up[0] = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i-1] == nums[i]:
                up[i] = up[i-1]
                down[i] = down[i-1]
            else:  # >
                up[i] = up[i-1]
                down[i] = up[i-1] + 1
        return max(up[len(nums)-1], down[len(nums)-1])


    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        p_smaller = [-1] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and stack[-1][1] >= nums[i]:
                stack.pop()
            if stack:
                p_smaller[i] = stack[-1][0]
            stack.append((i, nums[i]))

        p_greater = [-1] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and stack[-1][1] <= nums[i]:
                stack.pop()
            if stack:
                p_greater[i] = stack[-1][0]
            stack.append((i, nums[i]))

        ans = 1
        up = [0] * len(nums)
        down = [0] * len(nums)
        up[0] = 1
        down[0] = 1
        for i in range(1, len(nums)):
            if p_smaller[i] == -1:
                up[i] = max(1, up[i - 1])
            else:
                up[i] = max(down[p_smaller[i]] + 1, up[i - 1])
                ans = max(ans, up[i])

            if p_greater[i] == -1:
                down[i] = max(1, down[i - 1])
            else:
                down[i] = max(up[p_greater[i]] + 1, down[i - 1])
                ans = max(ans, down[i])

        return ans


s = Solution()
print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(s.wiggleMaxLength2([1,17,5,10,13,15,10,5,16,8]))
print(s.wiggleMaxLength3([1,17,5,10,13,15,10,5,16,8]))
print(s.wiggleMaxLength4([1,17,5,10,13,15,10,5,16,8]))
print(s.wiggleMaxLength5([1,17,5,10,13,15,10,5,16,8]))
