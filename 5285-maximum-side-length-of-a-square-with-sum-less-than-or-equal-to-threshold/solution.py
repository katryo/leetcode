from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        n = len(mat)
        m = len(mat[0])
        total_on_left = [[0] * m for _ in range(n)]

        for i in range(n):
            cur = 0
            for j in range(m):
                cur += mat[i][j]
                total_on_left[i][j] = cur

        total_on_up_left = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    total_on_up_left[i][j] = total_on_left[i][j]
                else:
                    total_on_up_left[i][j] = total_on_up_left[i-1][j] + total_on_left[i][j]

        # for i in range(n):
        #     print(total_on_up_left[i])

        # O(1)
        def bottomright_length_sum(bottom, right, length):
            total = total_on_up_left[bottom][right]

            if bottom - length >= 0:
                up_dec = total_on_up_left[bottom-length][right]
            else:
                up_dec = 0

            if right - length >= 0:
                left_dec = total_on_up_left[bottom][right - length]
            else:
                left_dec = 0

            if bottom - length >= 0 and right - length >= 0:
                up_left_inc = total_on_up_left[bottom-length][right-length]
            else:
                up_left_inc = 0
            return total - up_dec - left_dec + up_left_inc

        def check(mid):
            for i in range(n):
                for j in range(m):
                    if i < mid-1:
                        continue
                    if j < mid-1:
                        continue
                    total = bottomright_length_sum(i, j, mid)
                    if total <= threshold:
                        return True
            return False

        lo = 0
        hi = min(m, n)
        mid = hi

        while lo < hi:
            found = check(mid)
            if found:
                lo = mid
            else:
                hi = mid-1
            mid = (lo + hi) // 2
            if lo == mid:
                if check(lo+1):
                    return lo+1
                else:
                    return lo

        return lo


# s = Solution()
# print(s.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4))
# print(s.maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1))
# print(s.maxSideLength([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6))
# print(s.maxSideLength([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184))
