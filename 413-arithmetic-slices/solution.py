class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        count = 0
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                count += 1
            else:
                ans += (count+1) * count // 2
                count = 0
        ans += (count+1) * count // 2
        return ans
#
s = Solution()
print(s.numberOfArithmeticSlices([1, 2, 3]))
print(s.numberOfArithmeticSlices([1, 2, 3, 4]))
print(s.numberOfArithmeticSlices([1,2,3,8,9,10]))
