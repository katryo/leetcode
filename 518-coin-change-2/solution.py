class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        # memo[i][j] := #combinations with [0, i] coins to achieve j
        memo = [[-1] * (amount+1) for _ in range(len(coins))]

        def helper(coin_i, total):
            if coin_i < 0 or total < 0:
                return 0
            if memo[coin_i][total] != -1:
                return memo[coin_i][total]
            if total == 0:
                memo[coin_i][total] = 1
                return 1

            memo[coin_i][total] = helper(coin_i-1, total) + helper(coin_i, total - coins[coin_i])
            return memo[coin_i][total]

        if not coins:
            if amount == 0:
                return 1
            else:
                return 0
        return helper(len(coins)-1, amount)

s = Solution()
print(s.change(3, [1]))
print(s.change(3, [1, 2]))
print(s.change(5, [1, 2]))
print(s.change(5, [1, 2, 5]))
print(s.change(3, [2]))
print(s.change(10, [10]))




