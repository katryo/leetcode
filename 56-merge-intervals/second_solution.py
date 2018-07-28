import heapq

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        ans = [intervals[0]]
        for interval in intervals[1:]:
            last = ans[-1]
            if last.end >= interval.start:
                ans[-1] = Interval(last.start, interval.end)
            else:
                ans.append(interval)
        ret = []
        for interval in ans:
            ret.append([interval.start, interval.end])
        return ret

s = Solution()
print(s.merge([Interval(1, 3), Interval(2, 6),Interval(8, 10), Interval(15, 18)]))
print(s.merge([Interval(1, 4), Interval(4, 5)]))
print(s.merge([Interval(1, 4), Interval(0, 0)]))
