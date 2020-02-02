from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if k >= n // 2:
            ans = 0
            for i in range(n-1):
                if prices[i] < prices[i+1]:
                    ans += prices[i+1] - prices[i]
            return ans

        withstock = [[float('-inf')] * (k+1) for _ in range(n)]
        withoutstock = [[float('-inf')] * (k+1) for _ in range(n)]

        withoutstock[0][0] = 0
        withstock[0][0] = - prices[0]

        for i in range(1, n):
            for j in range(k+1):
                withstock[i][j] = max(withstock[i-1][j], withoutstock[i-1][j] - prices[i])
                if j == 0:
                    withoutstock[i][0] = withoutstock[i-1][j]
                else:
                    withoutstock[i][j] = max(withstock[i-1][j-1] + prices[i], withoutstock[i-1][j])

        # print(withoutstock)
        # print(withstock)
        return max(withoutstock[n-1])


# s = Solution()
# print(s.maxProfit(2, [2, 4, 1]))
# print(s.maxProfit(2, [3,2,6,5,0,3]))
# print(s.maxProfit(2, [3,3,5,0,0,3,1,4]))
# print(s.maxProfit(4, [1,2,4,2,5,7,2,4,9,0]))

