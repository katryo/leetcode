class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l) // 2
            while nums[l] == nums[mid] and l < mid:
                l += 1
            if nums[mid] == target:
                return True
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:  # nums[l] > nums[mid]
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return False

    # def search(self, nums, target):
    #     l = 0
    #     r = len(nums)-1
    #     while l <= r:
    #         mid = l + (r-l)//2
    #         if nums[mid] == target:
    #             return True
    #         while l < mid and nums[l] == nums[mid]:
    #             l += 1
    #         if nums[l] <= nums[mid]:
    #             if nums[l] <= target < nums[mid]:
    #                 r = mid - 1
    #             else:
    #                 l = mid + 1
    #         else:  # nums[l] > nums[mid]
    #             if nums[mid] < target <= nums[r]:
    #                 l = mid + 1
    #             else:
    #                 r = mid - 1
    #     return False

    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: bool
    #     """
    #     if not nums:
    #         return False
    #
    #     def helper(lo, hi):
    #         if lo == hi:
    #             return lo
    #         if lo + 1 == hi:
    #             if nums[lo] > nums[hi]:
    #                 return lo
    #             else:
    #                 return hi
    #         mid = (lo + hi) // 2
    #         if nums[mid] > nums[hi]:
    #             return helper(mid, hi)
    #         if nums[lo] > nums[mid]:
    #             return helper(lo, mid)
    #         right = helper(mid, hi)
    #         left = helper(lo, mid)
    #         if right == hi and left == mid:
    #             return hi
    #         if right == hi:
    #             return left
    #         else:
    #             return right
    #
    #     pivot = helper(0, len(nums) - 1)
    #
    #     def b_search(start, end):
    #         if start >= end:
    #             return False
    #         mid = (start + end) // 2
    #         if nums[mid] == target:
    #             return True
    #         if nums[mid] < target:
    #             return b_search(mid + 1, end)
    #         else:
    #             return b_search(start, mid)
    #
    #     # print(pivot)
    #     if pivot == len(nums)-1:
    #         return b_search(0, len(nums))
    #     if target < nums[0]:
    #         return b_search(pivot+1, len(nums))
    #     else:
    #         return b_search(0, pivot+1)

s = Solution()
print(s.search([1,1,1,3,1], 3))
print(s.search([1,3,1,1,1], 3))
