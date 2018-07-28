import collections

# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = collections.deque()
        queue.append((root, 0))

        deepest_leftmost = (root.val, 0)
        while queue:
            node, depth = queue.popleft()
            if depth > deepest_leftmost[1]:  # >, not >=. Thus, leftmost node is assigned to deepest_leftmost
                deepest_leftmost = (node.val, depth)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return deepest_leftmost[0]
#
# tree = TreeNode(2)
# left = TreeNode(1)
# right = TreeNode(3)
# tree.left = left
# tree.right = right
# s = Solution()
# print(s.findBottomLeftValue(tree))  # 1
#
#
# tree = TreeNode(1)
# l2 = TreeNode(2)
# t4 = TreeNode(4)
# l2.left = t4
# tree.left = l2
#
# r3 = TreeNode(3)
# tree.right = r3
#
# l5 = TreeNode(5)
# r3.left = l5
# l7 = TreeNode(7)
# l5.left = l7
#
# r6 = TreeNode(6)
# r3.right = r6
#
# print(s.findBottomLeftValue(tree))  # 7
