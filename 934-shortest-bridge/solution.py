from collections import deque


class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        def get_first_island():
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] == 1:
                        return i, j
            return -1, -1

        r, c = get_first_island()

        def fill_two(i, j):
            if i < 0 or i > len(A) - 1 or j < 0 or j > len(A[0]) - 1:
                return
            if A[i][j] == 1:
                A[i][j] = 2
                fill_two(i + 1, j)
                fill_two(i - 1, j)
                fill_two(i, j + 1)
                fill_two(i, j - 1)

        fill_two(r, c)

        seen = [[False] * len(A[0]) for _ in range(len(A))]

        def get_edges(i, j):
            ans = []
            if i < 0 or i > len(A) - 1 or j < 0 or j > len(A[0]) - 1:
                return []
            if seen[i][j]:
                return []
            seen[i][j] = True
            if A[i][j] == 2:
                ans += get_edges(i + 1, j)
                ans += get_edges(i - 1, j)
                ans += get_edges(i, j + 1)
                ans += get_edges(i, j - 1)
            if A[i][j] == 0:
                ans.append((i, j))
            return ans

        edges = get_edges(r, c)

        queue = deque()
        for edge in edges:
            queue.append((0, edge))

        while queue:
            layer, cur = queue.popleft()
            row, col = cur[0], cur[1]
            if row < 0 or row > len(A) - 1 or col < 0 or col > len(A[0]) - 1:
                continue

            if A[row][col] == 1:
                return layer
            if A[row][col] == 2:
                continue
            A[row][col] = 2

            queue.append((layer + 1, (row + 1, col)))
            queue.append((layer + 1, (row - 1, col)))
            queue.append((layer + 1, (row, col + 1)))
            queue.append((layer + 1, (row, col - 1)))
        return -1


# s = Solution()
# # print(s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
# # print(s.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
# print(s.shortestBridge([[1,0,0,0,0,1]]))
# print(s.shortestBridge([[1,0,0,0,0,1],[1,0,0,0,0,1]]))
# print(s.shortestBridge([[1,0,0,0,0,0],[0,0,0,0,0,1]]))
