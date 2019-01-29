from collections import defaultdict


class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':
        multi = defaultdict(int)

        for i in range(len(A)):
            for j in range(len(A)):
                multi[A[i] & A[j]] += 1

        ans = 0
        for i in range(len(A)):
            for key in multi.keys():
                if key & A[i] == 0:
                    ans += multi[key]

        return ans


# s = Solution()
# print(s.countTriplets([2, 1, 3]))
