# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def countNodes(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root:
    #         return 0
    #
    #     def count_node(node):
    #         assert node
    #         if node.left and node.right:
    #             return count_node(node.left) + count_node(node.right) + 1
    #         if node.left:
    #             return count_node(node.left) + 1
    #         if node.right:
    #             return count_node(node.right) + 1
    #         return 1
    #
    #     return count_node(root)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def calc_height(node):
            if node.left:
                return calc_height(node.left)+1
            return 0

        def count_nodes_in_full_tree(height):
            return 2 ** (height + 1) - 1

        if not root.right and not root.left:
            return 1
        if not root.right:
            return 2

        left_height = calc_height(root.left)
        right_height = calc_height(root.right)
        if left_height == right_height:
            # root.left is a full tree
            return 1 + count_nodes_in_full_tree(left_height) + self.countNodes(root.right)
        else:
            # root.right is a full tree
            return 1 + self.countNodes(root.left) + count_nodes_in_full_tree(right_height)



