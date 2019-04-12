# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        digits_list = self.helper(root)
        ans = 0
        for digits in digits_list:
            total = 0
            d = 0
            for i in range(len(digits) - 1, -1, -1):
                total += digits[i] << d
                d += 1
            ans += total
        return ans

    def helper(self, root: TreeNode):
        res = []
        if root.right:
            r_d_list = self.helper(root.right)
        if root.left:
            l_d_list = self.helper(root.left)

        for r_d in r_d_list:
            res.append([root.val] + r_d)
        for l_d in l_d_list:
            res.append([root.val] + l_d)
        return res
