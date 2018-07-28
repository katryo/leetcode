class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # table = dict()
        # 0 <= len(nums) <= 20
        # 0 <= #combinations <= 2 ^ 20

        # memo[i][j] means #combinations that make j - 1000 with [0, i] subarray
        # 0 <= j <= 2000
        # 0 <= i < len(nums) <= 20
        # 20 x 2000

        if S > 1000 or S < -1000:
            return 0

        # memo = [[0] * 3001 for _ in range(len(nums) + 2)]
        # memo[0][1000+nums[0]] += 1
        # memo[0][1000-nums[0]] += 1

        memo = [0] * 4001
        memo[1000+nums[0]] += 1
        memo[1000-nums[0]] += 1

        for i in range(1, len(nums)):
            next_memo = [0] * 4001
            for j in range(2000):
                next_memo[j] = memo[j-nums[i]] + memo[j+nums[i]]
            memo = next_memo
        return memo[S + 1000]

s = Solution()
print(s.findTargetSumWays([1, 2, 1], 0))