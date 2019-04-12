from typing import List


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n-1) % (K-1):
            return -1
        INF = float('inf')
        prefix = [0]
        for stone in stones:
            prefix.append(prefix[-1] + stone)

        memo = {}

        # Returns sum([x:y+1])
        def total(x, y):
            return prefix[y + 1] - prefix[x]

        def rec(i, j, m):
            length = j - i + 1
            piles_to_reduce = length - m
            if piles_to_reduce % (K - 1):
                return INF
            if (i, j, m) in memo:
                return memo[i, j, m]
            if i == j:
                if m == 1:
                    res = 0
                else:
                    res = -1
            else:
                if m == 1:
                    res = rec(i, j, K) + total(i, j)
                else:
                    res = INF
                    for mid in range(i, j, K - 1):
                        res = min(res, rec(i, mid, 1) + rec(mid + 1, j, m - 1))
            memo[i, j, m] = res
            return res

        res = rec(0, n - 1, 1)
        if res == INF:
            return -1
        return res


# s = Solution()
# print(s.mergeStones([3, 2, 4, 1], 2))
# print(s.mergeStones([3, 2, 4, 1], 3))
# print(s.mergeStones([2, 1], 2))
# print(s.mergeStones([3, 5, 1, 2, 6], 3))
# print(s.mergeStones([69, 39, 79, 78, 16, 6, 36, 97, 79, 27, 14, 31, 4], 2))
