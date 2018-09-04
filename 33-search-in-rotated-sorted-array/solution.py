class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # [start, end]
        def get_pivot_idx(start, end):
            if nums[start] <= nums[end]:
                return start
            middle = (start+end) // 2
            if nums[end] < nums[middle]:
                return get_pivot_idx(middle+1, end)
            else:
                return get_pivot_idx(start, middle)

        # [start, end)
        def b_search(start, end):
            if start == end:
                return -1
            middle = (start+end)//2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                return b_search(middle+1, end)
            else:
                return b_search(start, middle)

        if not nums:
            return -1
        pivot_idx = get_pivot_idx(0, len(nums)-1)

        if target == nums[0]:
            return 0
        if target < nums[0]:
            return b_search(pivot_idx, len(nums))
        else:
            if pivot_idx == 0:
                return b_search(0, len(nums))
            else:
                return b_search(0, pivot_idx)

s = Solution()
print(s.search([], 0))
print(s.search([0], 0))
print(s.search([0], 1))
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([4,5,6,7,0,1,2], 4))
print(s.search([4,5,6,7,0,1,2], 6))
print(s.search([4,5,6,7,0,1,2], 7))
print(s.search([1, 3], 0))
print(s.search([1, 3], 1))
print(s.search([1, 3], 3))
print(s.search([2,4,7,9,0], 9))
print(s.search([3, 5, 1], 1))
