class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        is_sharp = False
        sharp_nums = []
        ans_reverse = []
        for i in range(n - 1, -1, -1):
            char = s[i]
            if char == '#':
                is_sharp = True
                continue
            if is_sharp:
                sharp_nums.append(char)
            else:
                if sharp_nums:
                    sharp_nums.append(char)
                    string = ''.join(sharp_nums[::-1])
                    num = int(string)
                    ans_reverse.append(chr(ord('a') + num - 1))
                    sharp_nums = []
                else:
                    ord_diff_1 = ord(char) - ord('1')
                    ord_result = ord('a') + ord_diff_1
                    ans_reverse.append(chr(ord_result))
            is_sharp = False

        if sharp_nums:
            string = ''.join(sharp_nums)
            num = int(string)
            ans_reverse.append(chr(ord('a') + num))
        return ''.join(ans_reverse[::-1])


s = Solution()
print(s.freqAlphabets("10#11#12"))
print(s.freqAlphabets("1326#"))
print(s.freqAlphabets("25#"))
print(s.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
