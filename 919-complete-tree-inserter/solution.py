# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class CBTInserter:
    def __init__(self, root):
        self.head = root
        self.arr = []

        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            self.arr.append(cur)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    def insert(self, v):
        new_idx = len(self.arr)
        if new_idx % 2:
            parent_idx = (new_idx - 1) // 2
        else:
            parent_idx = (new_idx - 2) // 2
        parent = self.arr[parent_idx]

        new_node = TreeNode(v)
        if new_idx % 2:
            parent.left = new_node
        else:
            parent.right = new_node
        self.arr.append(new_node)
        return parent.val

    def get_root(self):
        return self.head

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()