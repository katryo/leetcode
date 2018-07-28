import collections

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        # memo[i][j]: max result of division [i, j]
        # j < j
        max_memo = [[(0.0, [])] * len(nums) for _ in range(len(nums))]
        min_memo = [[(0.0, [])] * len(nums) for _ in range(len(nums))]

        def dp(i, j):
            if max_memo[i][j][0] != 0.0:
                return max_memo[i][j][0], min_memo[i][j][0]

            if i+1 == j:
                max_memo[i][j] = (nums[i] / nums[j], [])
                min_memo[i][j] = (nums[i] / nums[j], [])
                return max_memo[i][j][0], min_memo[i][j][0]

            max_r_rest, min_r_rest = dp(i+1, j)
            max_l_rest, min_l_rest = dp(i, j-1)

            max_leftmost_over_rest = nums[i] / min_r_rest
            min_leftmost_over_rest = nums[i] / max_r_rest

            max_rest_over_rightmost = max_l_rest / nums[j]
            min_rest_over_rightmost = min_l_rest / nums[j]

            if max_leftmost_over_rest > max_rest_over_rightmost:
                max_memo[i][j] = (max_leftmost_over_rest, min_memo[i+1][j][1] + [(i+1, j)])
            else:
                max_memo[i][j] = (max_rest_over_rightmost, max_memo[i][j+1][1])

            if min_leftmost_over_rest > min_rest_over_rightmost:
                min_memo[i][j] = (min_rest_over_rightmost, min_memo[i][j-1][1])
            else:
                min_memo[i][j] = (min_leftmost_over_rest, max_memo[i-1][j][1] + [(i+1, j)])
            # max_memo[i][j] = max(max_leftmost_over_rest, max_rest_over_rightmost)
            # min_memo[i][j] = min(min_leftmost_over_rest, min_rest_over_rightmost)

            return max_memo[i][j][0], min_memo[i][j][0]

        res = dp(0, len(nums)-1)
        pairs = max_memo[0][len(nums)-1][1]

        START = 1
        END = 2
        ps = [0] * len(nums)

        starts = collections.defaultdict(int)
        ends = collections.defaultdict(int)
        for pair in pairs:
            starts[pair[0]] += 1
            ends[pair[1]] += 1

        ans = []
        for i in range(len(nums)):
            if i != 0:
                ans.append('/')
            for j in range(starts[i]):
                ans.append('(')
            ans.append(str(nums[i]))
            for j in range(ends[i]):
                ans.append(')')

        return ''.join(ans)

# s = Solution()
# print(s.optimalDivision([1000,100,10,2]))

# Given a list of positive integers, the adjacent integers will perform the float division.
# For example, [2,3,4] -> 2 / 3 / 4.
#
# However, you can add any number of parenthesis at any position to change the priority of operations.
# You should find out how to add parenthesis to get the maximum result,
# and return the corresponding expression in string format.
# Your expression should NOT contain redundant parenthesis.
#
# Example:
# Input: [1000,100,10,2]
# Output: "1000/(100/10/2)"
# Explanation:
# 1000/(100/10/2) = 1000/((100/10)/2) = 200
# However, the bold parenthesis in "1000/((100/10)/2)" are redundant,
# since they don't influence the operation priority. So you should return "1000/(100/10/2)".
#
# Other cases:
# 1000/(100/10)/2 = 50
# 1000/(100/(10/2)) = 50
# 1000/100/10/2 = 0.5
# 1000/100/(10/2) = 2
# Note:
#
# The length of the input array is [1, 10].
# Elements in the given array will be in range [2, 1000].
# There is only one optimal division for each test case.