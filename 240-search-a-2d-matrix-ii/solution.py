class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False

        n = len(matrix)
        m = len(matrix[0])

        def has_target(left, right, top, bottom):
            if left > right or top > bottom:
                return False

            if matrix[top][left] > target or matrix[bottom][right] < target:
                return False
            mid = (left + right) // 2

            row = top
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return has_target(left, mid - 1, row, bottom) or has_target(mid + 1, right, top, row - 1)

        return has_target(0, m - 1, 0, n - 1)

