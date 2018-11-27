from collections import defaultdict

class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        row_col = defaultdict(set)
        col_row = defaultdict(set)
        for stone in stones:
            row, col = stone[0], stone[1]
            row_col[row].add(col)
            col_row[col].add(row)

        seen = set()

        def dfs(row, col):
            if (row, col) in seen:
                return
            seen.add((row, col))
            for c in row_col[row]:
                if (row, c) in seen:
                    continue
                dfs(row, c)

            for r in col_row[col]:
                if (r, col) in seen:
                    continue
                dfs(r, col)

        islands = 0
        for stone in stones:
            row, col = stone[0], stone[1]
            if (row, col) in seen:
                continue
            dfs(row, col)
            islands += 1

        return len(stones) - islands


# s = Solution()
# print(s.removeStones([[0,0]]))