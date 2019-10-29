from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        total = 0
        tot = 0
        n = len(customers)
        gru = [0] * n
        for i in range(n):
            if grumpy[i]:
                total += customers[i]
            else:
                tot += customers[i]
            gru[i] = total

        # n = 10
        # X = 1
        # range(n-X): 0...8
        ans = tot
        for start in range(n):
            end = start + X
            if end > n:
                break
            if start == 0:
                cand = tot + gru[end-1]
            else:
                cand = tot + (gru[end-1] - gru[start-1])
            ans = max(ans, cand)
        return ans


# s = Solution()
# print(s.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
# print(s.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 1))
# print(s.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 8))
