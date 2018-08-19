# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         if not root:
#             return None
#
#         if root == p and root == q:
#             return root
#
#         right_lca = self.lowestCommonAncestor(root.right, p, q)
#         left_lca = self.lowestCommonAncestor(root.left, p, q)
#
#         if right_lca and not left_lca:
#             if root == p or root == q:
#                 return root
#             else:
#                 return right_lca
#         if left_lca and not right_lca:
#             if root == p or root == q:
#                 return root
#             else:
#                 return left_lca
#         if right_lca and left_lca:
#             return root
#
#         if root == p or root == q:
#             return root
#         return None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        parents = {root: None}

        # Record parent for each node using dfs
        stack = [root]
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
            if node.left:
                parents[node.left] = node
                stack.append(node.left)

        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p = parents[p]

        while q not in p_ancestors:
            q = parents[q]
        return q


s = Solution()

tree = TreeNode(3)
left = TreeNode(5)
right = TreeNode(1)

left_right = TreeNode(4)

tree.left = left
tree.left.right = left_right
tree.right = right
print(s.lowestCommonAncestor(tree, left, left_right).val)
#

