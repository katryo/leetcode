from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for query in queries:
            ans.append(self.is_match(query, pattern))
        return ans

    def is_match(self, query: str, pattern: str) -> bool:
        n = len(query)
        m = len(pattern)
        table = [[0] * (m + 1) for _ in range(n + 1)]

        table[0][0] = 1
        # for i in range(n):
        #     if query[i].islower() or query[i] == pattern[0]:
        #         table[i][0] = 1
        #     else:
        #         break

        capital_contains = [True] * n
        for i in range(n):
            if query[i].isupper():
                break
            else:
                capital_contains[i] = False

        def helper(i, j):
            if i < -1 or j < -1:
                return 2
            if table[i + 1][j + 1] != 0:
                return table[i + 1][j + 1]

            if j == -1:
                if capital_contains[i]:
                    return 2
                else:
                    return 1
            if query[i] == pattern[j]:
                res = helper(i - 1, j - 1)
            else:
                if query[i].islower():
                    res = helper(i - 1, j)
                else:
                    res = 2
            table[i + 1][j + 1] = res
            return res

        ans = helper(n-1, m-1)
        return ans == 1

#
# s = Solution()
# print(s.camelMatch(["pglharjdshxbxsig"], "hrjdshxbxsig"))
# print(s.camelMatch(["ghrjdesqohxbxsig"], "hrjdshxbxsig"))
# # print(s.camelMatch(["FB"], "FB"))
# print(s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))
# print(s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],  "FoBa"))
# print(s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"))
# print(s.camelMatch(["aksvbjLiknuTzqon","mmkasvjLiknTxzqn"], "ksvjLiknTzqn"))
