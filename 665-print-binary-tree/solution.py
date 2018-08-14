# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        if not root:
            return [[""]]

        def height(node):
            if not node.left and node.right:
                return 0
            right_height = 0
            if node.right:
                right_height = height(node.right)

            left_height = 0
            if node.left:
                left_height = height(node.left)
            return max(right_height, left_height)

        root_height = height(root)
        counter = 0
        width = 1
        while counter < root_height:
            width = width * 2 + 1
            counter += 1

        output = [[""] * width for _ in (range(root_height + 1))]

        # Replace elements in the array recursively
        def put_tree(node, depth, start, end):
            # [start, end]
            assert (end - start + 1) % 2 == 1
            center = (start + end) // 2
            output[depth][center] = str(node.val)
            if node.left:
                put_tree(node.left, depth + 1, start, center - 2)
            if node.right:
                put_tree(node.right, depth + 1, center + 2, end)

        put_tree(root, 0, 0, width - 1)
        return output

