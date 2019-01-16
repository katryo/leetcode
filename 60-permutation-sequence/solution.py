from math import factorial


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        nums = list(range(1, n+1))
        remain = k-1
        perm = ''
        digits = n
        while digits > 0:
            digits -= 1
            idx, remain = divmod(remain, factorial(digits))
            perm += str(nums[idx])
            nums.remove(nums[idx])
        return perm

    # def getPermutation(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: str
    #     """
    #
    #     nums = list(range(1, n+1))
    #     k -= 1
    #     ans = []
    #
    #     for i in range(n-1, -1, -1):
    #         idx, k = divmod(k, factorial(n))
    #         ans.append(str(nums[idx]))
    #         del nums[idx]
    #     return ''.join(ans)


s = Solution()
print(s.getPermutation(3, 3))
# print(s.getPermutation(4, 10))
# print(s.getPermutation(4, 24))




