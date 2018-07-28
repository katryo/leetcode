# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        parents = dict()

        stack = [root]

        target_node = None

        while stack:
            node = stack.pop()
            if node.val == target:
                target_node = node
                break
            if node.left:
                parents[node.left.val] = node
                stack.append(node.left)
            if node.right:
                parents[node.right.val] = node
                stack.append(node.right)

        visited = set()

        def bfs(dist, n):
            if n.val in visited:
                return []
            visited.add(n.val)
            if dist < 0:
                return []
            if dist == 0:
                return [n.val]
            if n.left and n.right:
                return bfs(dist - 1, n.left) + bfs(dist - 1, n.right)
            if n.left:
                return bfs(dist - 1, n.left)
            if n.right:
                return bfs(dist - 1, n.right)
            return []

        chosen = []
        visited.add(target)
        parent = None
        if target in parents:
            parent = parents[target]
        if parent:
            parent_dist = 1
            while parent:
                chosen += bfs(K - parent_dist, parent)
                parent_dist += 1
                v = parent.val
                if v in parents:
                    parent = parents[v]
                else:
                    break

        if target_node.left:
            chosen += bfs(K-1, target_node.left)

        if target_node.right:
            chosen += bfs(K-1, target_node.right)

        return chosen


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

one = root.right

one.right = TreeNode(8)
one.left = TreeNode(0)

five = root.left
five.left = TreeNode(6)
five.right = TreeNode(2)

two = five.right
two.left = TreeNode(7)
two.right = TreeNode(4)

s = Solution()
print(s.distanceK(root, 5, 2))
