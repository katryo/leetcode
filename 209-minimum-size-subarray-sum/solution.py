class Solution:
    def minSubArrayLen(self, s, nums):
        total = 0
        if not nums:
            return 0
        totals = [0]
        for num in nums:
            total += num
            totals.append(total)

        ans = len(nums)+1
        for i in range(len(totals)):
            hi = len(totals)-1
            lo = i
            # [lo, hi]
            while lo < hi:
                mid = (lo+hi) // 2
                summation = totals[mid]-totals[i]
                if summation < s:
                    lo = mid+1
                else:
                    hi = mid
            if totals[lo] - totals[i] >= s:
                ans = min(ans, lo-i)
        if ans == len(nums)+1:
            return 0
        return ans


# if __name__ == '__main__':
#     s = Solution()
#     print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
#     print(s.minSubArrayLen(10, [2,3,1,2,4,3]))

    # def minSubArrayLen(self, s, nums):
    #     """
    #     :type s: int
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #     ans = len(nums) + 1
    #     right = 0
    #     total = nums[0]
    #     for left in range(len(nums)):
    #         while right < len(nums) - 1 and total < s:
    #             right += 1
    #             total += nums[right]
    #         if total >= s:
    #             ans = min(ans, right - left + 1)
    #         total -= nums[left]
    #     if ans == len(nums) + 1:
    #         return 0
    #     return ans


