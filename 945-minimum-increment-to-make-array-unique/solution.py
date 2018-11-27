from collections import Counter


class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counter = Counter(A)
        taken = []
        ans = 0

        for x in range(40000):
            if counter[x] >= 2:
                taken.extend([x] * (counter[x]-1))
            elif taken and counter[x] == 0:
                ans += (x - taken.pop())
        return ans

s = Solution()
print(s.minIncrementForUnique([3,2,1,2,1,7]))
print(s.minIncrementForUnique([2,1,1]))
