from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))

        seen_levels = set()
        ans = []

        while queue:
            node, level = queue.popleft()
            # (node, level) = queue.popleft()
            if level in seen_levels:
                ans[level] = max(ans[level], node.val)
            else:
                ans.append(node.val)
                seen_levels.add(level)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return ans


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.left = n3
    root.right = n2

    n5 = TreeNode(5)
    n3.left = n5

    n9 = TreeNode(9)
    n2.right = n9
    print(s.largestValues(root))
