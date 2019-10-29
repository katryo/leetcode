from typing import List


class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)

        hi_lo = -1
        # 1. Find rightmost high > low
        for i in range(n-1):
            if A[i] > A[i+1]:
                hi_lo = i
        if hi_lo == -1:
            # Input: [1, 1, 5]
            # Output: [1, 1, 5]
            return A

        hival = A[hi_lo]
        ans = hi_lo + 1
        for i in range(hi_lo+1, n):
            if A[ans] < A[i] < hival:
                ans = i
        A[hi_lo], A[ans] = A[ans], A[hi_lo]
        return A


s = Solution()
print(s.prevPermOpt1([3,2,1]))
print(s.prevPermOpt1([1,9,4,6,7]))
print(s.prevPermOpt1([1,1,5]))
print(s.prevPermOpt1([3,1,1,3]))
