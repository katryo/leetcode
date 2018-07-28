class Solution:
    def makesquare(self, nums):
        def dfs(index, edge, count, used):
            if count == 0:
                return True
            for i in range(index, len(nums)):
                len_after_apply = edge - nums[i]
                if i in used or len_after_apply < 0:
                    continue
                if len_after_apply > 0:
                    if dfs(i + 1, len_after_apply, count, used | {i}):
                        return True
                if len_after_apply == 0:
                    if count:
                        if dfs(1, l, count - 1, used | {i}):
                            return True
                    else:
                        return True
                    # return True
            return False

        sm = sum(nums)
        if len(nums) < 4 or sm % 4 != 0:
            return False
        l = sm // 4
        nums.sort(reverse=True)
        if nums[0] > l:
            return False
        if nums[0] == l:
            return dfs(1, l, 3, {0})
        return dfs(1, l, 4, {0})

s = Solution()
print(s.makesquare([2, 2, 2, 2, 2, 2]))
print(s.makesquare([3,3,2,2,2,2,2,2,2,2,2,2,2,2,2]))

print(s.makesquare([1, 1, 2, 2, 2]))
# print(s.makesquare([3, 3, 3, 3, 4]))
# print(s.makesquare([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10]))

