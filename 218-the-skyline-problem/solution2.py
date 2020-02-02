from typing import List
from heapq import heappush, heappop


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap = []

        LEFT = 0
        RIGHT = 1
        END = 10

        events = []

        for left, right, height in buildings:
            left_event = [-height, left, LEFT, None]
            right_event = [-height, right, RIGHT, left_event]
            heappush(events, (left, left_event))
            heappush(events, (right, right_event))

        ans = []
        while events:
            x, event = heappop(events)
            nega_height = event[0]
            right_or_left = event[2]
            if right_or_left == LEFT:
                if not heap or nega_height < heap[0][0]:
                    ans.append([x, - nega_height])
                heappush(heap, event)
            else:
                left_event = event[3]
                left_event[3] = END

                while heap and heap[0][3] == END:
                    # Removes the current largest which has finished
                    heappop(heap)
                if heap:
                    if heap[0][0] > nega_height:
                        if ans and ans[-1][0] == x:
                            popped = ans.pop()
                            if popped[1] > - heap[0][0]:
                                continue
                            else:
                                ans.append([x, -heap[0][0]])
                        else:
                            ans.append([x, - heap[0][0]])
                else:
                    ans.append([x, 0])

        real_ans = []
        # cur = 0
        for elem in ans:
            if real_ans and real_ans[-1][0] == elem[0] and real_ans[-1][1] <= elem[1]:
                real_ans.pop()
                real_ans.append(elem)
            else:
                real_ans.append(elem)
        return real_ans


# s = Solution()
# print(s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# print(s.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]))
# print(s.getSkyline([[6765, 184288, 53874], [13769, 607194, 451649], [43325, 568099, 982005], [
#       47356, 933141, 123943], [59810, 561434, 119381], [75382, 594625, 738524]]))
# print(s.getSkyline([[2, 9, 10], [9, 12, 15]]))
# print(s.getSkyline([[2, 9, 10], [3, 7, 15], [
#     5, 12, 12], [15, 20, 10], [19, 24, 8]]))
# print(s.getSkyline([[15, 20, 10], [19, 24, 8]]))
