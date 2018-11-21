from collections import Counter


class Solution:
    def numSubarraysWithSum3(self, A, S):
        total = [0] + [0] * len(A)
        for i in range(len(A)):
            total[i+1] = total[i] + A[i]

        # P = [0]
        # for x in A: P.append(P[-1] + x)

        counter = Counter()
        ans = 0
        for x in total:
            ans += counter[x]
            counter[x+S] += 1
        return ans

    def numSubarraysWithSum2(self, A, S):
        indexes = [-1] + [i for i, val in enumerate(A) if val] + [len(A)]
        ans = 0

        if S == 0:
            for i in range(len(indexes)-1):
                zeros = indexes[i+1] - indexes[i] + 1
                ans += zeros * (zeros+1) // 2
            return ans

        for i in range(1, len(indexes)-S):
            j = i + S - 1
            left = indexes[i] - indexes[i-1]
            right = indexes[j+1] - indexes[j]
            ans += left * right
        return ans

    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        sum_array = sum(A)
        idx = [-1] * sum_array
        p = 0
        for i in range(len(A)):
            if A[i] == 1:
                idx[p] = i
                p += 1

        total = 0
        start = 0
        j = 0
        ans = 0

        if S == 0:
            if not idx:
                return len(A) * (len(A)-1) // 2 + len(A)
            before = 0
            for i in range(len(idx)):
                ran = idx[i]-before
                if ran == 0:
                    pass
                elif ran == 1:
                    ans += 1
                else:
                    ans += ran * (ran-1) // 2 + ran
                before = idx[i]+1
            ran = len(A) - idx[-1] - 1
            if ran == 0:
                pass
            elif ran == 1:
                ans += 1
            else:
                ans += ran * (ran-1) // 2 + ran
            return ans

        for i in range(len(idx)):
            total += 1
            if total == S:
                if i == len(idx) - 1:
                    ans += (idx[j] - start + 1) * (len(A) - idx[i])
                else:
                    ans += (idx[j] - start + 1) * (idx[i + 1] - idx[i])  # todo: end case
                start = idx[j] + 1
                j += 1
                total -= 1
        return ans


s = Solution()
# print(s.numSubarraysWithSum([1,0,0,0,0,0,0,0,1], 0))
# print(s.numSubarraysWithSum([0,0,0,0,0,0,0], 0))
# print(s.numSubarraysWithSum([0,0,0,0,0,0,0,0], 0))
# print(s.numSubarraysWithSum([0, 0], 0))

# print(s.numSubarraysWithSum2([1,0,0,0,0,0,0,0,1], 0))
# print(s.numSubarraysWithSum2([0,0,0,0,0,0,0], 0))
# print(s.numSubarraysWithSum2([0,0,0,0,0,0,0,0], 0))

print(s.numSubarraysWithSum2([1,0,1], 2))
print(s.numSubarraysWithSum3([1,0,1], 2))
print(s.numSubarraysWithSum2([1,1,1], 2))
print(s.numSubarraysWithSum3([1,1,1], 2))
# print(s.numSubarraysWithSum2([1,0,1,1,0,0,1,0,1], 0))
# print(s.numSubarraysWithSum3([1,0,1,1,0,0,1,0,1], 0))

# print(s.numSubarraysWithSum([1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0], 0))
# print(s.numSubarraysWithSum([0,0,1], 2))
# print(s.numSubarraysWithSum([0,0,1,1], 2))
# print(s.numSubarraysWithSum([0], 2))
# print(s.numSubarraysWithSum([], 2))
# print(s.numSubarraysWithSum([], 0))
# print(s.numSubarraysWithSum([0], 0))
# print(s.numSubarraysWithSum([0,0], 0))
# print(s.numSubarraysWithSum([1,0,0], 0))
# print(s.numSubarraysWithSum([0,1,0,0], 0))
# print(s.numSubarraysWithSum([0,0,1,0,0], 0))

# print(s.numSubarraysWithSum([], 1))
# print(s.numSubarraysWithSum([1], 1))
# print(s.numSubarraysWithSum([1,0], 1))
# print(s.numSubarraysWithSum([0,1], 1))
# print(s.numSubarraysWithSum([1,0,1,0,1], 2))
# print(s.numSubarraysWithSum([1,0,1,0,1,0], 2))
# print(s.numSubarraysWithSum([0,1,0,1,0,1], 2))
# print(s.numSubarraysWithSum([0,1,0,1,0,1,0], 2))
