# https://leetcode.com/problems/minimum-window-subsequence/

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n = len(S)
        m = len(T)

        last_i = -1
        first_i = 0
        cand = [-1, float('inf')]
        while last_i < n-1:
            ti = 0
            for i in range(first_i, n):
                last_i = i
                if S[i] == T[ti]:
                    ti += 1
                    if ti == m:
                        break
            if ti < m:
                break
            first_i = last_i
            ti = m-1
            for i in range(last_i, -1, -1):
                first_i = i
                if S[i] == T[ti]:
                    ti -= 1
                    if ti == -1:
                        break
            if cand[1] - cand[0] > last_i - first_i:
                cand = [first_i, last_i]
            first_i += 1
        if cand[1] == float('inf'):
            return ''
        return S[cand[0]:cand[1]+1]


# s = Solution()
# print(s.minWindow("cnhczmccqouqadqtmjjzl", "cm"))
