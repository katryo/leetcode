class Solution:
    def coinChange2(self, coins, amount):
        if amount == 0:
            return 0
        if not coins:
            return -1
        coins.sort(reverse=True)
        table = [-2] * (amount + 1)
        table[0] = 0

        def helper(money):
            if money < 0:
                return -1
            if table[money] != -2:
                return table[money]
            ans = -1
            for coin in coins:
                result = helper(money - coin) + 1
                if result > 0:
                    if ans == -1:
                        ans = result
                    else:
                        ans = min(ans, result)
            table[money] = ans
            return ans

        return helper(amount)

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if not coins:
            return -1

        table = [-1] * (amount + 1)
        table[0] = 0
        inf = float('inf')

        for cur in range(1, amount + 1):
            table[cur] = min(table[cur - coin] if cur - coin >= 0 else inf for coin in coins) + 1
        return table[amount]


s = Solution()
# print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([338,26,303,41,167,331,485,239,332], 8966))
print(s.coinChange([413,213,453,20,150,321,254,396,487,234], 5629))