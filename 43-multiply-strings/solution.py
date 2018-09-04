class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == '0' or num2 == '0':
            return '0'
        ans = [0] * (len(num1) + len(num2))
        right_pos = len(num1) + len(num2) - 1

        for n1 in reversed(num1):
            pos = right_pos
            for n2 in reversed(num2):
                product = int(n1) * int(n2)
                ans[pos] += product
                ans[pos-1] += product // 10
                ans[pos] %= 10
                pos -= 1
            right_pos -= 1
        non_zero_start = 0
        while ans[non_zero_start] == 0 and non_zero_start < len(ans)-1:
            non_zero_start += 1
        return ''.join(map(str, ans[non_zero_start:]))

        # if num1 == '0' or num2 == '0':
        #     return '0'
        #
        # ans_digit_lists = []
        #
        # for p2 in range(len(num2) - 1, -1, -1):
        #     carry = 0
        #     ans_digit_list = []
        #     for i in range(len(num2) - 1 - p2):
        #         ans_digit_list.append(0)
        #     for p1 in range(len(num1) - 1, -1, -1):
        #         prod = int(num1[p1]) * int(num2[p2]) + carry
        #         ans_digit_list.insert(0, prod % 10)
        #         carry = prod // 10
        #     if carry:
        #         ans_digit_list.insert(0, carry)
        #     ans_digit_lists.append(ans_digit_list)
        #
        # ans_list = []
        # carry = 0
        # for i in range(-1, -len(ans_digit_lists[-1])-1, -1):
        #     total = sum([list[i] for list in ans_digit_lists if len(list) >= -i]) + carry
        #     digit = total % 10
        #     carry = total // 10
        #     ans_list.insert(0, str(digit))
        # if carry:
        #     ans_list.insert(0, str(carry))
        # return ''.join(ans_list)


s = Solution()
print(s.multiply("3", "2"))
print(s.multiply("3", "6"))
print(s.multiply("30", "6"))
print(s.multiply("30", "62"))
print(s.multiply("9133", "0"))
print(s.multiply("0", "21"))
