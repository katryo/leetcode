# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head:
        #     return None
        # ans = head.next
        # if not ans:
        #     return head
        # next_head = ans.next
        # ans.next = head
        # head.next = self.swapPairs(next_head)
        # return ans

        start = ListNode(0)
        prev = start
        prev.next = head
        ans = head.next
        if not ans:
            return head

        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next
            prev.next, b.next, a.next = b, a, b.next
            prev = a
        return ans













