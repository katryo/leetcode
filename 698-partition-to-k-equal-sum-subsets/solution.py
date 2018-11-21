class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        total = sum(nums)
        if total % k:
            return False
        target = total // k
        nums.sort(reverse=True)

        def backtrack(numbers, cur):
            if not numbers:
                return True

            for i in range(len(numbers)):
                if cur + numbers[i] == target:
                    if backtrack(numbers[:i] + numbers[i + 1:], 0):
                        return True
                elif cur + numbers[i] < target:
                    if backtrack(numbers[:i] + numbers[i + 1:], cur + numbers[i]):
                        return True
                else:
                    return False
            return False

        return backtrack(nums, 0)


# s = Solution()
# print(s.canPartitionKSubsets([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], 5))