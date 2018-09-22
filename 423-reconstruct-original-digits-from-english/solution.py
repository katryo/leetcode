from collections import Counter

class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        zero = Counter('zero')
        one = Counter('one')
        two = Counter('two')
        three = Counter('three')
        four = Counter('four')
        five = Counter('five')
        six = Counter('six')
        seven = Counter('seven')
        eight = Counter('eight')
        nine = Counter('nine')
        counters = [
            (six, 6, 'six'),
            (two, 2, 'two'),
            (zero, 0, 'zero'),
            (four, 4, 'four'),
            (one, 1, 'one'),
            (seven, 7, 'seven'),
            (nine, 9, 'nine'),
            (five, 5, 'five'),
            (eight, 8, 'eight'),
            (three, 3, 'three'),
        ]

        txt = Counter(s)

        def contain(text_ctr, ctr):
            for key in ctr:
                if ctr[key] > text_ctr[key]:
                    return False
            return True

        ans_arr = [0] * 10
        for counter, num, name in counters:
            while contain(txt, counter):
                ans_arr[num] += 1
                txt -= counter

        ans = ''
        for i, num in enumerate(ans_arr):
            ans += str(i) * num
        return ans


s = Solution()
print(s.originalDigits("owoztneoer"))
print(s.originalDigits("fviefuro"))
print(s.originalDigits("zeroonetwothreefourfivesixseveneightnine"))

