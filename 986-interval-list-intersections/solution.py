# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        i = 0
        j = 0
        ans = []

        def overlap(x, y):
            start = max(A[x].start, B[y].start)
            end = min(A[x].end, B[y].end)
            if start > end:
                return []
            else:
                return [start, end]
            # return []
            # return [10, 10]
            # return [29, 35]

        while i < len(A) and j < len(B):
            candidate = overlap(i, j)
            a = A[i]
            b = B[j]
            if candidate:
                ans.append(candidate)

            if a.end < b.end:
                i += 1
            else:
                j += 1
        return ans
