class Solution:
    def makesquare(self, nums):
        nums.sort(reverse=True)
        if not nums:
            return False
        quarter = sum(nums) // 4
        if quarter * 4 != sum(nums):
            return False

        for num in nums:
            if num > quarter:
                return False

        def dfs(idx, edges):
            if idx == len(nums):
                return edges[0] == edges[1] == edges[2] == edges[3]
            for i in range(4):
                if edges[i] + nums[idx] > quarter:
                    continue
                j = i - 1
                while j >= 0:
                    if edges[i] == edges[j]:
                        break
                    j -= 1
                if j != -1:
                    continue
                edges[i] += nums[idx]
                if dfs(idx+1, edges):
                    return True
                edges[i] -= nums[idx]
            return False

        edges = [0, 0, 0, 0]
        return dfs(0, edges)


s = Solution()
print(s.makesquare([2, 2, 2, 2, 2, 2]))
print(s.makesquare([3,3,2,2,2,2,2,2,2,2,2,2,2,2,2]))

print(s.makesquare([1, 1, 2, 2, 2]))
print(s.makesquare([3, 3, 3, 3, 4]))
print(s.makesquare([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10]))

