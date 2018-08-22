import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]

        def gen(prime):
            for ugly in uglies:
                yield ugly * prime

        iterater = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(iterater)
            if ugly != uglies[-1]:
                uglies.append(ugly)

        return uglies[n-1]

s = Solution()
print(s.nthSuperUglyNumber(100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]))
