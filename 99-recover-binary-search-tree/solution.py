# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        nums = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            nums.append(node)
            if node.right:
                traverse(node.right)

        traverse(root)

        prev = TreeNode(float('-inf'))
        first = None
        second = None
        for i in range(len(nums)):
            cur = nums[i]
            if not first and cur.val <= prev.val:
                first = prev
            if first and cur.val <= prev.val:
                second = cur
            prev = cur

        first.val, second.val = second.val, first.val


root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
s = Solution()
s.recoverTree(root)
