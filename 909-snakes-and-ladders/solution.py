from collections import deque


class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not board or not board[0]:
            return -1
        memo = [[-1] * len(board[0]) for _ in range(len(board))]
        memo[len(board) - 1][len(board[0]) - 1] = 0

        def num_to_ij(num):
            n = num - 1
            remainder = n % len(board)
            dividend = n // len(board)

            # print(remainder, dividend)
            i = len(board) - 1 - dividend
            if dividend % 2:
                j = len(board[0]) - remainder - 1
            else:
                j = remainder
            return i, j

        queue = deque()
        queue.insert(0, (1, 0))
        visited = set()
        while queue:
            num, moves = queue.pop()
            if num == len(board) * len(board[0]):
                return moves
            if num in visited:
                continue
            visited.add(num)
            for i in range(1, 7):
                new_num = num+i
                if new_num > len(board) * len(board[0]):
                    continue
                r, c = num_to_ij(new_num)
                if board[r][c] != -1:
                    new_num = board[r][c]
                queue.insert(0, (new_num, moves + 1))
        return -1
#
# s = Solution()
# print(s.snakesAndLadders([
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]))
# print(s.snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))
# print(s.snakesAndLadders([[-1,-1],[-1,3]]))
# print(s.snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))
# print(s.snakesAndLadders([[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]))
# print(s.snakesAndLadders(
#     [
#         [-1,-1,30,14,15,-1],
#         [23,9,-1,-1,-1,9],
#         [12,5,7,24,-1,30],
#         [10,-1,-1,-1,25,17],
#         [32,-1,28,-1,-1,32],
#         [-1,-1,23,-1,13,19]
#     ]
# ))
