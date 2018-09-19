# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        if not head:
            return None
        helper = ListNode(0)
        cur = head
        pre = helper
        while cur:
            next = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = helper
            cur = next
            
        return helper.next



    # def insertionSortList(self, head):
    #
    #     if not head:
    #         return None
    #     sorted_head = head
    #     cur = head.next
    #     sorted_head.next = None
    #     while cur:
    #         sorted_prev = None
    #         sorted_cur = sorted_head
    #         if sorted_cur.val >= cur.val:
    #             tmp = cur.next
    #             cur.next = sorted_cur
    #             sorted_head = cur
    #             cur = tmp
    #             continue
    #         while sorted_cur and cur.val > sorted_cur.val:
    #             sorted_prev = sorted_cur
    #             sorted_cur = sorted_cur.next
    #         if sorted_cur:
    #             if sorted_prev:
    #                 sorted_prev.next = cur
    #             cur_next = cur.next
    #             cur.next = sorted_cur
    #             cur = cur_next
    #         else:
    #             sorted_prev.next = cur
    #             cur = cur.next
    #             sorted_prev.next.next = None
    #     return sorted_head


s = Solution()
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

four.next = two
two.next = one
one.next = three

head = s.insertionSortList(four)

n = head
while n:
    print(n.val)
    n = n.next
