from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0:
            if dy == 0:
                return False
            return x3 != x1

        assert x1 != x2
        angle = dy / dx
        y_in_line_12_at_x3 = y1 + (x3 - x1) * angle
        return y_in_line_12_at_x3 != y3


# s = Solution()
# print(s.isBoomerang([[0,0], [0, 1], [0, 2]]))
# print(s.isBoomerang([[0,0], [0, 0], [1, 2]]))
# print(s.isBoomerang([[0,0], [0, 0], [0, 0]]))
# print(s.isBoomerang([[1,1], [0, 0], [2, 2]]))
# print(s.isBoomerang([[1,1], [0, 0], [2, 3]]))
# print(s.isBoomerang([[1,1],[2,3],[3,2]]))
#
# print(s.isBoomerang([[0,0], [1, 0], [2, 0]]))
# print(s.isBoomerang([[0,0], [1, 0], [2, 1]]))
# print(s.isBoomerang([[0,0], [2, 1], [1, 0]]))


