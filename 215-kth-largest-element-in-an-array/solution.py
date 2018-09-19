class Solution:
    def findKthLargest(self, nums, k):
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k - 1]

    def findKthLargest2(self, nums, k):
        pivot = nums[0]
        smaller = [n for n in nums if n < pivot]
        same = [n for n in nums if n == pivot]
        greater = [n for n in nums if n > pivot]
        if k <= len(greater):
            return self.findKthLargest2(greater, k)
        if k <= len(greater) + len(same):
            return same[0]
        return self.findKthLargest2(smaller, k - (len(greater) + len(same)))

    def bubble_sort(self, nums, k):
        for size in range(len(nums)-(k-1)):
            for i in range(size-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums[-k]

if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest2([2, 5, 2, 2, 7, 8, 9, 9], 4))
    print(s.findKthLargest([2, 5, 2, 2, 7, 8, 9, 9], 4))
    print(s.bubble_sort([2, 5, 2, 2, 7, 8, 9, 9], 4))
