# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        count = 0
        stack = []
        num_depth = []
        for i in range(len(S)):
            if S[i] == '-':
                if stack:
                    num = int(''.join(stack))
                    num_depth.append((num, count))
                    count = 0
                    stack = []
                count += 1
            else:
                stack.append(S[i])
        num = int(''.join(stack))
        num_depth.append((num, count))

        stack = []
        for num, depth in num_depth:
            cur = TreeNode(num)
            if not stack:
                stack.append((cur, 0))
                continue
            while stack[-1][1] >= depth:
                stack.pop()

            if stack[-1][0].left:
                stack[-1][0].right = cur
            else:
                stack[-1][0].left = cur
            stack.append((cur, depth))
        return stack[0][0]


# s = Solution()
# root = s.recoverFromPreorder("1-2--3--4-5--6--7")
# print(root.val)
# print(root.left.val)
# print(root.left.left.val)
# print(root.left.right.val)
# print(root.right.val)
# print(root.right.left.val)
# print(root.right.right.val)
