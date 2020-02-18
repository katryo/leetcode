# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        heap = []

        n = len(lists)
        for i in range(n):
            li = lists[i]
            if li:
                heappush(heap, (li.val, i))

        dummy = ListNode(0)
        cur = dummy
        while heap:
            val, idx = heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next

            lists[idx] = lists[idx].next
            new_node = lists[idx]
            if new_node:
                heappush(heap, (new_node.val, idx))
        if dummy:
            return dummy.next
        else:
            return None