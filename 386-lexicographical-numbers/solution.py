class Solution:
    def lexicalOrder(self, n):
        ans = []

        def dfs(parent, result):
            if parent > n:
                return
            else:
                result.append(parent)
            for i in range(parent * 10, parent * 10 + 10):
                dfs(i, result)

        for i in range(1, 10):
            dfs(i, ans)
        return ans


    # def lexicalOrder(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[int]
    #     """
    #
    #     cur = 1
    #     ans = []
    #     for _ in range(n):
    #         ans.append(cur)
    #         if cur * 10 <= n:
    #             cur *= 10
    #         elif cur % 10 != 9 and cur+1 <= n:
    #             cur += 1
    #         else:
    #             while (cur // 10) % 10 == 9:
    #                 cur //= 10
    #             cur //= 10
    #             cur += 1
    #     return ans


s = Solution()
print(s.lexicalOrder(10))
print(s.lexicalOrder(34))


