from collections import deque
from copy import deepcopy

class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        new_board = deepcopy(board)
        if board[click[0]][click[1]] == 'M':
            new_board[click[0]][click[1]] = 'X'
            return new_board

        seen = set()

        stack = deque()
        stack.append(click)

        while stack:
            r, c = stack.pop()
            if (r, c) in seen:
                continue

            adjacent_points = []
            mines = 0
            for move in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)):
                adjacent = (r+move[0], c+move[1])
                if adjacent[0] < 0 or adjacent[0] >= len(board):
                    continue
                if adjacent[1] < 0 or adjacent[1] >= len(board[0]):
                    continue
                if board[adjacent[0]][adjacent[1]] == 'M':
                    mines += 1
                adjacent_points.append(adjacent)
            if mines == 0:
                new_board[r][c] = 'B'
                for adjacent in adjacent_points:
                    if adjacent not in seen:
                        stack.append(adjacent)
            else:
                new_board[r][c] = str(mines)
            seen.add((r, c))

        return new_board


if __name__ == '__main__':

    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    s = Solution()
    # print(s.updateBoard(board, [3, 0]))

    b2 = [['B', '1', 'E', '1', 'B'],
          ['B', '1', 'M', '1', 'B'],
          ['B', '1', '1', '1', 'B'],
          ['B', 'B', 'B', 'B', 'B']]
    print(s.updateBoard(b2, [1, 2]))
