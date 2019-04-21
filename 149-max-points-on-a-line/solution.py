from typing import List
from collections import Counter
import math


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points: List[Point]) -> int:
        if len(points) < 2:
            return len(points)
        n = len(points)
        ans = 0
        for i in range(n):
            formulas = Counter()
            x_equal = Counter()
            y_equal = Counter()
            pa = points[i]
            same = 0
            for j in range(n):
                if j == i:
                    continue
                pb = points[j]
                dx = pb.x - pa.x
                dy = pb.y - pa.y

                if dx == dy == 0:
                    same += 1
                    continue

                if dx == 0:
                    x_equal[pa.x] += 1
                    continue
                if dy == 0:
                    y_equal[pa.y] += 1
                    continue

                common = math.gcd(dx, dy)
                formulas[dy // common, dx // common] += 1
            cand = same
            if formulas:
                cand = max(cand, formulas.most_common()[0][1] + same)
            if x_equal:
                cand = max(cand, x_equal.most_common()[0][1] + same)
            if y_equal:
                cand = max(cand, y_equal.most_common()[0][1] + same)
            ans = max(ans, cand)
        return ans + 1


if __name__ == '__main__':
    s = Solution()
    ps = [Point(0, 0), Point(2, 2), Point(1, 1), Point(2, 2)]
    print(s.maxPoints(ps))
    # ps = [Point(1, 1), Point(2, 2), Point(1, 1), Point(2, 2)]
#     ps = [Point(1, 1), Point(0, 0), Point(1, -1)]
#     ps = [Point(3, 1), Point(12, 3), Point(3, 1), Point(-6, -1)]
    # [[3,1],[12,3],[3,1],[-6,-1]]
    # ps = [Point(1, 1), Point(0, 0), Point(1, -1)]
    # ps = [Point(1, 4), Point(-29, 4)]
    # print(s.maxPoints(ps))
    # print(s.maxPoints(ps))
    # ps = [Point(1, 4), Point(3, 2), Point(2, 3), Point(4, 1), Point(5, 0)]
    # ps = [Point(1, 1), Point(3, 2), Point(5, 3), Point(4, 1), Point(2, 3), Point(1, 4)]
    # print(s.maxPoints(ps))
    # ps = [Point(1, 1), Point(2, 2), Point(3, 3)]
