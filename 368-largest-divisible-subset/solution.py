from copy import deepcopy


class Solution(object):
    maxcount_set = (0, set())

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()

        greatest_set_ends_at = [set()] * len(nums)
        greatest_set_ends_at[0].add(nums[0])

        ans = [nums[0]]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(greatest_set_ends_at[j])+1 > len(greatest_set_ends_at[i]):
                        copied_set = deepcopy(greatest_set_ends_at[j])
                        copied_set.add(nums[i])
                        greatest_set_ends_at[i] = copied_set

                        if len(copied_set) > len(ans):
                            ans = list(copied_set)

        return ans


# s = Solution()
# print(s.largestDivisibleSubset([1, 2, 3]))
# print(s.largestDivisibleSubset([1, 2, 4, 8]))
# print(s.largestDivisibleSubset([1, 2, 4, 8, 9, 72]))
# print(s.largestDivisibleSubset([3, 9, 2]))
# print(s.largestDivisibleSubset([3, 9, 18, 200]))
