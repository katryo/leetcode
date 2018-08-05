class Solution(object):
    MOD = 1337

    def pow_mod(self, a, arr):
        super_pow = self.superPow(a, arr)
        powered = super_pow ** 10
        return powered % self.MOD

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        # Assume len(b) == 2
        # superPow(a, b) = (a ^ b) % MOD = (a ^ (b[0] * 10 + b[1])) % MOD
        # = (a ^ (b[0] * 10) * a ^ b[1]) % MOD
        # = (a ^ (b[0] * 10) % MOD) * (a ^ b[1] % MOD)) % MOD

        # a ^ (b[0] * 10) % MOD
        # a ^ b[0] ^ 10 % MOD
        # ((a ^ b[0]) % MOD) ^ 10 % MOD

        if len(b) == 0:
            return 1
        if len(b) == 1:
            result = (a ** b[0])
            return result % self.MOD

        b_without_last = b[:-1]
        return self.pow_mod(a, b_without_last) * self.superPow(a, [b[-1]]) % self.MOD


# s = Solution()
# a = 2
# b = [1, 0]
# print(s.superPow(a, b))
#
# a = 2
# b = [3]
# print(s.superPow(a, b))
#
# a = 3
# b = [39]
# print(s.superPow(a, b))
