class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        if not matrix[0]:
            return []

        PACIFIC = 1
        ATLANTIC = 2

        pacifics = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        atlantics = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        def dfs(r, c, ocean):
            if ocean == ATLANTIC:
                if atlantics[r][c] != -1:
                    return
                atlantics[r][c] = 1
            else:
                if pacifics[r][c] != -1:
                    return
                pacifics[r][c] = 1

            for move in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                n_r = r+move[0]
                n_c = c+move[1]
                if n_r == -1 or n_c == -1 or n_r == len(matrix) or n_c == len(matrix[0]):
                    continue
                if matrix[r][c] <= matrix[n_r][n_c]:
                    dfs(n_r, n_c, ocean)

        for r in range(len(matrix)):
            dfs(r, 0, PACIFIC)
            dfs(r, len(matrix[0])-1, ATLANTIC)
        for c in range(len(matrix[0])):
            dfs(0, c, PACIFIC)
            dfs(len(matrix)-1, c, ATLANTIC)

        ans = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if pacifics[r][c] == 1 and atlantics[r][c] == 1:
                    ans.append([r, c])
        return ans

s = Solution()
# m = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# m = [[10,10,10],[10,1,10],[10,10,10]]
# m = [[1,1],[1,1],[1,1]]
m = [[3,3,3],[3,1,3],[0,2,4]]
print(s.pacificAtlantic(m))