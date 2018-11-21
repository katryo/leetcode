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

        if len(lists) > 2:
            mid = len(lists) // 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
        else:
            left = lists[0]
            right = lists[1]

        dummy = ListNode(0)
        ans = dummy
        while left or right:
            if not left:
                ans.next = right
                break
            if not right:
                ans.next = left
                break
            assert left and right
            if left.val >= right.val:
                ans.next = ListNode(right.val)
                ans = ans.next
                right = right.next
            else:
                ans.next = ListNode(left.val)
                ans = ans.next
                left = left.next
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
