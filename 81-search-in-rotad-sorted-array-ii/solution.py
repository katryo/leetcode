class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True

            while nums[l] == nums[mid] and l < mid:
                l += 1

            # 1st half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                # 1st half is not sorted. 2nd is.
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return False

# s = Solution()
# print(s.search([2,5,6,0,0,1,2], 0))
# print(s.search([2,5,6,0,0,1,2], 3))
