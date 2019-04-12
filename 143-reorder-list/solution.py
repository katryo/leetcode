# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList2(self, head):

        #1. get the mid node
        slower = head
        faster = head.next
        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
        mid = slower

        #2. reverse the latter nodes
        pre = None
        cur = mid.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        mid.next = pre

        right = mid.next
        mid.next = None
        left = head

        # 1 2 4 3
        # l   r

        while right and left:
            tmp_left = left.next
            left.next = right
            tmp_right = right.next
            right.next = tmp_left
            left = tmp_left
            right = tmp_right
        return head


    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        def helper(head_node, nodes_count):
            if nodes_count == 1:
                tail_next = head_node.next
                head_node.next = None
                return head_node, tail_next
            if nodes_count == 2:
                tail_next = head_node.next.next
                head_node.next.next = None
                return head_node, tail_next
            inner_head, inner_tail_next = helper(head_node.next, nodes_count - 2)
            head_node.next = inner_tail_next
            tmp = inner_tail_next.next
            inner_tail_next.next = inner_head
            return head_node, tmp

        new_head, _ = helper(head, length)
        return new_head


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five

s = Solution()
s.reorderList2(one)

h = one
while h:
    print(h.val)
    h = h.next
