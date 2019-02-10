class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        year = 366
        table = [-1] * year
        table[0] = 0
        day_set = set(days)

        for i in range(1, year):
            if i in day_set:
                if i < 7:
                    table[i] = min(table[i-1]+costs[0], costs[1], costs[2])
                elif i < 30:
                    table[i] = min(table[i-1]+costs[0], table[i-7]+costs[1], costs[2])
                else:
                    table[i] = min(table[i-1]+costs[0], table[i-7]+costs[1], table[i-30]+costs[2])
            else:
                table[i] = table[i-1]
        return table[year-1]


s = Solution()
print(s.mincostTickets([1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29], [3,14,50]))
print(s.mincostTickets([1,4,6,7,8,20], [2,7,15]))
print(s.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))
