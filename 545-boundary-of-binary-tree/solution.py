# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        def left_t(node):
            if node.left:
                left_arr = left_t(node.left)
                return [node.val] + left_arr
            elif node.right:
                arr = left_t(node.right)
                return [node.val] + arr
            return [node.val]
        
        def right_t(node):
            if node.right:
                arr = right_t(node.right)
                return arr + [node.val]
            elif node.left:
                arr = right_t(node.left)
                return arr + [node.val]
            return [node.val]
        
        def bottom(node):
            if not node.left and not node.right:
                return [node.val]
            left = []
            if node.left:
                left = bottom(node.left)
            right = []
            if node.right:
                right = bottom(node.right)
            return left + right
        
        if root.left:
            left = left_t(root)[:-1]
        else:
            left = [root.val]
            
        if root.right:
            right = right_t(root)[1:-1]
        else:
            right = []
            
        bottoms = bottom(root)
        return left + bottoms + right
        
        
