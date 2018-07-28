# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def rec(node, level):
            if not node:
                return " "
            serialized = str(node.val) + "/" + str(level) + "/" + rec(node.left, level + 1) + "/" + str(
                level) + "/" + rec(node.right, level + 1)
            # 0 1 3 4 2 5 6
            return serialized

        return rec(root, 0)

        # 0
        # 1 2
        # 3 4 5 6

        # 0123456
        #

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rec(text, level):
            if text == " ":
                return None
            splitted = text.split("/" + str(level) + "/")
            if len(splitted) == 1:
                return TreeNode(text)
            top_txt, left_txt, right_txt = splitted
            left = rec(left_txt, level + 1)
            right = rec(right_txt, level + 1)
            top = TreeNode(top_txt)
            top.left = left
            top.right = right
            return top

        return rec(data, 0)

# Your Codec object will be instantiated and called as such:


root = TreeNode(10)
codec = Codec()
codec.deserialize(codec.serialize(root))
