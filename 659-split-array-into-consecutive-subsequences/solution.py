# https://leetcode.com/problems/split-array-into-consecutive-subsequences/solution/

import heapq
from collections import Counter
from collections import deque
from itertools import groupby


class Solution:
    def isPossible3(self, nums):
        prev, prev_count = None, 0
        starts = deque()
        for num, grp in groupby(nums):
            count = len(list(grp))

            # Number jump. New chain or die
            if prev is not None and (num-prev) != 1:
                for _ in range(prev_count):
                    if prev < starts.popleft() + 2:
                        return False
                prev, prev_count = None, 0
            else:  # Continuous or brand new chain begins
                # Several new chains begin
                if count > prev_count:
                    for _ in range(count-prev_count):
                        starts.append(num)
                # end chain(s)
                elif count < prev_count:
                    for _ in range(prev_count - count):
                        if num-1 < starts.popleft()+2:
                            return False
                prev, prev_count = num, count
        return all(nums[-1] >= x+2 for x in starts)


    def isPossible2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        tails = Counter()
        for x in nums:
            # x is already consumed in the past by new chaining. Lazy evaluation.
            if count[x] == 0:
                continue
            # extend the chain
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            # start a new chain
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1
        return True


    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        heap = []
        i = 0
        while i < len(nums):
            if not heap:
                heap.append((nums[i], 1))
                i += 1
                continue
            top_num, top_len = heap[0]

            if nums[i] == top_num:
                heapq.heappush(heap, (nums[i], 1))
                i += 1
                continue
            elif nums[i] == top_num + 1:
                heapq.heappop(heap)
                heapq.heappush(heap, (nums[i], top_len + 1))
                i += 1
                continue
            elif top_len > 2:  # hop
                heapq.heappop(heap)
            else:
                return False

        return all(tup[1] > 2 for tup in heap)


s = Solution()
print(s.isPossible([1, 2, 3, 3, 4, 5]))
print(s.isPossible([1, 2, 3, 4, 4, 5]))
print(s.isPossible2([1, 2, 3, 3, 4, 5]))
print(s.isPossible2([1, 2, 3, 4, 4, 5]))
print(s.isPossible3([1, 2, 3, 3, 4, 5]))
print(s.isPossible3([1, 2, 3, 4, 4, 5]))
