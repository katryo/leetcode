# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return None
        cur = root
        stack = []
        ans = []
        while stack or cur:
            while cur:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if cur.right and stack and stack[-1] == cur.right:
                stack.pop()
                stack.append(cur)
                cur = cur.right
            else:
                ans.append(cur.val)
                cur = None
        return ans

    # def postorderTraversal(self, root):
    #     if not root:
    #         return None
    #
    #     stack = [root]
    #     ans = []
    #     while stack:
    #         node = stack.pop()
    #         ans.append(node.val)
    #         if node.left:
    #             stack.append(node.left)
    #         if node.right:
    #             stack.append(node.right)
    #     return ans[::-1]

    # def postorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     BEGINNING = 0
    #     LEFT_SEEN = 1
    #     RIGHT_SEEN = 2
    #     ans = []
    #     stack = []
    #     cur = root
    #     state = BEGINNING
    #     while stack or cur:
    #         if cur:
    #             if cur.left and state == BEGINNING:
    #                 stack.append((cur, LEFT_SEEN))
    #                 cur = cur.left
    #                 state = BEGINNING
    #             elif cur.right and (state == LEFT_SEEN or state == BEGINNING):
    #                 stack.append((cur, RIGHT_SEEN))
    #                 cur = cur.right
    #                 state = BEGINNING
    #             else:
    #                 ans.append(cur.val)
    #                 cur = None
    #                 state = BEGINNING
    #         else:
    #             cur, state = stack.pop()
    #     return ans


s = Solution()
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
print(s.postorderTraversal(root))
