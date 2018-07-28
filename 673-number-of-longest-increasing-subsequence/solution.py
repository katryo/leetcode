class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [-1] * len(nums)
        dp[0] = 1
        counts = [-1] * len(nums)
        counts[0] = 1

        for i in range(1, len(nums)):
            longest_non_largers_length = -1
            num_of_longests = -1
            for j in range(i):
                if nums[j] < nums[i]:
                    if longest_non_largers_length == dp[j]:
                        num_of_longests += counts[j]
                    elif longest_non_largers_length < dp[j]:
                        num_of_longests = counts[j]
                        longest_non_largers_length = dp[j]
            if longest_non_largers_length == -1:
                dp[i] = 1
                counts[i] = 1
            else:
                dp[i] = longest_non_largers_length + 1
                counts[i] = num_of_longests

        longest_length = -1
        for i in range(len(nums)):
            longest_length = max(longest_length, dp[i])
        end_indexes_with_longest = []
        for i in range(len(nums)):
            if dp[i] == longest_length:
                end_indexes_with_longest.append(i)
        ans = 0
        for i in end_indexes_with_longest:
            ans += counts[i]
        print(counts)
        return ans


s = Solution()
# print(s.findNumberOfLIS([1,2,4,3,5,4,7,2]))
# print(s.findNumberOfLIS([1,3,5,4,7]))
# print(s.findNumberOfLIS([2,2,2,2,2]))
print(s.findNumberOfLIS([1,1,1,2,2,2,3,3,3]))
