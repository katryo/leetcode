from collections import defaultdict


class InvertedTree:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        def make_inverted_tree(node):
            tree = InvertedTree(node.val)
            if node.right:
                right_child = make_inverted_tree(node.right)
                right_child.left = tree
            if node.left:
                left_child = make_inverted_tree(node.left)
                left_child.right = tree
            return tree

        # returns nodes to the leaves
        def paths(node):
            if not node.left and not node.right:
                return [[node]]
            if not node.right:
                return [path + [node] for path in paths(node.left)]
            if not node.left:
                return [path + [node] for path in paths(node.right)]
            return [path + [node] for path in paths(node.left)] + [path + [node] for path in paths(node.right)]

        pathlist = paths(root)

        def dup_list(path_list):
            d = defaultdict(list)
            ans_d = {}
            for path in path_list:
                if path:
                    d[path[0].val].append(path[1:])
                    ans_d[path[0].val] = path[0]
            ans = []
            for val in d:
                if len(d[val]) > 1:
                    ans.append(ans_d[val])
                    ans += dup_list(d[val])
            return ans

        return dup_list(pathlist)


class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


root = TreeNode(2)
left = TreeNode(1)
right = TreeNode(1)
root.left = left
root.right = right
s = Solution()
print(s.findDuplicateSubtrees(root))


