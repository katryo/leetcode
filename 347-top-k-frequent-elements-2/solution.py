from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        counter = Counter(nums)
        #items = counter.most_common(k)
        #return [item[0] for item in items]
        
        heap = []
        for key, count in counter.items():
            heappush(heap, (-count, key))
        
        ans = []
        for _ in range(k):
            popped = heappop(heap)
            ans.append(popped[1])
        return ans
