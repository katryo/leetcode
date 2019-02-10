# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        if not root:
            return ''

        def val_to_str(v):
            return chr(ord('a') + root.val)

        # TODO: edge case
        if not root.left and not root.right:
            return val_to_str(root.val)

        if not root.left:
            return self.smallestFromLeaf(root.right) + val_to_str(root.val)
        if not root.right:
            return self.smallestFromLeaf(root.left) + val_to_str(root.val)

        left_str = self.smallestFromLeaf(root.left)
        right_str = self.smallestFromLeaf(root.right)

        if left_str < right_str:
            return left_str + val_to_str(root.val)
        else:
            return right_str + val_to_str(root.val)
