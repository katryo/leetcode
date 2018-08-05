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

        stol = [nums[0]]
        # stol[i] is the smallest tail of the length of i+1
        # [6, 4, 7, 2, 3] then
        # stol[0] == 6 => 4 => 2
        # stol[1] == 7 => 3
        # stol[1] is updated when 7 is found since stol[0] == 4 and the new num is 7.
        # stol is a sorted array.

        # Find the smallest num in stol greater than target
        # If not found, returns len(stol) which means we append the target to stol.
        def binary_search(target):
            assert len(stol) > 0
            lo = 0
            hi = len(stol)
            # We search the smallest num in stol greater than target in the range of [lo, hi)
            while lo < hi:
                mid = (lo + hi) // 2
                if stol[mid] < target:
                    lo = mid+1
                else:
                    hi = mid
            return lo

        for num in nums:
            idx = binary_search(num)
            if idx == len(stol):
                stol.append(num)
            else:
                stol[idx] = num
        return len(stol)


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
