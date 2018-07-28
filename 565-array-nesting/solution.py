class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        moves_to_end = [-1] * len(nums)

        for i in range(len(nums)):
            if moves_to_end[i] != -1:
                continue
            visited = set()
            path = []
            cur = i
            while cur not in visited:
                visited.add(cur)
                path.append(cur)
                cur = nums[cur]

            # path: [a, b, c, ..., f] f is the nearest to the goal
            for j, loc in enumerate(reversed(path)):
                moves_to_end[loc] = j+1

        ans = -1
        for moves in moves_to_end:
            ans = max(ans, moves)
        return ans

# s = Solution()
# print(s.arrayNesting([5,4,0,3,1,6,2]))
# print(s.arrayNesting([0]))
# print(s.arrayNesting([1, 0]))
# print(s.arrayNesting([0, 1]))
