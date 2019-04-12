# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        sorted_first = self.sortList(head)
        sorted_second = self.sortList(second)

        if not sorted_second:
            return sorted_first

        dummy_head = ListNode(0)
        cur = dummy_head

        while sorted_first and sorted_second:
            if sorted_first.val < sorted_second.val:
                cur.next = sorted_first
                sorted_first = sorted_first.next
            else:
                cur.next = sorted_second
                sorted_second = sorted_second.next
            cur = cur.next
        if sorted_first:
            cur.next = sorted_first
        if sorted_second:
            cur.next = sorted_second
        return dummy_head.next







# s = Solution()
# one = ListNode(4)
# two = ListNode(2)
# one.next = two
# ret = s.sortList(one)
#
# cur = ret
# while cur:
#     print(cur.val)
#     cur = cur.next

