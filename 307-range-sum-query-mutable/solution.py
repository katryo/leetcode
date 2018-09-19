# import math
class NumArray:
    def __init__(self, nums):
        self.nums = nums
        if len(nums) > 0:
            length = len(nums)
            tree = [0] * (len(nums) * 2 - 1)

            self.two_power_len = 1
            while self.two_power_len < len(nums):
                self.two_power_len *= 2

            for i in range(len(nums)):
                tree[length-1+i] = nums[i]
            for i in range(length-2, -1, -1):
                tree[i] = tree[2*i+1] + tree[2*i + 2]
            self.tree = tree
        else:
            self.tree = []

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] += diff
        idx = len(self.nums) - 1 + i
        while idx:
            self.tree[idx] += diff
            idx = (idx-1) // 2
        self.tree[0] += diff

    def sumRange(self, i, j):
        def query(a, b, k, left, right):
            if a <= left and right <= b:
                return self.tree[k]
            if 2 * len(self.nums)-2 < k*2+1:
                return 0
            left_sum = query(a, b, k * 2 + 1, left, (left + right) // 2)
            right_sum = query(a, b, k * 2 + 2, (left + right) // 2, right)
            return left_sum + right_sum

        return query(i, j+1, 0, 0, self.two_power_len)



# class NumArray:
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         sq_seg_len = math.floor(math.sqrt(len(nums)))
#         if sq_seg_len == 0:
#             return
#         sq_seg_count = math.ceil(len(nums) / sq_seg_len)
#         sq_segs = [0] * sq_seg_count
#
#         for i, num in enumerate(nums):
#             sq_segs[i // sq_seg_len] += num
#
#         self.sq_seg_len = sq_seg_len
#         self.sq_segs = sq_segs
#         self.nums = nums
#
#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: void
#         """
#         sq_seg_idx = i // self.sq_seg_len
#         diff = val - self.nums[i]
#         self.nums[i] = val
#         self.sq_segs[sq_seg_idx] += diff
#
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#
#         ans = 0
#         seg_idx_start = i // self.sq_seg_len
#         seg_idx_end = j // self.sq_seg_len
#         if seg_idx_start == seg_idx_end:
#             for k in range(i, j+1):
#                 ans += self.nums[k]
#             return ans
#
#         for k in range(i, self.sq_seg_len * (seg_idx_start+1)):
#             ans += self.nums[k]
#         for k in range(seg_idx_start+1, seg_idx_end):
#             ans += self.sq_segs[k]
#         for k in range(self.sq_seg_len * seg_idx_end, j+1):
#             ans += self.nums[k]
#         return ans


# s = NumArray([1, 3, 5])
# print(s.sumRange(0, 2))
# s.update(1, 2)
# print(s.sumRange(0, 2))
# #
# s = NumArray([-1])
# print(s.sumRange(0, 0))
# s.update(0, 1)
# print(s.sumRange(0, 0))
#
# s = NumArray([9, -8])
# s.update(0, 3)
# print(s.sumRange(1, 1))
# print(s.sumRange(0, 2))

s = NumArray([0, 9, 5, 7, 3])
print(s.sumRange(4, 4))

# ["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
# [[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
