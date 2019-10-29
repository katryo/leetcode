from typing import List


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        table = [[float('inf')] * n for _ in range(n)]

        def helper(first, last):
            if table[first][last] != float('inf'):
                return table[first][last]
            if last - first == 2:
                table[first][last] = A[first] * A[first+1] * A[first+2]
                return table[first][last]
            mul = A[first] * A[last]
            ans = mul * A[first+1] + helper(first+1, last)
            for i in range(first+2, last-1):
                cand = mul * A[i] + helper(first, i) + helper(i, last)
                ans = min(ans, cand)
            ans = min(ans, helper(first, last-1) + mul * A[last-1])
            table[first][last] = ans
            return ans

        return helper(0, n-1)


# s = Solution()
# print(s.minScoreTriangulation([35,73,90,27,71,80,21,33,33,13,48,12,68,70,80,36,66,3,70,58]))
# print(s.minScoreTriangulation([3,7,4,5]))
# print(s.minScoreTriangulation([1,3,1,4,1,5]))
