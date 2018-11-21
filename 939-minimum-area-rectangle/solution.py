# https://leetcode.com/articles/minimum-area-rectangle/

from collections import defaultdict


class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)

        last_x_for_vertical_line_segment = {}
        ans = float('inf')
        for x in sorted(columns):
            ys = sorted(columns[x])
            for i, y in enumerate(ys):
                for j in range(i):
                    y2 = ys[j]
                    if (y2, y) in last_x_for_vertical_line_segment:
                        area = (y-y2) * (x-last_x_for_vertical_line_segment[(y2, y)])
                        ans = min(ans, area)
                    last_x_for_vertical_line_segment[(y2, y)] = x
        if ans == float('inf'):
            return 0
        return ans

    # def minAreaRect(self, points):
    #     # point_set = {(x, y) for x, y in points}
    #     point_set = set(map(tuple, points))
    #     ans = float('inf')
    #     for i, pointlist in enumerate(points):
    #         point = tuple(pointlist)
    #         for j in range(i):
    #             point2 = tuple(points[j])
    #             point3 = (point[0], point2[1])
    #             point4 = (point2[0], point[1])
    #             if point3 in point_set and point4 in point_set:
    #                 area = abs(point[0]-point2[0]) * abs(point[1]-point2[1])
    #                 if area:
    #                     ans = min(ans, area)
    #
    #     if ans == float('inf'):
    #         return 0
    #     return ans


s = Solution()
# print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
# print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))
print(s.minAreaRect([[36219,4673],[26311,36047],[26311,4673],[36219,16024],[17010,16024],[26311,6287],[22367,6287],[17010,36047],[17010,6287],[22367,16024],[36219,6287],[22367,4673],[17010,4673],[36219,36047]]))
