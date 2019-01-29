import bisect


class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        table = [-1] * len(days)
        table[0] = costs[0]

        for i in range(1, len(table)):
            date = days[i]
            idx_uncovered_by_7 = bisect.bisect(days, date-7)-1
            if idx_uncovered_by_7 == -1:
                candidate = costs[1]
            else:
                candidate = table[idx_uncovered_by_7] + costs[1]
            idx_uncovered_by_30 = bisect.bisect(days, date-30)-1
            if idx_uncovered_by_30 == -1:
                candidate = min(candidate, costs[2])
            else:
                candidate = min(candidate, table[idx_uncovered_by_30] + costs[2])
            table[i] = min(table[i-1] + costs[0], candidate)
        return table[-1]


# s = Solution()
# print(s.mincostTickets([1,4,6,7,8,20], [2,7,15]))
# print(s.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))
