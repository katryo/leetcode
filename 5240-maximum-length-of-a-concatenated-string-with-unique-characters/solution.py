from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        # TODO: duplicate character in the str
        def to_num(str):
            ret = 0
            for c in str:
                order = ord(c)-ord('a')
                ret = ret | (2 ** order)
            return ret

        def no_dup(str):
            seen = set()
            for c in str:
                if c in seen:
                    return False
                seen.add(c)
            return True

        non_dup_arr = filter(no_dup, arr)

        nums = [to_num(str) for str in non_dup_arr]

        s = set()
        for num in nums:
            added = {num}
            for item in s:
                if item & num == 0:
                    added.add(item | num)
            s = s.union(added)

        def count_ones(n):
            ans = 0
            while n:
                ans += n % 2
                n //= 2
            return ans

        ans = 0
        for item in s:
            ans = max(ans, count_ones(item))
        return ans

# s = Solution()
# print(s.maxLength(["un","iq","ue"]))
# print(s.maxLength(["cha","r","act","ers"]))
# print(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
# print(s.maxLength(["yy","bkhwmpbiisbldzknpm"]))
