class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def candidates(bd, row, col):
            possible = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

            for i in range(9):
                possible.discard(bd[row][i])
                possible.discard(bd[i][col])
            big_row_start = (row // 3) * 3
            big_col_start = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    possible.discard(bd[big_row_start+i][big_col_start+j])
            return possible

        has_point = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    has_point = True
        if not has_point:
            return True

        possible_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        smallest_possibility_r = -1
        smallest_possibility_c = -1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    new_possible_nums = candidates(board, i, j)
                    if not new_possible_nums:
                        return False

                    if len(new_possible_nums) < len(possible_nums):
                        possible_nums = new_possible_nums
                        smallest_possibility_r = i
                        smallest_possibility_c = j

        assert smallest_possibility_r != -1
        assert smallest_possibility_c != -1

        for num in possible_nums:
            board[smallest_possibility_r][smallest_possibility_c] = num
            ans = self.solveSudoku(board)
            filled = True
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        filled = False
            if filled:
            board[smallest_possibility_r][smallest_possibility_c] = '.'


if __name__ == '__main__':
    s = Solution()
    # board = [["5","3",".",".","7",".",".",".","."],
    #          ["6",".",".","1","9","5",".",".","."],
    #          [".","9","8",".",".",".",".","6","."],
    #          ["8",".",".",".","6",".",".",".","3"],
    #          ["4",".",".","8",".","3",".",".","1"],
    #          ["7",".",".",".","2",".",".",".","6"],
    #          [".","6",".",".",".",".","2","8","."],
    #          [".",".",".","4","1","9",".",".","5"],
    #          [".",".",".",".","8",".",".","7","9"]
    #          ]

    board = [[".",".",".","2",".",".",".","6","3"],
             ["3",".",".",".",".","5","4",".","1"],
             [".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],
             [".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]

    # s.solveSudoku(board)
    # print(board)

# [["8","9","7","2","5","4","1","6","3"],
#  ["3","6","8","9","7","5","4","2","1"],
#  ["2","5","1","6","4","3","9","8","7"],
#  ["7","8","2","4","1","6","3","9","5"],
#  ["6","1","9","5","3","8","7","4","2"],
#  ["9","3","4","1","2","7","8","5","6"],
#  ["1","2","6","3","8","9","5","7","4"],
#  ["5","4","3","7","9","2","6","1","8"],
#  ["4","7","5","8","6","1","2","3","9"]]