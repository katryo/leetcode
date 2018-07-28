class Solution:
    def makesquare(self, nums):
        if not nums:
            return False
        nums = sorted(nums, reverse=True)
        total = sum(nums)
        quarter = total // 4
        if quarter * 4 != total:
            return False
        edges = [0, 0, 0, 0]

        def dfs(idx, edges):
            if idx == len(nums):
                return edges[0] == edges[1] == edges[2] == edges[3] == quarter
            for i in range(4):
                j = i - 1
                while j > -1:
                    if edges[i] == edges[j]:
                        break
                    j -= 1
                if j != -1:
                    continue
                if edges[i] + nums[idx] > quarter:
                    continue
                else:
                    assert edges[i] - nums[idx] <= quarter
                    edges[i] += nums[idx]
                    if dfs(idx+1, edges):
                        return True
                    edges[i] -= nums[idx]
            return False

        return dfs(0, edges)

s = Solution()
print(s.makesquare([1, 1, 1, 1]))
# print(s.makesquare([8,16,24,32,40,48,56,64,72,80,88,96,104,112,60]))
# print(s.makesquare([2, 2, 2, 2, 2, 2]))
# print(s.makesquare([3,3,2,2,2,2,2,2,2,2,2,2,2,2,2]))
#
# print(s.makesquare([1, 1, 2, 2, 2]))
# print(s.makesquare([3, 3, 3, 3, 4]))
# print(s.makesquare([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10]))

