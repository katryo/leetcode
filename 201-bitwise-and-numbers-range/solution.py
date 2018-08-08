class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m_bin = bin(m)[2:]
        diff = n - m
        ans = 0

        for i in range(len(m_bin)):
            if m_bin[-1 -i] == '1':
                cur = int(m_bin[-1-i:], 2)
                moves_to_change = (1 << (i+1)) - cur

                if moves_to_change > diff:
                    ans |= (1 << i)
        return ans

    def rangeBitwiseAnd2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        digit = 1
        while m != n:
            digit <<= 1
            m >>= 1
            n >>= 1
        return digit * m


s = Solution()
print(s.rangeBitwiseAnd2(5, 7))
print(s.rangeBitwiseAnd2(0, 1))
print(s.rangeBitwiseAnd2(998, 1000))


