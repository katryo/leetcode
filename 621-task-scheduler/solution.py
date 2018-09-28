# https://leetcode.com/problems/task-scheduler/solution/

from collections import defaultdict
import heapq


class Solution:
    def leastInterval2(self, tasks, n):
        map = [0] * 26
        for char in tasks:
            map[ord(char)-ord('A')] += 1
        map.sort()

        max_val = map[25]-1
        idle_slots = max_val * n
        for i in range(24, -1, -1):
            idle_slots -= min(map[i], max_val)
        return max(idle_slots + len(tasks), len(tasks))

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        table = defaultdict(int)
        for task in tasks:
            table[task] += 1
        heap = []
        for task in table:
            heapq.heappush(heap, (-table[task], task))

        ans = 0
        while heap:
            popped = []
            for i in range(n + 1):
                if not heap:
                    if not popped:
                        break
                    else:
                        ans += n + 1 - i
                    break
                number, task = heapq.heappop(heap)
                ans += 1
                if number == -1:
                    pass
                else:
                    popped.append((number + 1, task))
            for popped_item in popped:
                heapq.heappush(heap, popped_item)
        return ans


s = Solution()
print(s.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2))
print(s.leastInterval2(['A', 'A', 'A', 'B', 'B', 'B'], 2))
print(s.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 0))
print(s.leastInterval2(['A', 'A', 'A', 'B', 'B', 'B'], 0))
print(s.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 1))
print(s.leastInterval2(['A', 'A', 'A', 'B', 'B', 'B'], 1))
