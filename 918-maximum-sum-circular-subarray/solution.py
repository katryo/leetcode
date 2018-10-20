# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/C++JavaPython-One-Pass


from collections import deque


class Solution:
    def maxSubarraySumCircular2(self, A):
        total = 0
        cur_max = float('-inf')
        max_sum = 0
        min_sum = float('inf')
        cur_min = 0
        for a in A:
            cur_max = max(cur_max+a, a)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min+a, a)
            min_sum = min(min_sum, cur_min)
            total += a
        if max_sum > 0:
            return max(max_sum, total-min_sum)
        else:
            return max_sum


    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A2 = A + A

        table = [0] * len(A2)

        if len(A) == 1:
            return A[0]

        ans = float('-inf')
        total = 0
        for i in range(len(A2)):
            total += A2[i]
            table[i] = total
            if i < len(A):
                ans = max(ans, total)

        queue = deque([(0, table[0])])

        for i in range(1, len(table)):
            ans = max(ans, table[i] - queue[0][1])
            if i >= len(A):
                while queue and queue[0][0] <= i - len(A):
                    queue.popleft()
            while queue and table[i] <= queue[-1][1]:
                queue.pop()
            queue.append((i, table[i]))
        return ans


s = Solution()
print(s.maxSubarraySumCircular([2]))
print(s.maxSubarraySumCircular([1,-2,3,-2]))
print(s.maxSubarraySumCircular([5,-3,5]))
print(s.maxSubarraySumCircular([3,-1,2,-1]))
print(s.maxSubarraySumCircular([3,-2,2,-3]))
print(s.maxSubarraySumCircular([-2,4,-5,4,-5,9,4]))
