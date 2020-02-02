from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        # 1. start with 12.
        cur = 12

        # 2. Get the number of digits

        def num_digits(num):
            if num == 0:
                return 1
            ans = 0
            while num:
                num //= 10
                ans += 1
            return ans

        # e.g. 2 digits

        # 3. add 11111... (n 1s to n digits)
        # e.g. 3456

        def one_digits_num(d):
            num = 0
            for i in range(d):
                num += 10 ** i
            return num

        def seq_from_digits(d):
            num = 0
            for i in range(d+1):
                num = num * 10 + i
            return num

        ret = []

        while cur <= high:
            if low <= cur:
                ret.append(cur)

            digits = num_digits(cur)
            cur += one_digits_num(digits)
            if cur % 10 == 0:
                cur = seq_from_digits(digits+1)
        return ret

        # 4. Continues 3 until it reaches 9 or gt high
        # e.g. 4567, 5678, 6789

        # 5.From the # of digits (e.g. 4 digits), get the next seq (e.g. 12345)

s = Solution()
print(s.sequentialDigits(100, 300))
