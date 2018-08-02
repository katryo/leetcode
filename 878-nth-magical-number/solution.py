from math import gcd


class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        gcd_ab = gcd(A, B)
        lcm = A * B // gcd_ab
        magic_count_in_interval = lcm // A + lcm // B - 1

        quotient = N // magic_count_in_interval
        remainder = N % magic_count_in_interval

        if remainder == 0:
            return (quotient * lcm) % MOD

        heads = [0, 0]
        for _ in range(remainder+1):
            if heads[0] > heads[1]:
                heads[1] += B
            else:
                heads[0] += A

        return (quotient * lcm + min(heads)) % MOD


s = Solution()
print(s.nthMagicalNumber(1, 2, 3))
print(s.nthMagicalNumber(4, 2, 3))
print(s.nthMagicalNumber(5, 2, 4))
print(s.nthMagicalNumber(3, 6, 4))
