import collections

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        count_table = collections.defaultdict(int)
        ans = (-1, -1)
        for row in wall:
            total = 0
            for brick in row[:-1]:
                total += brick
                count_table[total] += 1
                if count_table[total] > ans[0]:
                    ans = (count_table[total], total)
        if ans[0] == -1:
            return len(wall)
        return len(wall) - ans[0]


# w = [[1,2,2,1],
#  [3,1,2],
#  [1,3,2],
#  [2,4],
#  [3,1,2],
#  [1,3,1,1]]
w = [[1], [1], [1]]
s = Solution()
print(s.leastBricks(w))