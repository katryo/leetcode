# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        for i in range(m-1):
            pre = pre.next
        head = pre.next.next
        cur = pre.next
        for i in range(n-m):
            head_next = head.next
            head.next = cur
            cur = head
            head = head_next
        pre.next.next = head
        pre.next = cur

        # def swap_returns_head(head_node, diff):
        #     if diff == 0:
        #         return head_node, head_node
        #     if diff == 1:
        #         next_tmp = head_node.next
        #         head_node.next = next_tmp.next
        #         next_tmp.next = head_node
        #         return next_tmp, head_node
        #     nodes_next, nodes_tail = swap_returns_head(head_node.next, diff - 2)
        #
        #     tail = nodes_tail.next
        #     head_node.next = tail.next
        #     tail.next = nodes_next
        #     nodes_tail.next = head_node
        #     return tail, head_node
        #
        # if m == 1:
        #     return swap_returns_head(head, n - m)[0]
        #
        # ans = head
        # for _ in range(m - 2):
        #     head = head.next
        # head.next = swap_returns_head(head.next, n - m)[0]
        # return ans
        #

