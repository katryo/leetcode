import math


class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        def divisors(number):
            ans = 2
            for div in range(number // 2, 1, -1):
                if number % div == 0:
                    pre = number // div
                    if len(divs) > pre:
                        ans = divs[pre]
                        divs.append(ans)
                        break
                    ans += 1
            divs.append(ans)
            return ans

        divs = [0, 1, 2]
        ans = 1
        for num in range(3, n + 1):
            # print(num, divisors(num))
            if divisors(num) % 2:
                ans += 1
        # print(divs)
        return ans


s = Solution()
# print(s.bulbSwitch(1))
# print(s.bulbSwitch(2))
# print(s.bulbSwitch(3))
# print(s.bulbSwitch(4))
# print(s.bulbSwitch(5))
# print(s.bulbSwitch(6))
print(s.bulbSwitch(100))
