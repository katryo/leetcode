# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

from itertools import permutations

# Definition for a binary tree node.

from copy import deepcopy

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return None

        def insert_to_tree(node, new_node):
            if node.val < new_node.val:
                if not node.right:
                    node.right = new_node
                else:
                    insert_to_tree(node.right, new_node)
            else:
                if not node.left:
                    node.left = new_node
                else:
                    insert_to_tree(node.left, new_node)

        nums = {num for num in range(1, n+1)}

        def build_tree(availables, current_root):
            if not availables:
                return [deepcopy(current_root)]
            trees = []
            for num in nums:
                new_node = TreeNode(num)
                insert_to_tree(current_root, new_node)
                trees += build_tree(availables.difference({num}), current_root)
                del new_node
            return trees

        ans = []
        for num in nums:
            ans += build_tree(nums.difference({num}), TreeNode(num))

        return ans


s = Solution()
print(s.generateTrees(3))







