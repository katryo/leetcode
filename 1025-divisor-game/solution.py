import math
from functools import lru_cache


class Solution:
    def divisorGame(self, N: int) -> bool:
        table = [0] * 1001
        table[1] = -1
        table[2] = 1

        for i in range(3, 1001):
            can_win = False
            for j in range(1, i):
                if i % j == 0:
                    if table[i-j] == -1:
                        can_win = True
                        table[i] = True
                        break
            if not can_win:
                table[i] = -1
        return table[N] == 1


s = Solution()
print(s.divisorGame(1))
print(s.divisorGame(2))
print(s.divisorGame(3))
print(s.divisorGame(4))
print(s.divisorGame(1000))
