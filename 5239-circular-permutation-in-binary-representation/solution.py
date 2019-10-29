from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:

        cur = [0]
        for i in range(n):
            size = len(cur)
            for j in range(size-1, -1, -1):
                cur.append(cur[j] + (1 << i))

        start_i = -1
        for i in range(1 << n):
            if cur[i] == start:
                start_i = i

        result = cur[start_i:] + cur[:start_i]
        return result

# s = Solution()
# print(s.circularPermutation(3, 1))
# print(s.circularPermutation(4, 1))
# print(s.circularPermutation(1, 0))
# print(s.circularPermutation(1, 1))
# print(s.circularPermutation(2, 3))
# print(s.circularPermutation(3, 2))
