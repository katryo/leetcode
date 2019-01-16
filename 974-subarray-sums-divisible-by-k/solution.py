from collections import Counter


class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        table = [0] * len(A)
        table[0] = A[0] % K
        for i in range(1, len(A)):
            table[i] = (table[i - 1] + A[i]) % K

        counter = Counter()
        ans = 0
        for i in range(len(A)):
            num = table[i]
            if num in counter:
                ans += counter[num]
            if num % K == 0:
                ans += 1
            counter[num] += 1
        return ans


# s = Solution()
# print(s.subarraysDivByK([-1,2,9], 2))
# print(s.subarraysDivByK([4,5,0,-2,-3,1], 5))
