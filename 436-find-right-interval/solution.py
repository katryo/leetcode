# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """

        start_idx = sorted([(interval.start, i) for i, interval in enumerate(intervals)])
        end_idx = sorted([(interval.end, i) for i, interval in enumerate(intervals)])

        start_p = 0
        ans = [-1] * len(intervals)
        for i in range(len(end_idx)):
            end_i = end_idx[i]
            while start_p < len(start_idx) and start_idx[start_p][0] < end_i[0]:
                start_p += 1
            if start_p < len(start_idx):
                assert start_idx[start_p][0] >= end_i[0]
                ans[end_idx[i][1]] = start_idx[start_p][1]
        return ans


s = Solution()
i0 = Interval(3,4)
i1 = Interval(2,3)
i2 = Interval(1,2)
print(s.findRightInterval([i0, i1, i2]))