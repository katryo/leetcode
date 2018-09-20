import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []
        if not nums1 or not nums2:
            return []
        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0))

        ans = []
        visited = set()
        while heap and len(ans) < k:
            total, one, two = heapq.heappop(heap)
            if (one, two) in visited:
                continue
            visited.add((one, two))
            ans.append([nums1[one], nums2[two]])

            if one < len(nums1)-1:
                heapq.heappush(heap, (nums1[one+1] + nums2[two], one+1, two))
            if two < len(nums2)-1:
                heapq.heappush(heap, (nums1[one] + nums2[two+1], one, two+1))
        return ans






