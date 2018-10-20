from itertools import permutations


class Solution:
    def constructArray2(self, n, k):
        def is_valid(nums):
            seen = [False] * k
            for i in range(1, len(nums)):
                diff = abs(nums[i-1] - nums[i])
                if diff > k:
                    return False
                seen[diff-1] = True
            return all(seen)

        for cand in permutations(range(1, n)):
            if is_valid(cand):
                return cand
        return []

    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        move = k
        is_plus = True
        ans = list(range(1, n - k + 1))
        cur = n - k
        while move != 0:
            if is_plus:
                cur += move
                is_plus = False
            else:
                cur -= move
                is_plus = True
            ans.append(cur)
            move -= 1

        return ans


s = Solution()
print(s.constructArray2(10, 2))
