import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        def map_sum_freq(tree):
            left_map = collections.defaultdict(int)
            left_sum = 0
            right_sum = 0
            if tree.left:
                left_map, left_sum = map_sum_freq(tree.left)
            right_map = []
            if tree.right:
                right_map, right_sum = map_sum_freq(tree.right)

            for k in right_map:
                left_map[k] += right_map[k]
            total = left_sum + right_sum + tree.val
            left_map[total] += 1
            return left_map, total

        map, total = map_sum_freq(root)
        ans = []
        max_freq = -1
        for k in map:
            if map[k] == max_freq:
                ans.append(k)
            if map[k] > max_freq:
                max_freq = map[k]
                ans = [k]
        return ans


# left = TreeNode(2)
# tree = TreeNode(5)
# right = TreeNode(-3)
# tree.left = left
# tree.right = right
#
# s = Solution()
# print(s.findFrequentTreeSum(tree))
#
# right_2 = TreeNode(-5)
# tree.right = right_2
#
# print(s.findFrequentTreeSum(tree))
