class Solution:
    def minDeletionSize(self, A):
        cuts = [False] * len(A)
        ans = 0

        for col in zip(*A):
            if all(cuts[i] or col[i] <= col[i+1] for i in range(len(col)-1)):
                for i in range(len(col)-1):
                    if col[i] < col[i+1]:
                        cuts[i] = True
            else:
                ans += 1
        return ans

    # def minDeletionSize(self, A):
    #     """
    #     :type A: List[str]
    #     :rtype: int
    #     """
    #
    #     def is_sorted(B):
    #         return all(B[i] <= B[i+1] for i in range(len(B)-1))
    #
    #     ans = 0
    #
    #     cur = [''] * len(A)
    #
    #     for col in zip(*A):
    #         cur2 = cur[:]
    #         for i, letter in enumerate(col):
    #             cur2[i] = cur2[i]+letter
    #
    #         if is_sorted(cur2):
    #             cur = cur2
    #         else:
    #             ans += 1
    #
    #     return ans


s = Solution()
print(s.minDeletionSize(["xga","xfb","yfa"]))
print(s.minDeletionSize(["jwkwdc","etukoz"]))
print(s.minDeletionSize(["koccmoezl","hbccayhbd"]))
print(s.minDeletionSize(["ca","bb","ac"]))
print(s.minDeletionSize(["zyx","wvu","tsr"]))
print(s.minDeletionSize(["xc","yb","za"]))
