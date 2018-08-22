class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        if n < 4:
            return max(nums)

        table = [[-1] * n for _ in range(n)]
        for i in range(n):
            table[i][i] = nums[i]
        for i in range(n - 1):
            table[i][i + 1] = max(nums[i:i + 1])
        table[n - 1][0] = max(nums[n - 1:n])
        for i in range(n - 2):
            table[i][i + 2] = max(nums[i:i + 2])
        table[n - 2][0] = max(nums[n - 2:n])
        table[n - 1][1] = max(nums[n - 1:n+1])

        def rec(i, j):
            i = i % n
            if j < 0:
                j = j + n
            if table[i][j] != -1:
                return table[i][j]
            ret = -1
            for k in range(i, j+1):
                ret = max(ret, rec(k+2, k-2) + nums[k])

            table[i][j] = ret
            return ret

        return rec(0, n - 1)


s = Solution()
# print(s.rob([1, 2, 3, 1]))
# print(s.rob([9]))
print(s.rob([9, 1, 9]))
# print(s.rob([1, 9, 1, 9, 1, 9]))
# print(s.rob([1, 9, 1, 9, 1, 9, 1]))
# print(s.rob([2, 3, 2]))
