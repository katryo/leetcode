class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        table = set()
        for i in range(R):
            for j in range(C):
                loc = (i, j)
                table.add(loc)

        def is_in_grid(cur):
            r, c = cur
            return r >= 0 and r < R and c >= 0 and c < C

        def check_grid_move(cur, ret):
            if is_in_grid(cur):
                ret.append([cur[0], cur[1]])
                table.remove(cur)
            return ret

        # returns locations agent moves which is non-negative
        def simulate_stroke(stroke_num, start_row, start_col):
            ret = []
            cur = (start_row, start_col)
            # 1. right
            cur = (cur[0], cur[1] + 1)
            check_grid_move(cur, ret)

            # 2. down
            for i in range(2 * stroke_num + 1):
                cur = (cur[0] + 1, cur[1])
                check_grid_move(cur, ret)

            # 3. left
            for i in range(2 * (stroke_num + 1)):
                cur = (cur[0], cur[1] - 1)
                check_grid_move(cur, ret)

            # 4. up
            for i in range(2 * (stroke_num + 1)):
                cur = (cur[0] - 1, cur[1])
                check_grid_move(cur, ret)

            # 5. right and reach start_row-1, start_col+1
            for i in range(2 * (stroke_num + 1)):
                cur = (cur[0], cur[1] + 1)
                check_grid_move(cur, ret)
            return ret

        cur_r = r0
        cur_c = c0

        table.remove((cur_r, cur_c))
        stroke = 0
        ans = [[cur_r, cur_c]]
        while True:
            locations = simulate_stroke(stroke, cur_r, cur_c)
            ans += locations
            if not table:
                return ans
            stroke += 1
            cur_r -= 1
            cur_c += 1


# s = Solution()
# print(s.spiralMatrixIII(1, 4, 0, 0))
# print(s.spiralMatrixIII(5, 6, 1, 4))
