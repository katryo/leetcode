class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        nums = [num for num in range(1, n+1)]
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
        factorials.reverse()

        k -= 1
        ans = []

        for i in range(n):
            factorial = factorials[i]
            num_idx = k // factorial
            k -= num_idx * factorial
            ans.append(str(nums[num_idx]))
            del nums[num_idx]
        return ''.join(ans)


# s = Solution()
# print(s.getPermutation(4, 10))
# print(s.getPermutation(4, 24))




