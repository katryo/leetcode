class Solution(object):
    def primePalindrome(self, N):
        if N == 1:
            return 2

        def is_prime(n):
            return n > 1 and all(n % d > 0 for d in range(2, int(n ** 0.5)+1))

        for l in range(1, 6):
            for root in range(10 ** (l-1), 10 ** l):
                root_str = str(root)
                pal_str = root_str + root_str[-2::-1]
                pal = int(pal_str)
                if N <= pal and is_prime(pal):
                    return pal

            for root in range(10 ** (l-1), 10 ** l):
                root_str = str(root)
                pal_str = root_str + root_str[-1::-1]
                pal = int(pal_str)
                if N <= pal and is_prime(pal):
                    return pal

# s = Solution()
# print(s.primePalindrome(1))
# print(s.primePalindrome(2))
# print(s.primePalindrome(3))
# print(s.primePalindrome(31))
# print(s.primePalindrome(1000))
# print(s.primePalindrome(10602))
