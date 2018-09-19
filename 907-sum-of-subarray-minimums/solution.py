class Solution:
    def sumSubarrayMins(self, A):
        size = len(A)

        #1. generate prev_smaller
        prev_smaller = [0] * size
        stack = []
        for i in range(size):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            else:
                prev_smaller[i] = -1
            stack.append(i)

        next_smaller = [0] * size
        stack = []
        for i in range(size-1, -1, -1):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            else:
                next_smaller[i] = size
            stack.append(i)

        ans = 0
        for i in range(size):
            ans += A[i] * ((i - prev_smaller[i]) * (next_smaller[i] - i))
            ans %= (10 ** 9 + 7)
        return ans


    def sumSubarrayMins2(self, A):
        MOD = 10 ** 9 + 7
        n = len(A)

        stack = []
        prev_smaller = [0] * n
        for i in range(n):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            else:
                prev_smaller[i] = -1
            stack.append(i)

        stack = []
        next_smaller = [0] * n
        for i in range(n-1, -1, -1):
            while stack and A[i] < A[stack[-1]]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            else:
                next_smaller[i] = n
            stack.append(i)

        print(prev_smaller)
        print(next_smaller)
        ans = 0
        for i in range(n):
            ans += A[i] * ((next_smaller[i]-i) * (i-prev_smaller[i]))
            ans %= MOD
        return ans


    # def sumSubarrayMins(self, A):
        # if len(A) == 1:
        #     return A[0]
        #
        # B = [0] * (len(A)-1)
        # total = A[0]
        # for i in range(1, len(A)):
        #     smaller = min(A[i], A[i-1])
        #     B[i-1] = smaller
        #     total += A[i]
        # A = None
        # return (total + self.sumSubarrayMins(B)) % (10 ** 9 + 7)

    # def sumSubarrayMins(self, A):
        # """
        # :type A: List[int]
        # :rtype: int
        # """
        #
        # sorted_a = sorted(A)
        #
        # def backtrack(nums):
        #     if not nums:
        #         return 0
        #     if len(nums) == 1:
        #         return nums[0]
        #     target = 0
        #     target_val = nums[0]
        #     for i in range(1, len(nums)):
        #         if nums[i] < target_val:
        #             target = i
        #             target_val = nums[i]
        #
        #     sub_contain = (len(nums) - target) * (target + 1)
        #     total = sub_contain * target_val
        #     left = backtrack(nums[:target])
        #     right = backtrack(nums[target + 1:])
        #     return (total + left + right) % (10 ** 9 + 7)
        #
        # return backtrack(A)


s = Solution()
# A = [3, 1, 2, 4]
# A = [10, 5, 3, 7, 0, 4, 5, 2, 1, 8]
A = [71,55,82,55]
print(s.sumSubarrayMins(A))
print(s.sumSubarrayMins2(A))
