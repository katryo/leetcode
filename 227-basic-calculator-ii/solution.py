class Solution:
    def calculate(self, s):
        if not s:
            return 0
        stack = []
        sign = '+'
        num = 0
        for i in range(len(s)):
            if s[i].isspace():
                continue
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if not s[i].isdigit() or i == len(s)-1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp//num + 1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
        return sum(stack)

    # def calculate(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     if not s:
    #         return 0
    #     new_s = []
    #     i = 0
    #     while i < len(s):
    #         if s[i] == ' ':
    #             i += 1
    #             continue
    #         if s[i].isdigit():
    #             cur = s[i]
    #             while i < len(s)-1 and s[i+1].isdigit():
    #                 i += 1
    #                 cur += s[i]
    #             new_s.append(cur)
    #             i += 1
    #             continue
    #         new_s.append(s[i])
    #         i += 1
    #     s = new_s
    #
    #     stack = []
    #     cur_operation = ''
    #     for i in range(len(s)):
    #         if s[i] == ' ':
    #             continue
    #         if s[i] == '/':
    #             cur_operation = '/'
    #             continue
    #         if s[i] == '*':
    #             cur_operation = '*'
    #             continue
    #         if s[i] == '+' or s[i] == '-':
    #             cur_operation = ''
    #             stack.append(s[i])
    #             continue
    #         else:
    #             if cur_operation == '/':
    #                 latest = stack.pop()
    #
    #                 result = int(latest) // int(s[i])
    #                 stack.append(str(result))
    #             elif cur_operation == '*':
    #                 latest = stack.pop()
    #
    #                 stack.append(str(int(latest) * int(s[i])))
    #             else:
    #                 if stack:
    #                     latest = stack.pop()
    #                     if latest.isdigit():
    #                         result = latest + s[i]
    #                         stack.append(result)
    #                     else:
    #                         stack.append(latest)
    #                         stack.append(s[i])
    #                 else:
    #                     stack.append(s[i])
    #             cur_operation = ''
    #     cur = int(stack[0])
    #     cur_ope = ''
    #     for i in range(1, len(stack)):
    #         if stack[i] == '-':
    #             cur_ope = '-'
    #             continue
    #         if stack[i] == '+':
    #             cur_ope = '+'
    #             continue
    #         if cur_ope == '+':
    #             cur = cur + int(stack[i])
    #         else:
    #             cur = cur - int(stack[i])
    #     return cur


s = Solution()
print(s.calculate(" 3+5 / 2 "))
print(s.calculate("3+2*2"))
print(s.calculate(" 3 / 2"))
print(s.calculate(" 42 "))
print(s.calculate("1*2-3/4+5*6-7*8+9/10"))
