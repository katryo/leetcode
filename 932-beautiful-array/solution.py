class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        memo = {1:[1]}

        def func(n):
            if n in memo:
                return memo[n]
            odds = func((n+1) // 2)
            evens = func(n // 2)

            memo[n] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
            return memo[n]
        return func(N)



s = Solution()
print(s.beautifulArray(5))
# print(s.beautifulArray(2))
# print(s.beautifulArray(3))
# print(s.beautifulArray(4))
# print(s.beautifulArray(1000))
