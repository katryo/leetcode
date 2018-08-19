class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort(reverse=True)

        def set_d(ns):
            if not ns:
                return {()}
            right = set_d(ns[1:])
            ret = set()
            for r in right:
                ret.add(r + tuple([ns[0]]))
            ret = ret.union(right)
            return ret

        set_ret = set_d(nums)
        ans = [list(t) for t in set_ret]
        return ans


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
