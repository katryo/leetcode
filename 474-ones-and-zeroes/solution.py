import collections

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        nums = []
        for st in strs:
            counter = collections.Counter(st)
            nums.append((counter['0'], counter['1']))

        memo = [[[-1] * len(strs) for _ in range(n+1)] for _ in range(m+1)]

        def helper(i, j, k):
            if i < 0:
                return 0
            if j < 0:
                return 0
            if k < 0:
                return 0
            if memo[i][j][k] != -1:
                return memo[i][j][k]

            zeros, ones = nums[k]
            if k == 0:
                if i >= zeros and j >= ones:
                    memo[i][j][k] = 1
                    return 1
                memo[i][j][k] = 0
                return 0

            # memo[i][j][k] Given i zeroes, j ones, and k strings, the max #strings

            if zeros <= i and ones <= j:
                memo[i][j][k] = max(helper(i, j, k-1),
                                    helper(i-zeros, j-ones, k-1) + 1)
            else:
                memo[i][j][k] = helper(i, j, k-1)
            return memo[i][j][k]

        return helper(m, n, len(strs)-1)


# s = Solution()
# print(s.findMaxForm(["10", "0001"], 5, 3))
# print(s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
# print(s.findMaxForm(["10", "0", "1"], 1, 1))
# print(s.findMaxForm(["00", "000"], 1, 10))
