import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo = matrix[0][0]
        hi = matrix[len(matrix)-1][len(matrix[0])] + 1
        while lo < hi:
            mid = (lo + hi) // 2
            count = 0
            j = len(matrix[0]) - 1
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j+1
            if count < k:
                lo = mid+1
            else:
                hi = mid
        return lo
