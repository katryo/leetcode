from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        nodes = [None] * k
        probe = dummy
        cur = dummy
        while probe:
            reach_end = False
            for i in range(k):
                probe = probe.next
                if not probe:
                    reach_end = True
                    break
                nodes[i] = probe
            if reach_end: break
            nodes[0].next = probe.next
            for i in range(1, k):
                nodes[i].next = nodes[i-1]
            cur.next = nodes[k-1]
            cur = nodes[0]
            probe = nodes[0]
        return dummy.next


# s = Solution()
# list = ListNode(1)
# list.next = ListNode(2)
# list.next.next = ListNode(3)
# list.next.next.next = ListNode(4)
# list.next.next.next.next = ListNode(5)
# list.next.next.next.next.next = ListNode(6)
#
# result = s.reverseKGroup(list, 4)
# while result:
#     print(result.val)
#     result = result.next
