class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        if N < 11:
            return 0
        if N < 100:
            ans = 0
            for n in range(1, N):
                if n % 10 == n // 10:
                    ans += 1
            return ans

        n = N
        digits = 0
        while n:
            digits += 1
            n //= 10

        # table[i][j]: # of rep-digits of ith digit number. leftmost number is j+1.
        # table[i][j] = table[i-1][0] + table[i-1][1] + ... + table[i-1][9] + (i!)

        table = [[0] * 10 for _ in range(digits)]

        for i in range(10):
            table[1][i] = 1

        def non_rep_one_target(length):
            if length > 9:
                return 0
            ans = length
            l = length - 1
            num = 9
            while l:
                ans *= num
                l -= 1
                num -= 1
            return ans

        for i in range(2, digits):
            for j in range(10):
                table[i][j] = sum(table[i-1]) + non_rep_one_target(2)

        ans = 0
        for i in range(2, digits-1):
            ans += sum(table[digits-i][1:])
        return ans


s = Solution()
print(s.numDupDigitsAtMostN(1000))
