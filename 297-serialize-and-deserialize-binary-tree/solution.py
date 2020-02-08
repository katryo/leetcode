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
        if not root:
            return '(N)'

        left_s = '(N)'
        if root.left:
            left_s = self.serialize(root.left)

        right_s = '(N)'
        if root.right:
            right_s = self.serialize(root.right)
        ret = '(' + str(root.val) + left_s + right_s + ')'
        return ret

        # (1(2(N)(N))(3(4(N)(N))(5(N)(N))))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '(N)':
            return None
        cur = 1
        root_val_arr = []
        while data[cur] != '(':
            root_val_arr.append(data[cur])
            cur += 1
        root_val = int(''.join(root_val_arr))

        def get_node():
            nonlocal cur
            left_p_begin = cur
            p_count = 1
            while p_count > 0:
                cur += 1
                if data[cur] == '(':
                    p_count += 1
                elif data[cur] == ')':
                    p_count -= 1
            left_p_end = cur
            node = self.deserialize(data[left_p_begin:left_p_end + 1])
            return node

        left_node = get_node()
        cur += 1
        right_node = get_node()
        root = TreeNode(root_val)
        root.left = left_node
        root.right = right_node
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))