# https://rcoh.me/posts/linear-time-median-finding/

def get_median(numbers):
    def pick_pivot(arr):
        if len(arr) < 5:
            return sorted(arr)[len(arr)//2]
        chunks = chunked(arr, 5)

        full_chunks = [chunk for chunk in chunks if len(chunk) == 5]
        sorted_chunks = [sorted(chunk) for chunk in full_chunks]
        medians = [chunk[2] for chunk in sorted_chunks]
        return get_median(medians)

    def chunked(arr, size):
        return [arr[i:i + size] for i in range(0, len(arr), size)]

    def partition(nums, target_idx):
        pivot = pick_pivot(nums)
        smaller = [num for num in nums if num < pivot]
        same = [num for num in nums if num == pivot]
        greater = [num for num in nums if num > pivot]
        if len(smaller) > target_idx:
            return partition(smaller, target_idx)
        if len(smaller) + len(same) > target_idx:
            return pivot
        else:
            return partition(greater, target_idx-len(smaller)-len(same))

    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        mid -= 1

    return partition(numbers, mid)


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        median = get_median(nums)
        left = 0
        i = 0
        right = len(nums) - 1

        def v_idx(idx):
            return (1 + 2 * idx) % (len(nums) | 1)

        for i in range(len(nums)):
            print(v_idx(i))

        while i <= right:
            if nums[v_idx(i)] > median:
                nums[v_idx(left)], nums[v_idx(i)] = nums[v_idx(i)], nums[v_idx(left)]
                left += 1
                i += 1
            elif nums[v_idx(i)] < median:
                nums[v_idx(i)], nums[v_idx(right)] = nums[v_idx(right)], nums[v_idx(i)]
                right -= 1
            else:
                i += 1
        return nums


s = Solution()
# print(s.wiggleSort([1, 3, 4]))
print(s.wiggleSort([1, 2, 3, 4, 5, 6, 7]))

# print(get_median([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 2, 2, 2]))
# print(get_median([1, 2, 3]))
# print(get_median([1, 2, 3, 4]))
