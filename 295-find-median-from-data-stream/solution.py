from heapq import heappush, heappushpop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.greater_heap = []  # put numbers gt median
        self.smaller_heap = []  # put negative number lt median,

    # append self.greater_heap first
    def addNum(self, num: int) -> None:
        assert len(self.smaller_heap) <= len(self.greater_heap)

        if len(self.greater_heap) == len(self.smaller_heap):
            heappush(self.greater_heap, -heappushpop(self.smaller_heap, -num))
        else:
            heappush(self.smaller_heap, -heappushpop(self.greater_heap, num))

    def findMedian(self) -> float:
        assert self.greater_heap
        if len(self.smaller_heap) < len(self.greater_heap):
            return self.greater_heap[0]
        smaller = - self.smaller_heap[0]
        greater = self.greater_heap[0]
        return (smaller + greater) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()