from heapq import heappush, heappop
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        
        heap = []
        for key, count in counter.items():
            heappush(heap, (-count, key))
        
        ans = []
        for _ in range(k):
            popped = heappop(heap)
            ans.append(popped[1])
        return ans
