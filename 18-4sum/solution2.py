from collections import defaultdict


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        summed = defaultdict(list)
        for i, num in enumerate(nums):
            for j in range(i):
                summed[num + nums[j]].append((j, i, nums[j], num))

        ans = set()
        for two_sum in summed:
            diff = target - two_sum
            if diff in summed:
                combis = summed[diff]
                for x, y, valx, valy in combis:
                    for a, b, vala, valb in summed[two_sum]:
                        if x != a and x != b and y != a and y != b:
                            ans.add(tuple(sorted([valx, valy, vala, valb])))
        return [list(a) for a in ans]


# s = Solution()
# print(s.fourSum([3, 1, 5, 3, 6, 7, 3, 1, 10], 14))