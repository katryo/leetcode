from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]

        def two_ex(x):
            if x == 1:
                return 0
            if x == 2:
                return 1
            return two_ex(x // 2) + 1

        exp = two_ex(label)
        nearest = 2 ** exp
        diff = label - nearest
        parent = nearest - 1 - diff // 2
        return self.pathInZigZagTree(parent) + [label]


# if __name__ == '__main__':
#     s = Solution()
#     print(s.pathInZigZagTree(14))
#     print(s.pathInZigZagTree(26))

