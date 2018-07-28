# Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
# and the length of an increasing subsequence should be at least 2 .
#
# Example:
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# Note:
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates,
# and two equal integers should also be considered as a special case of increasing sequence.


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 2:
            return []

        seen = set()
        # Assume arr is sorted
        def inc_subs_rec(arr):
            if len(arr) < 2:
                return []
            result = set()
            subsequence_begins_from_next = inc_subs_rec(arr[1:])
            for subs in subsequence_begins_from_next:
                if arr[0] <= subs[0]:
                    result.add(tuple([arr[0]] + list(subs)))

            num_set = set()
            pair_set = set()
            for num in arr[1:]:
                num_set.add(num)
            for num in num_set:
                if arr[0] <= num:
                    pair_set.add((arr[0], num))
            for pair in pair_set:
                result.add(pair)
            result |= set(subsequence_begins_from_next)

            return result

        set_of_tupples = inc_subs_rec(nums)
        ans = []
        for t in set_of_tupples:
            ans.append(list(t))
        return ans


s = Solution()
# print(s.findSubsequences([3, 4, 5]))
# print(s.findSubsequences([4, 3, 2, 1]))
# print(s.findSubsequences([1,1,1]))
ans = s.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1])
for a in ans:
    print(a)
