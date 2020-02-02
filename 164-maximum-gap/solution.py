from typing import List
import math


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        n = len(nums)
        ma = max(nums)
        mi = min(nums)
        gap = math.ceil((ma - mi) / (n-1))
        mins = [float('inf')] * (n-1)
        maxs = [float('-inf')] * (n-1)

        for num in nums:
            if num == mi or num == ma:
                continue
            idx = (num - mi) // gap
            mins[idx] = min(num, mins[idx])
            maxs[idx] = max(num, maxs[idx])

        maxgap = float('-inf')
        prev = mi
        for i in range(n-1):
            if mins[i] == float('inf') or maxs[i] == float('-inf'):
                continue
            maxgap = max(maxgap, mins[i] - prev)
            prev = maxs[i]
        return max(maxgap, ma - prev)






# s = Solution()
# print(s.maximumGap([12115,10639,2351,29639,31300,11245,16323,24899,8043,4076,17583,15872,19443,12887,5286,6836,31052,25648,17584,24599,13787,24727,12414,5098,26096,23020,25338,28472,4345,25144,27939,10716,3830,13001,7960,8003,10797,5917,22386,12403,2335,32514,23767,1868,29882,31738,30157,7950,20176,11748,13003,13852,19656,25305,7830,3328,19092,28245,18635,5806,18915,31639,24247,32269,29079,24394,18031,9395,8569,11364,28701,32496,28203,4175,20889,28943,6495,14919,16441,4568,23111,20995,7401,30298,2636,16791,1662,27367,2563,22169,1607,15711,29277,32386,27365,31922,26142,8792]))
# print(s.maximumGap([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]))
# print(s.maximumGap([3,6,9,1]))
# print(s.maximumGap([10]))
