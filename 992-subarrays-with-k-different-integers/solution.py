# https://leetcode.com/articles/subarrays-with-k-different-integers/
from collections import Counter


class Window:
    def __init__(self):
        self.counter = Counter()
        self.kinds = 0

    def add(self, num):
        self.counter[num] += 1
        if self.counter[num] == 1:
            self.kinds += 1

    def remove(self, num):
        self.counter[num] -= 1
        if self.counter[num] == 0:
            self.kinds -= 1


class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        n = len(A)
        longest = Window()
        shortest = Window()

        left_longest = 0
        left_shortest = 0

        ans = 0

        for i, right in enumerate(A):
            longest.add(right)
            shortest.add(right)

            while longest.kinds > K:
                longest.remove(A[left_longest])
                left_longest += 1

            while shortest.kinds >= K:
                shortest.remove(A[left_shortest])
                left_shortest += 1

            ans += (left_shortest - left_longest)

        return ans



# s = Solution()
# print(s.subarraysWithKDistinct([2,2,1,2,2,2,1,1], 2))
# print(s.subarraysWithKDistinct([1,2,1,2,3], 2))
# print(s.subarraysWithKDistinct([1,2,1,3,4], 3))

