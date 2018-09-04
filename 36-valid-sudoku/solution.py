class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def is_3x3_valid(r, c):
            nums = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    num = board[i][j]
                    if num == '.':
                        continue
                    if num in nums:
                        return False
                    nums.add(num)
            return True

        def is_1x9_valid(r):
            nums = set()
            for j in range(9):
                num = board[r][j]
                if num == '.':
                    continue
                if num in nums:
                    return False
                nums.add(num)
            return True

        def is_9x1_valid(c):
            nums = set()
            for i in range(9):
                num = board[i][c]
                if num == '.':
                    continue
                if num in nums:
                    return False
                nums.add(num)
            return True

        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                if not is_3x3_valid(row, col):
                    return False

        for row in range(9):
            if not is_1x9_valid(row):
                return False
        for col in range(9):
            if not is_9x1_valid(col):
                return False
        return True

s = Solution()
board = [
["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(board))
