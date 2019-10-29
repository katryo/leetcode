# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution

from typing import List
import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append((endTime[i], startTime[i], profit[i]))

        jobs.sort()

        dp_prof = [0]
        dp_end = [0]

        # through ith jobs
        for i in range(n):
            job = jobs[i]
            job_start = job[1]

            max_profit_can_take_i = bisect.bisect(dp_end, job_start) - 1
            max_total_profit_with_i = dp_prof[max_profit_can_take_i] + job[2]
            if max_total_profit_with_i > dp_prof[-1]:
                dp_prof.append(max_total_profit_with_i)
                dp_end.append(job[0])
        return dp_prof[-1]


# s = Solution()
# print(s.jobScheduling([1,1,1],  [2,3,4], [5,6,4]))
# print(s.jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))
# print(s.jobScheduling([1,2,3,3],  [3,4,5,6],  [50,10,40,70]))

