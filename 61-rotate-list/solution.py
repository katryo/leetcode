# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        if k == 0:
            return head
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1
        k = k % length
        if not k:
            return head

        forward = head
        rear = head
        for i in range(k):
            forward = forward.next
        while forward.next:
            forward = forward.next
            rear = rear.next

        first = rear.next
        rear.next = None
        last.next = head
        return first