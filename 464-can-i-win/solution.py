
# In the "100 game," two players take turns adding, to a running total,
# any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of numbers of 1..15
# without replacement until they reach a total >= 100.
#
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players play optimally.
#
# You can always assume that maxChoosableInteger will not be larger than 20
# and desiredTotal will not be larger than 300.


# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
#
# Output:
# false
#
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        if (maxChoosableInteger + 1) * maxChoosableInteger // 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        nums = [i+1 for i in range(maxChoosableInteger)]

        calculated = {}

        def dfs(nums, desired):
            key = str(nums)
            if key in calculated:
                return calculated[key]
            if desired <= nums[-1]:
                calculated[key] = True
                return True
            if desired <= 0:
                calculated[key] = False
                return False

            for i in range(len(nums)):
                # The opponent loses!
                if not dfs(nums[:i] + nums[i+1:], desired - nums[i]):
                    calculated[key] = True
                    return True
            calculated[key] = False
            return False

        return dfs(nums, desiredTotal)


# s = Solution()
# print(s.canIWin(10, 11))
# print(s.canIWin(10, 3))
# print(s.canIWin(2, 3))
# print(s.canIWin(16, 100))
