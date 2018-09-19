import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets = {}
        bucket_width = t+1

        if k <= 0:
            return False

        if t < 0:
            return False

        if bucket_width == 0:
            seen = set()
            for i in range(len(nums)):
                if nums[i] in seen:
                    return True
                if i >= k:
                    seen.remove(nums[i-k])
                seen.add(nums[i])
            return False

        for i in range(len(nums)):
            bucket = nums[i] // bucket_width
            if bucket in buckets:
                return True
            if bucket+1 in buckets and buckets[bucket+1] - nums[i] <= t:
                return True
            if bucket-1 in buckets and nums[i] - buckets[bucket-1] <= t:
                return True
            buckets[bucket] = nums[i]
            if i >= k:
                buckets.pop(nums[i-k] // bucket_width)
        return False

    # def containsNearbyAlmostDuplicate(self, nums, k, t):
    #     if not nums or k == 0:
    #         return False
    #     sorted_num = []
    #     for i in range(len(nums)):
    #         num = nums[i]
    #         loc = bisect.bisect(sorted_num, num)
    #         if len(sorted_num)-1 >= loc and sorted_num[loc] - num <= t:
    #             return True
    #         if loc > 0 and num - sorted_num[loc-1] <= t:
    #             return True
    #         bisect.insort_left(sorted_num, num)
    #         if i >= k:
    #             sorted_num.remove(nums[i-k])
    #
    #     return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([2, 1], 1, 1))
    print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
    print(s.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
    print(s.containsNearbyAlmostDuplicate([-1, -1], 1, -1))
    print(s.containsNearbyAlmostDuplicate([-1, -1], 0, -1))

