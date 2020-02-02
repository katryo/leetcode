from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        dp = [0] * n

        cur = 0
        for i in range(n):
            cur = cur ^ arr[i]
            dp[i] = cur

        q = len(queries)
        ans = [0] * q
        for i in range(q):
            l, r = queries[i]
            if not l:
                ans[i] = dp[r]
            else:
                ans[i] = dp[r] ^ dp[l-1]
        return ans


# s = Solution()
# print(s.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
# print(s.xorQueries([4,8,2,10],  [[2,3],[1,3],[0,0],[0,3]]))
# print(s.xorQueries([16],  [[0, 0],[0,0],[0,0]]))
