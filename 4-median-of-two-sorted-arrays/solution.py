class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        length = m + n
        if length % 2 == 0:
            left = self.kth(nums1, 0, nums2, 0, length//2)
            right = self.kth(nums1, 0, nums2, 0, length//2+1)
            return (left + right) / 2
        else:
            return self.kth(nums1, 0, nums2, 0, length//2+1)

    def kth(self, A, a_start, B, b_start, k):
        if a_start > len(A)-1:
            return B[b_start+k-1]
        if b_start > len(B)-1:
            return A[a_start+k-1]
        if k == 1:
            return min(A[a_start], B[b_start])

        a_val = float('inf')
        b_val = float('inf')
        a_mid = a_start+k//2-1
        b_mid = b_start+k//2-1
        if a_mid <= len(A)-1:
            a_val = A[a_mid]
        if b_mid <= len(B)-1:
            b_val = B[b_mid]
        if a_val <= b_val:
            return self.kth(A, a_mid+1, B, b_start, k-k//2)
        else:
            return self.kth(A, a_start, B, b_mid+1, k-k//2)


# s = Solution()
# print(s.findMedianSortedArrays([3, 5, 6, 100], [2, 3, 9, 10, 20, 30]))
# print(s.findMedianSortedArrays([1, 5, 36, 55], [10, 20, 30, 40, 50]))
#
#

