class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        def b_search(left, right, total):
            while left <= right < len(nums):
                mid = (left + right) // 2
                if nums[mid] >= total:
                    right = mid-1
                else:
                    left = mid+1
            return left

        ans = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                continue
            k = i+2
            for j in range(i+1, len(nums)-1):
                while k < len(nums) and nums[i]+nums[j] > nums[k]:
                    k += 1
                ans += k - j - 1
        return ans

# s = Solution()
# print(s.triangleNumber([0, 0, 0]))
# print(s.triangleNumber([2,2,3,4]))
# print(s.triangleNumber([1,1,3,4]))
# print(s.triangleNumber([1,2,3,4,5,6]))
