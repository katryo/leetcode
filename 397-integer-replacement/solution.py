class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n != 1:
            if n % 2 == 0:
                n >>= 1
            elif n == 3 or ((n >> 1) & 1 == 0):
                n -= 1
            else:
                n += 1
            ans += 1

        return ans

s = Solution()
print(s.integerReplacement(3)) # 11
print(s.integerReplacement(1000)) #
print(s.integerReplacement(8))
print(s.integerReplacement(16))
print(s.integerReplacement(17))
print(s.integerReplacement(7))
print(s.integerReplacement(65535)) # 111111111111111 => +1 /2 x 16
