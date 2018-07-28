class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        [0, 2, 3, 5, 5, 6, 8]

        [0, 0, 10, 100, 100]
        210   220   290

        [0, 0, 50, 100, 100]
        250   200   250

        [0, 0, 50, 90, 100]
        240   190  230  260

        """
        nums.sort()

        # O(n)
        def score(idx):
            ans = 0
            for num in nums:
                ans += abs(num-nums[idx])
            return ans

        left = 0
        right = len(nums)  # [left, right)
        while left < right:
            middle = (left+right) // 2  # left might be right
            # 1
            # 1

            if middle == left:
                assert left + 1 == right
                return score(middle)
            assert left < middle < right

            middle_v = score(middle)  # 0
            if middle + 1 == right:
                return min(middle_v, score(left))

            middle_r_v = score(middle+1) # 1

            if middle_v < middle_r_v:
                right = middle+1  # 2
            else:
                left = middle

        assert left == right
        return score(left)

# s = Solution()
# print(s.minMoves2([0,0,1]))
# print(s.minMoves2([1,0,0,8,6]))
# print(s.minMoves2([1,2,3]))
#
# print(s.minMoves2([1,2,3, 100000000]))
# print(s.minMoves2([1,2,3, 100000000, 100000000]))
# print(s.minMoves2([1,2,3, 100000000, 100000000, 100000000]))

