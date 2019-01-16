class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        cur = [0, 1, 3, 2]
        for i in range(n-2):
            cur = cur + [num + 2 ** (i+2) for num in cur[::-1]]
        return cur


# s = Solution()
# print(s.grayCode(2))
# print(s.grayCode(3))
# print(s.grayCode(4))
