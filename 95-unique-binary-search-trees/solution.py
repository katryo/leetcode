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
        if n == 0:
            return []

        # Return array of trees with [start, end]
        def build_trees(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]

            results = []
            for root_num in range(start, end+1):
                root = TreeNode(root_num)
                left_trees = build_trees(start, root_num-1)
                right_trees = build_trees(root_num+1, end)

                for left in left_trees:
                    for right in right_trees:
                        result = deepcopy(root)
                        result.left = left
                        result.right = right
                        results.append(result)
            return results
        return build_trees(1, n)


# s = Solution()
# print(s.generateTrees(3))
# print(s.generateTrees(6))
# print(s.generateTrees(8))







