# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False

        def is_same(tree_a, tree_b):
            if not tree_a and not tree_b:
                return True
            if not tree_a or not tree_b:
                return False
            if tree_a.val == tree_b.val:
                return is_same(tree_a.left, tree_b.left) and is_same(tree_a.right, tree_b.right)
            return False

        if is_same(s, t):
            return True
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        return False