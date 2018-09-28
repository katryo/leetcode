from random import randrange


class Solution:

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.count = n_rows * n_cols
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.dic = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        n = randrange(self.count)
        actual = self.dic.get(n, n)
        if self.count-1 in self.dic:
            self.dic[n] = self.dic[self.count-1]
        else:
            self.dic[n] = self.count-1

        self.count -= 1

        return divmod(actual, self.n_cols)

    def reset(self):
        """
        :rtype: void
        """

        self.count = self.n_rows * self.n_cols
        self.dic = {}


s = Solution(2, 2)
print(s.flip())
print(s.flip())
print(s.flip())
print(s.flip())
