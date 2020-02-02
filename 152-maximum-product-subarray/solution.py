from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        a = []
        ans = - float('inf')
        for i in range(n):
            if nums[i] == 0:
                ans = max(ans, 0)
                if a:
                    ans = max(ans, self.sub(a))
                    a = []
                continue
            a.append((nums[i]))
        if a:
            ans = max(ans, self.sub(a))
        return ans

    def sub(self, nums):
        n = len(nums)
        products = [0] * n
        cur = 1

        ans = - float('inf')
        for i in range(n):
            cur = cur * nums[i]
            products[i] = cur
            ans = max(ans, cur)

        maxs = [0] * n
        mins = [0] * n

        max_so_far = - float('inf')
        min_so_far = float('inf')

        for i in range(n-1, -1, -1):
            max_so_far = max(max_so_far, products[i])
            maxs[i] = max_so_far

            min_so_far = min(min_so_far, products[i])
            mins[i] = min_so_far

        for i in range(n-1):
            if products[i] >= 0:
                cand = maxs[i+1] // products[i]
            else:
                cand = mins[i+1] // products[i]
            ans = max(ans, cand)
        return ans


# s = Solution()
# print(s.maxProduct([2,3,-2,4]))
# print(s.maxProduct([-2, 0, -1]))

