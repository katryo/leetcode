from typing import List
from functools import lru_cache


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)

        l_total = [0] * n
        m_total = [0] * n

        lsum = 0
        start = 0
        for i in range(n):
            lsum += A[i]
            if i - start + 1 == L:
                l_total[start] = lsum
                lsum -= A[start]
                start += 1

        msum = 0
        start = 0
        for i in range(n):
            msum += A[i]
            if i - start + 1 == M:
                m_total[start] = msum
                msum -= A[start]
                start += 1

        max_from_left = [float('-inf')] * n
        cur = m_total[0]
        for i in range(n):
            cur = max(cur, m_total[i])
            max_from_left[i] = cur

        max_from_right = [float('-inf')] * n
        cur = m_total[n-1]
        for i in range(n-1, -1, -1):
            cur = max(cur, m_total[i])
            max_from_right[i] = cur

        ans = 0
        for i in range(n-L+1):
            l_val = l_total[i]
            if 0 <= i-M and i+L+1 < n:
                m_val = max(max_from_left[i-M], max_from_right[i+L+1])
            elif 0 <= i-M:
                m_val = max_from_left[i-M]
            elif i+L+1 < n:
                m_val = max_from_right[i+L+1]
            else:
                continue
            ans = max(ans, l_val + m_val)
        return ans


# s = Solution()
# print(s.maxSumTwoNoOverlap([1, 2, 3, 4, 5], 1, 2))
# print(s.maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0], 3, 2))
# print(s.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], 4, 3))
# print(s.maxSumTwoNoOverlap([1,0,3], 1, 2))
