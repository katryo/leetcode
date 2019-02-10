# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        table = defaultdict(list)
        leftmost = 0
        rightmost = 0

        def traverse(node, loc, y):
            nonlocal leftmost
            nonlocal rightmost
            if not node:
                return
            leftmost = min(leftmost, loc)
            rightmost = max(rightmost, loc)
            table[loc].append((node.val, y))
            traverse(node.left, loc - 1, y + 1)
            traverse(node.right, loc + 1, y + 1)

        traverse(root, 0, 0)
        ans = []
        for i in range(leftmost, rightmost + 1):
            array = table[i]
            ans.append([x[0] for x in sorted(array, key=lambda z: z[1] * 1000 + z[0])])
        return ans

    