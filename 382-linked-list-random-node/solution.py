# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import random


class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cur = self.head
        count = 1
        ret = cur.val
        while cur.next:
            cur = cur.next
            count += 1
            if random.randint(0, count-1) == 0:
                ret = cur.val
        return ret

# Your Solution object will be instantiated and called as such:
h = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
h.next = n2
n2.next = n3
obj = Solution(h)
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
