from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ma = defaultdict(int)
        self.mi = defaultdict(int)

    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max_min(root)

        def helper(node):
            assert node

            cand = max(abs(node.val - self.ma[node]), abs(node.val - self.mi[node]))
            if node.left:
                cand = max(cand, helper(node.left))
            if node.right:
                cand = max(cand, helper(node.right))
            return cand

        return helper(root)

    def max_min(self, root):
        assert root
        ma = root.val
        mi = root.val
        if root.left:
            mar, mir = self.max_min(root.left)
            ma = max(ma, mar)
            mi = min(mi, mir)
        if root.right:
            mar, mir = self.max_min(root.right)
            ma = max(ma, mar)
            mi = min(mi, mir)

        self.ma[root] = ma
        self.mi[root] = mi
        return ma, mi


s = Solution()
one = TreeNode(4)
two = TreeNode(2)
nega = TreeNode(-4)
nega.left = TreeNode(-10)
one.left = two
one.right = nega
print(s.maxAncestorDiff(one))
