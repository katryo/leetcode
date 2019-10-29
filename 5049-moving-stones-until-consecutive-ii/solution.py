from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)

        i = 0
        low = n

        high_left = stones[n-1] - stones[1] - n + 2
        high_right = stones[n-2] - stones[0] - n + 2
        high = max(high_left, high_right)

        for j in range(n):
            while stones[j] - stones[i] >= n:
                i += 1
            if j - i + 1 == n - 1 and stones[j] - stones[i] == n-2:
                low = min(low, 2)
            else:
                low = min(low, n - (j-i+1))
        return [low, high]

