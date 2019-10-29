class Solution:
    def calc_k(self, n):
        assert n > 0
        k = 0
        while n:
            n //= 10
            k += 1
        return k

    def isArmstrong(self, N: int) -> bool:
        k = self.calc_k(N)
        total = 0
        n = N
        while n:
            rem = n % 10
            total += rem ** k
            n //= 10
        return total == N


# s = Solution()
# print(s.isArmstrong(1))
# print(s.isArmstrong(2))
# print(s.isArmstrong(10))
# print(s.isArmstrong(153))
# print(s.isArmstrong(123))
