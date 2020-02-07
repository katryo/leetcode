class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        num_name = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty'
        }

        tens_name = {
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }

        def helper(n):
            if n < 1000:
                if n == 0:
                    return ''
                thousands = n // 1000
                remaining = n % 1000
                hundreds = remaining // 100
                less_hundred = n % 100

                arr = []
                if thousands:
                    thousand_num_s = num_name[thousands]
                    arr.append(thousand_num_s)
                    arr.append('Thousand')
                if hundreds:
                    hundred_num = num_name[hundreds]
                    arr.append(hundred_num)
                    arr.append('Hundred')
                if less_hundred:
                    if less_hundred in num_name:
                        arr.append(num_name[less_hundred])
                    else:
                        tens = less_hundred // 10
                        if tens:
                            arr.append(tens_name[tens * 10])
                        ones = less_hundred % 10
                        if ones:
                            arr.append(num_name[ones])
                return ' '.join(arr)

            elif 1000 <= n < 1000_000:
                smaller_1000 = helper(n % 1000)
                greater_1000 = helper(n // 1000)
                ret = greater_1000 + ' Thousand'
                if smaller_1000:
                    ret += ' ' + smaller_1000
                return ret
            elif 1000_000 <= n < 1000_000_000:
                greater_million = helper(n // 1000_000)
                smaller_million = helper(n % 1000_000)

                ret = greater_million + ' Million'
                if smaller_million:
                    ret += ' ' + smaller_million
                return ret
            else:  # 1000_000_000 <= n
                greater_billion = helper(n // 1000_000_000)
                smaller_billion = helper(n % 1000_000_000)

                ret = greater_billion + ' Billion'
                if smaller_billion:
                    ret += ' ' + smaller_billion
                return ret

        return helper(num)