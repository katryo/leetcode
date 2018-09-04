# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        def helper(front):
            if front.next:
                while front.next.next and front.val == front.next.val == front.next.next.val:
                    front = front.next
                next_list = helper(front.next)
                if not next_list:
                    front.next = None
                    return front
                if next_list.val == front.val:
                    return next_list.next
                else:
                    front.next = next_list
                    return front
            else:
                return front

        ans = helper(head)
        return ans