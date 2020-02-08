from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # divide nums => segments of k items
        if not k:
            return []
        if not nums:
            return []

        segments = []
        seg = []
        for num in nums:
            seg.append(num)
            if len(seg) == k:
                segments.append(seg)
                seg = []
        if seg:
            segments.append(seg)

        n = len(nums)
        # Create left[i] and right[i]
        left = [float('-inf')] * n
        cur = float('-inf')
        prev_seg_i = -1
        for i in range(n):
            seg_i = i // k
            if prev_seg_i < seg_i:
                cur = float('-inf')
            prev_seg_i = seg_i
            cur = max(cur, nums[i])
            left[i] = cur

        right = [float('-inf')] * n
        cur = float('-inf')
        prev_seg_i = -1
        for i in range(n - 1, -1, -1):
            seg_i = i // k
            if prev_seg_i > seg_i:
                cur = float('-inf')
            prev_seg_i = seg_i
            cur = max(cur, nums[i])
            right[i] = cur

        ans = [0] * (n - k + 1)
        # [1,3,-1,-3,5,3,6,7],
        #      (     ^)
        # k == 4
        # right[2] ;;; left[4]
        # populate ans
        for i in range(k - 1, n):
            # k = 3
            # i = 2
            # i-k+1 = 0
            #                right[0],   left[2]
            ans[i - k + 1] = max(right[i - k + 1], left[i])
        return ans
