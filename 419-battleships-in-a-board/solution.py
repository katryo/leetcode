class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        if not board or not board[0]:
            return 0
        ans = 0

        j = 0
        while j < len(board[0]):
            if board[0][j] == 'X':
                ans += 1
                while j < len(board[0]) and board[0][j] == 'X':
                    j += 1
            else:
                j += 1
        if len(board) == 1:
            return ans

        for i in range(1, len(board)):
            j = 0
            while j < len(board[0]):
                if board[i][j] == 'X':
                    if board[i - 1][j] == '.':
                        ans += 1
                        j += 1
                        while j < len(board[0]) and board[i][j] == 'X':
                            j += 1
                    else:
                        j += 1
                else:
                    j += 1
        return ans

s = Solution()
print(s.countBattleships([['.', '.'], ['X', 'X']]))