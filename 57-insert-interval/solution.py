# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        s = newInterval.start
        e = newInterval.end
        left = [interval for interval in intervals if interval.end < s]
        right = [interval for interval in intervals if interval.start > e]
        if left + right == intervals:
            return left + [newInterval] + right

        # Some overwrap exist
        merged_s = min(s, intervals[len(left)].start)
        merged_e = max(e, intervals[len(intervals)-1-len(right)].end)
        return left + [Interval(merged_s, merged_e)] + right


s = Solution()
interval_list = [[2,4],[5,7],[8,10],[11,13]]

intervals = [Interval(elem[0], elem[1]) for elem in interval_list]
new = Interval(3, 6)
# new = Interval(6, 8)
result = s.insert(intervals, new)
print([(i.start, i.end) for i in result])

