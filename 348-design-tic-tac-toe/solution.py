class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.grid = [[0] * n for _ in range(n)]
        self.row_ones = [0] * n
        self.row_twos = [0] * n
        
        self.col_ones = [0] * n
        self.col_twos = [0] * n
        
        self.top_left_bottom_right_ones = 0
        self.top_left_bottom_right_twos = 0
        
        self.top_right_bottom_left_ones = 0
        self.top_right_bottom_left_twos = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = self.n
        
        self.grid[row][col] = player
        if player == 1:
            self.row_ones[row] += 1
            self.col_ones[col] += 1
            if row == col:
                self.top_left_bottom_right_ones += 1
            if col + row == self.n - 1:
                self.top_right_bottom_left_ones += 1
        else:
            self.row_twos[row] += 1
            self.col_twos[col] += 1
            if row == col:
                self.top_left_bottom_right_twos += 1
            if col + row == n - 1:
                self.top_right_bottom_left_twos += 1
        
        def is_end():
            for i in range(n):
                if self.row_ones[i] == n:
                    return True
                if self.col_ones[i] == n:
                    return True
                if self.row_twos[i] == n:
                    return True
                if self.col_twos[i] == n:
                    return True
            if self.top_left_bottom_right_ones == n:
                return True
            if self.top_left_bottom_right_twos == n:
                return True
            if self.top_right_bottom_left_ones == n:
                return True
            if self.top_right_bottom_left_twos == n:
                return True
            return False
        
        
        if is_end():
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
