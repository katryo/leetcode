# https://leetcode.com/problems/longest-increasing-subsequence/solution/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        table = [1] * len(nums)
        ans = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    table[i] = max(table[i], table[j]+1)
                    ans = max(ans, table[i])
        return ans


    def lengthOfLIS2(self, nums):
        if not nums:
            return 0
        arr = [nums[0]]

        # Returns the lowest idx of # equal to or greater than target
        def binary_search(target):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] > target:
                    hi = mid
                else:
                    lo = mid+1
            return lo

        for i in range(1, len(nums)):
            idx_in_arr = binary_search(nums[i])
            # if the target is greater than the current max, append it to the arr.
            if idx_in_arr == len(arr):
                arr.append(nums[i])
            else:
                arr[idx_in_arr] = nums[i]
        return len(arr)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
    print(s.lengthOfLIS([]))
    print(s.lengthOfLIS([0]))
    print(s.lengthOfLIS([1]))
    print(s.lengthOfLIS([0, 1]))
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print('--')

    print(s.lengthOfLIS2([1,3,6,7,9,4,10,5,6]))
    print(s.lengthOfLIS2([]))
    print(s.lengthOfLIS2([0]))
    print(s.lengthOfLIS2([1]))
    print(s.lengthOfLIS2([0, 1]))
    print(s.lengthOfLIS2([10,9,2,5,3,7,101,18]))
