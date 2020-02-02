from typing import List
from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        locations = defaultdict(list)
        for i in range(n):
            for j in range(m):
                letter = board[i][j]
                locations[letter].append((i, j))

        tree = {}
        for word in words:
            cur = tree
            for letter in word:
                if letter not in cur:
                    cur[letter] = {}
                cur = cur[letter]
            cur['terminal'] = {'word': word}

        seen = set()
        ans_set = set()

        def dfs(row, col, cur):
            if 'terminal' in cur:
                ans_set.add(cur['terminal']['word'])
                del cur['terminal']
            if row < 0 or row >= n or col < 0 or col >= m:
                return
            if (row, col) in seen:
                return False

            letter = board[row][col]
            if letter not in cur:
                return
            seen.add((row, col))
            child_tree = cur[letter]
            dfs(row+1, col, child_tree)
            dfs(row-1, col, child_tree)
            dfs(row, col+1, child_tree)
            dfs(row, col-1, child_tree)
            seen.remove((row, col))

        for i in range(n):
            for j in range(m):
                dfs(i, j, tree)
        return list(ans_set)



# s = Solution()
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# print(s.findWords(board, words))
#
# s = Solution()
# board = [["a","b","c"],
#          ["a","e","d"],
#          ["a","f","g"]]
# words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
# print(s.findWords(board, words))