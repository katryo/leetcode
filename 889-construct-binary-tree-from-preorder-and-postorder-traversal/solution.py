# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None

        root = TreeNode(pre[0])
        if pre == post:
            return root
        if len(pre) == 2:
            root.left = TreeNode(pre[1])
            return root

        if pre[1] == post[-2]:
            child = self.constructFromPrePost(pre[1:], post[:-1])
            root.left = child
            return root

        idx_post_left = post.index(pre[1])
        idx_pre_right = pre.index(post[-2])
        left_child = self.constructFromPrePost(pre[1:idx_pre_right], post[:idx_post_left + 1])
        right_child = self.constructFromPrePost(pre[idx_pre_right:], post[idx_post_left + 1:-1])
        root.left = left_child
        root.right = right_child
        return root


s = Solution()
# print(s.constructFromPrePost([2, 1], [1, 2]))
# print(s.constructFromPrePost([1, 2, 3], [2, 3, 1]))
# print(s.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1]))
print(s.constructFromPrePost([4,2,1,3], [3,1,2,4]))