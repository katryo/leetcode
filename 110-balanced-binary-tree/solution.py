from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        stack, node = [], root
        last, depths = None, defaultdict(int)
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths[node.left], depths[node.right]
                    if abs(left - right) > 1:
                        return False
                    depths[node] = max(left, right)+1
                    last = node
                    node = None
                else:
                    node = node.right
        return True
    #     length, ans = self.length_balanced(root)
    #     return ans
    #
    # def length_balanced(self, node):
    #     if not node:
    #         return 0, True
    #     left_len, left_b = self.length_balanced(node.left)
    #     right_len, right_b = self.length_balanced(node.right)
    #     if not left_b or not left_b:
    #         return -1, False
    #     if abs(left_len - right_len) > 1:
    #         return -1, False
    #     return max(left_len, right_len) + 1, True


s = Solution()
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
print(s.isBalanced(root))
