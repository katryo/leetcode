# https://leetcode.com/articles/3sum-with-multiplicity/

from collections import Counter


class Solution:
    def threeSumMulti3(self, A, target):
        counter = Counter(A)
        keys = sorted(counter)
        MOD = 10 ** 9 + 7
        ans = 0

        for i, x in enumerate(counter):
            total = target - x
            j = i
            k = len(keys)-1

            while j <= k:
                y = keys[j]
                z = keys[k]

                if y + z > total:
                    k -= 1
                    continue
                if y + z < total:
                    j += 1
                    continue

                assert x + y + z == target
                if i < j < k:
                    ans += counter[x] * counter[y] * counter[z]
                elif i == j < k:
                    ans += counter[x] * (counter[x]-1) // 2 * counter[z]
                elif i < j == k:
                    ans += counter[x] * counter[y] * (counter[y]-1) // 2
                else:  # i == j == k
                    ans += counter[x] * (counter[x]-1) * (counter[x]-2) // 6
                ans %= MOD
                j += 1
                k -= 1
        return ans


    def threeSumMulti2(self, A, target):
        A.sort()
        MOD = 10 ** 9 + 7

        ans = 0
        for i in range(len(A)):
            total = target - A[i]
            j = i+1
            k = len(A)-1

            while j < k:
                if A[j] + A[k] < total:
                    j += 1
                elif A[j] + A[k] > total:
                    k -= 1
                elif A[j] == A[k]:
                    ans += (k-j+1) * (k-j) // 2
                    ans %= MOD
                    break
                else:
                    left = 1
                    right = 1
                    while j+1 < k and A[j] == A[j+1]:
                        j += 1
                        left += 1
                    while j < k-1 and A[k] == A[k-1]:
                        k -= 1
                        right += 1
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1
        return ans


    def threeSumMulti(self, A, target):
        data = [0] * 101
        for a in A:
            data[a] += 1

        MOD = 10 ** 9 + 7

        table = [-1] * 3001
        table[0] = 1
        table[1] = 1

        def fact(x):
            if table[x] != -1:
                return table[x]
            table[x] = fact(x - 1) * x
            return table[x]

        def combi(a, b):
            return fact(a) // (fact(b) * fact(a-b))

        ans = 0
        # 1. A[i] < A[j] < A[k]
        for i in range(101):
            if data[i] == 0:
                continue
            for j in range(i, 101):
                if data[j] == 0:
                    continue
                for k in range(j, 101):
                    if data[k] == 0:
                        continue
                    if i + j + k == target:
                        if i == j == k:
                            if data[i] < 3:
                                continue
                            ans += combi(data[i], 3)
                        elif i == j:
                            if data[i] < 2:
                                continue
                            ans += combi(data[i], 2) * data[k]
                        elif j == k:
                            if data[j] < 2:
                                continue
                            ans += combi(data[j], 2) * data[i]
                        else:
                            ans += data[i] * data[j] * data[k]
                        ans %= MOD
        return ans


s = Solution()
print(s.threeSumMulti([0, 0, 0], 0))
print(s.threeSumMulti([0, 0, 0, 0], 0))
print(s.threeSumMulti([0, 0, 0, 0, 0], 0))
print(s.threeSumMulti([1,1,2], 5))
print(s.threeSumMulti([1,1,2], 4))
print(s.threeSumMulti([0, 0, 0], 4))
print(s.threeSumMulti([1,1,2,2,2,2], 5))
print(s.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))

s2 = Solution()
print(s2.threeSumMulti2([0, 0, 0], 0))
print(s2.threeSumMulti2([0, 0, 0, 0], 0))
print(s2.threeSumMulti2([0, 0, 0, 0, 0], 0))
print(s2.threeSumMulti2([1,1,2], 5))
print(s2.threeSumMulti2([0, 0, 0], 4))
print(s2.threeSumMulti2([1,1,2,2,2,2], 5))
print(s2.threeSumMulti2([1,1,2,2,3,3,4,4,5,5], 8))

print(s2.threeSumMulti3([0, 0, 0], 0))
print(s2.threeSumMulti3([0, 0, 0, 0], 0))
print(s2.threeSumMulti3([0, 0, 0, 0, 0], 0))
print(s2.threeSumMulti3([1,1,2], 5))
print(s2.threeSumMulti3([0, 0, 0], 4))
print(s2.threeSumMulti3([1,1,2,2,2,2], 5))
print(s2.threeSumMulti3([1,1,2,2,3,3,4,4,5,5], 8))
