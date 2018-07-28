import collections


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        summations = []
        summation = 0
        for num in nums:
            summation += num
            summations.append(summation)

        table = collections.defaultdict(int)

        ans = 0
        table[0] = 1

        for summation in summations:
            if summation-k in table:
                ans += table[summation-k]
            table[summation] += 1
        return ans


s = Solution()
print(s.subarraySum([1], 0))
# print(s.subarraySum([1, 1], 0))
# print(s.subarraySum([1], 1))
# print(s.subarraySum([1], 2))
# print(s.subarraySum([0], 1))
# print(s.subarraySum([0], 0))
# print(s.subarraySum([0, 0], 0))
# print(s.subarraySum([0, 0, 0], 0))
# print(s.subarraySum([-1, 1], 0))
# print(s.subarraySum([-1, 1, 1, -1], 0))
# print(s.subarraySum([1, 1, 1], 2))
# print(s.subarraySum([1, 1, 1, 1], 2))
# print(s.subarraySum([1, 1, 1, 1, 1], 2))
# print(s.subarraySum([1, 2, 1, 1, 1], 2))
# print(s.subarraySum([1, 2, -1, 1, 1], 2))
# print(s.subarraySum([-1, 2, -1, 5, -1], 3))
