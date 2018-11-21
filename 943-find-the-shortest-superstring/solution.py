class Solution:
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        N = len(A)

        overlaps = [[0] * N for _ in range(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break


        dp = [[0] * N for _ in range(N)]
        parent = [[None] * N for _ in range(1 << N)]
        print(parent)
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    pmask = mask ^ (1 << bit)
                    if pmask == 0:
                        continue
                    for i in range(N):
                        if (pmask >> i) & 1:
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        perm = []
        mask = (1<<N) - 1
        i = max(range(N), key=dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(N) if not seen[i]])

        ans = [A[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.apend(A[perm[i]][overlap:])
        return ''.join(ans)




s = Solution()
# print(s.shortestSuperstring(["abc", "def"]))
print(s.shortestSuperstring(["abc", "bcde"]))
print(s.shortestSuperstring(["abcdd", "wwabc"]))

