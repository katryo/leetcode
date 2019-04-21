from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        table = [{} for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in table[j]:
                    if diff in table[i]:
                        table[i][diff] = max(table[i][diff], table[j][diff]+1)
                    else:
                        table[i][diff] = table[j][diff] + 1
                else:
                    table[i][diff] = 2
                ans = max(ans, table[i][diff])
        return ans


# s = Solution()
# print(s.longestArithSeqLength([3, 6, 9, 12]))
# print(s.longestArithSeqLength([9,4,7,2,10]))
# print(s.longestArithSeqLength([20,1,15,3,10,5,8]))
