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
        events = []
        for interval in intervals:
            heapq.heappush(events, (interval.start, 1))  # start
            heapq.heappush(events, (interval.end, -1))  # end

        ans = []
        counter = 0
        start = -1
        while events:
            cur_event = heapq.heappop(events)
            time = cur_event[0]
            counter += cur_event[1]

            while events:
                event = heapq.heappop(events)
                if event[0] == time:
                    counter += event[1]
                else:
                    heapq.heappush(events, event)
                    break

            if counter > 0 and start == -1:
                start = time
            if counter == 0:
                if start == -1:
                    ans.append([time, time])
                else:
                    ans.append([start, time])
                start = -1
        return ans


s = Solution()
print(s.merge([Interval(1, 3), Interval(2, 6),Interval(8, 10), Interval(15, 18)]))
# print(s.merge([Interval(1, 4), Interval(4, 5)]))
# print(s.merge([Interval(1, 4), Interval(0, 0)]))
