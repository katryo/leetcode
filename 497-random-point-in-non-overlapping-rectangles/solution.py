# from random import randrange
from random import randint
from bisect import bisect

class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.ranges = [0]
        points_so_far = 0
        for i, (x1, y1, x2, y2) in enumerate(rects):
            points_so_far += (x2 - x1 + 1) * (y2 - x2 + 1)
            self.ranges.append(points_so_far)

    def pick(self):
        n = randint(0, self.ranges[-1]-1)
        i = bisect(self.ranges, n)
        x1, y1, x2, y2 = self.rects[i-1]
        n -= self.ranges[i-1]
        return [x1 + n % (x2 - x1 + 1), y1 + n // (x2 - x1 + 1)]

    # def __init__(self, rects):
    #     """
    #     :type rects: List[List[int]]
    #     """
    #     points = 0
    #     rect_points = [0] * len(rects)
    #     for i in range(len(rects)):
    #         x1, y1, x2, y2 = rects[i]
    #         rect_point = (x2 - x1 + 1) * (y2 - y1 + 1)
    #         rect_points[i] = rect_point
    #         points += rect_point
    #     self.points = points
    #     self.rects = rects
    #     self.rect_points = rect_points
    #
    # def pick(self):
    #     """
    #     :rtype: List[int]
    #     """
    #     rand = randrange(self.points)
    #     zero_idx = -1
    #     for i in range(len(self.rects)):
    #         rand -= self.rect_points[i]
    #         if rand < 0:
    #             zero_idx = i
    #             break
    #     x1, y1, x2, y2 = self.rects[zero_idx]
    #     counter = -rand
    #     width = x2 - x1 + 1
    #     h = y2
    #     while counter > width:
    #         counter -= width
    #         h -= 1
    #     return [x2 - counter + 1, h]


s = Solution([[0,0, 3, 10], [20, 30, 40, 50]])
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
