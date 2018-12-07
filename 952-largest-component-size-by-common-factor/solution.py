from collections import defaultdict
from collections import Counter


class DSU:
    def __init__(self, size):
        self.parents = list(range(size))

    def union(self, a, b):
        a_p = self.find(a)
        b_p = self.find(b)
        self.parents[a_p] = b_p

    def find(self, target):
        mid_points = set()
        while self.parents[target] != target:
            mid_points.add(target)
            target = self.parents[target]
        for point in mid_points:
            self.parents[point] = target
        return target

class Solution:
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        factors = []

        for a in A:
            factors.append(self.sieve(a))

        primes = list({factor for factor_list in factors for factor in factor_list})
        prime_to_idx = {prime: i for i, prime in enumerate(primes)}
        # print(prime_to_idx)

        dsu = DSU(len(primes))

        for factor_list in factors:
            for factor in factor_list:
                dsu.union(prime_to_idx[factor], prime_to_idx[factor_list[0]])

        counter = Counter(dsu.find(prime_to_idx[factor_list[0]]) for factor_list in factors if len(factor_list) > 0)
        return max(counter.values())

    def sieve(self, num):
        if num == 1:
            return []
        n = 2
        ans = []
        while n * n <= num:
            if num % n == 0:
                ans.append(n)
            while num % n == 0:
                num //= n
            n += 1
        if num > 1 or not ans:
            ans.append(num)
        # print(ans)
        return ans


# s = Solution()
# print(s.largestComponentSize(list(range(1, 10))))
# print(s.largestComponentSize([2,3,6,7,4,12,21,39]))
# print(s.largestComponentSize([4,6,15,35]))
# print(s.largestComponentSize([6]))
