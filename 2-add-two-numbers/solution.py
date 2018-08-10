# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        def calc_cur_carry(list, another_list, carry_num):
            if l1 and l2:
                result = l1.val + l2.val
            elif l1:
                result = l1.val
            else:
                result = l2.val
            result += carry_num
            carry_num = result // 10
            result %= 10
            return result, carry_num

        output = None
        ans = None
        carry = 0
        while l1 or l2:
            cur, carry = calc_cur_carry(l1, l2, carry)
            if not output:
                output = ListNode(cur)
                ans = output
            else:
                new_node = ListNode(cur)
                output.next = new_node
                output = output.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            new_node = ListNode(carry)
            output.next = new_node
        return ans



