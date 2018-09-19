# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):

        def rob_not_rob(node):
            if not node:
                return 0, 0
            left, left_not = rob_not_rob(node.left)
            right, right_not = rob_not_rob(node.right)

            rob = node.val + left_not + right_not
            not_rob = max(left, left_not) + max(right, right_not)

            return rob, not_rob

        options = rob_not_rob(root)
        return max(options)

    # def rob(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root:
    #         return 0
    #
    #     def generate_memo_tree(node, memo_node):
    #         if node.left:
    #             memo_node.left = generate_memo_tree(node.left, TreeNode(-1))
    #         if node.right:
    #             memo_node.right = generate_memo_tree(node.right, TreeNode(-1))
    #         return memo_node
    #
    #     memo_tree = generate_memo_tree(root, TreeNode(-1))
    #
    #     def max_money(node, m_tree):
    #         if not node:
    #             return 0
    #         if m_tree.val != -1:
    #             return m_tree.val
    #
    #         total = node.val
    #         if node.left:
    #             total += max_money(node.left.left, m_tree.left.left) + max_money(node.left.right, m_tree.left.right)
    #         if node.right:
    #             total += max_money(node.right.left, m_tree.right.left) + max_money(node.right.right, m_tree.right.right)
    #
    #         option = max_money(node.left, m_tree.left) + max_money(node.right, m_tree.right)
    #         m_tree.val = max(total, option)
    #         return m_tree.val
    #
    #     return max_money(root, memo_tree)

