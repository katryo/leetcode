import heapq

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = []
        ans = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if not cell:
                    heapq.heappush(heap, (0, (i, j)))
                    ans[i][j] = 0

        while heap:
            smallest = heapq.heappop(heap)  # (dist, (row, col))
            moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
            loc = smallest[1]
            for move in moves:
                nei_r, nei_c = loc[0]+move[0], loc[1]+move[1]
                if nei_r < 0 or nei_r >= len(matrix) or nei_c < 0 or nei_c >= len(matrix[0]):
                    continue
                if ans[nei_r][nei_c] == -1:
                    dist = smallest[0]+1
                    ans[nei_r][nei_c] = dist
                    heapq.heappush(heap, (dist, (nei_r, nei_c)))

        return ans


# if __name__ == '__main__':
#     s = Solution()
#     mtrx = [
#         [0, 0, 0],
#         [0, 1, 0],
#         [1, 1, 1],
#     ]
#     result = s.updateMatrix(mtrx)
#     for r in result:
#         print(r)

