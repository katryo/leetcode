from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets):
        dests = defaultdict(list)
        ans = []
        for src, dest in tickets:
            heapq.heappush(dests[src], dest)

        def dfs(dep):
            arrivals = dests[dep]
            while arrivals:
                dfs(heapq.heappop(arrivals))
            ans.insert(0, dep)

        dfs('JFK')
        return ans

    # def findItinerary(self, tickets):
    #     dests = defaultdict(list)
    #     for a, b in sorted(tickets)[::-1]:
    #         dests[a].append(b)
    #     ans = []
    #
    #     def visit(start):
    #         while dests[start]:
    #             visit(dests[start].pop())
    #         ans.append(start)
    #
    #     visit('JFK')
    #     return list(reversed(ans))

s = Solution()
print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
