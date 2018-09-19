class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        i = 0
        while i < len(citations):
            if i+1 <= citations[i]:
                if i == len(citations)-1:
                    return i+1
                if citations[i+1] <= i+1:
                    return i+1
            i += 1
        return 0


s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))
print(s.hIndex([3, 0, 6, 1]))
print(s.hIndex([1, 1]))
print(s.hIndex([1, 1, 2, 2, 5, 5, 2]))
print(s.hIndex([1, 0, 2, 2, 0, 5, 2]))
