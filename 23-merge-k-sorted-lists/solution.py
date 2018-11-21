# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        dummy = ListNode(0)
        ans = dummy
        while True:
            minimum = float('inf')
            min_i = -1
            for i, node in enumerate(lists):
                if node and node.val < minimum:
                    minimum = node.val
                    min_i = i
            if min_i == -1:
                return dummy.next

            # we have min node
            lists[min_i] = lists[min_i].next
            ans.next = ListNode(minimum)
            ans = ans.next
