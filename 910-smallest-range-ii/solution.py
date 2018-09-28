class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        if not A:
            return 0
        A.sort()
        mi = A[0]
        ma = A[-1]

        ans = ma - mi
        for i in range(len(A)-1):
            left = A[i]
            right = A[i+1]
            ans = min(ans, max(ma-K, left+K) - min(mi+K, right-K))
        return ans


s = Solution()
print(s.smallestRangeII([1,3,6], 3))



