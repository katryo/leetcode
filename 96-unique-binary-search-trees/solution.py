class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        table = [[-1] * (n+2) for _ in range(n+2)]

        def count_trees(start, end):
            if start > end:
                return 1
            if start == end:
                return 1
            if table[start][end] != -1:
                return table[start][end]
            ret = 0
            for root in range(start, end + 1):
                left_count = count_trees(start, root-1)
                right_count = count_trees(root + 1, end)
                ret += left_count * right_count
            table[start][end] = ret
            return ret

        return count_trees(1, n)


# s = Solution()
# print(s.numTrees(3))
# print(s.numTrees(10))
