class Solution:
    def hIndex(self, citations):
        lo = 0
        hi = len(citations)
        length = len(citations)
        while lo < hi:
            mid = (lo + hi) // 2
            if citations[mid] == length - mid:
                return citations[mid]
            if citations[mid] > length - mid:
                hi = mid
            else:
                lo = mid+1
        return length - lo
    
    # def hIndex(self, citations):
    #     """
    #     :type citations: List[int]
    #     :rtype: int
    #     """
    #     lo = 0
    #     hi = len(citations)-1
    #     length = len(citations)
    #     while lo <= hi:
    #         mid = (lo + hi) // 2
    #         if citations[mid] == length - mid:
    #             return citations[mid]
    #         if citations[mid] > length - mid:
    #             hi = mid-1
    #         else:
    #             lo = mid+1
    #
    #     return length - lo


s = Solution()
print(s.hIndex([0, 0, 1, 20, 22]))
print(s.hIndex([0,1,3,5,6]))
print(s.hIndex([0, 0, 1]))
print(s.hIndex([1, 1]))
print(s.hIndex([1, 1, 2, 2, 5, 5]))
print(s.hIndex([1, 3, 5, 10]))
