class Solution:
    ans = 0

    def tilingRectangle(self, n: int, m: int) -> int:
        self.ans = n * m

        def dfs(heights, count):
            if count >= self.ans:
                return
            if all(heights[i] == n for i in range(m)):
                self.ans = min(self.ans, count)
                return

            lowest = (n, -1)
            for i in range(m):
                if heights[i] < lowest[0]:
                    lowest = (heights[i], i)

            lowest_h = lowest[0]
            lowest_i = lowest[1]

            max_width = min(m - lowest_i, n - heights[lowest_i])
            for width in range(max_width, 0, -1):
                if lowest_i + width < m and heights[lowest_i+width-1] > lowest_h:
                    continue
                new_heights = heights[:]
                for i in range(lowest_i, lowest_i+width):
                    new_heights[i] += width
                dfs(new_heights, count+1)

        dfs([0] * m, 0)
        return self.ans


# s = Solution()
# print(s.tilingRectangle(2, 3))
# print(s.tilingRectangle(5, 8))
# print(s.tilingRectangle(11, 13))
