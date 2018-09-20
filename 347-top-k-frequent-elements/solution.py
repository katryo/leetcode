from collections import Counter
import heapq


class Solution(object):
    def topKFrequent2(self, nums, k):
        counter = Counter()

        max_counter = 0
        for num in nums:
            counter[num] += 1
            max_counter = max(max_counter, counter[num])

        bucket = [[]] * (max_counter + 1)
        for c in counter:
            bucket[counter[c]].append(c)

        ans = []
        for c in range(max_counter, -1, -1):
            ans += bucket[c]
            if len(ans) >= k:
                break
        while len(ans) > k:
            ans = ans[:-1]
        return ans


    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter()

        for num in nums:
            counter[num] += 1

        count_num = [(-counter[c], c) for c in counter]
        heapq.heapify(count_num)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(count_num)[1])
        return ans


s = Solution()
print(s.topKFrequent([4, 1,23,5,6, 4, 3, 2, 2, 23, 4, 5, 5], 5))
print(s.topKFrequent2([4, 1,23,5,6, 4, 3, 2, 2, 23, 4, 5, 5], 5))
