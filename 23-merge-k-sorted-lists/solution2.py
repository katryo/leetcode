from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        dummy = ListNode(0)
        ans = dummy
        heap = []
        for i, node in enumerate(lists):
            heappush(heap, (node.val, i))

        while heap:
            min_val, i = heappop(heap)
            ans.next = ListNode(min_val)
            ans = ans.next
            lists[i] = lists[i].next
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        return dummy.next


s = Solution()
list_a = ListNode(1)
list_a.next = ListNode(4)
list_a.next.next = ListNode(5)

list_b = ListNode(1)
list_b.next = ListNode(3)
list_b.next.next = ListNode(4)

list_c = ListNode(2)
list_c.next = ListNode(6)

result = s.mergeKLists([list_a, list_b, list_c])

while result:
    print(result.val)
    result = result.next
