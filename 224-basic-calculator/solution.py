class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)

        stack = []
        sign = '+'

        cur = []
        for i in range(n):
            letter = s[i]
            if letter.isnumeric():
                cur.append(letter)

            # [x] TODO: handle i == n-1
            if cur and (i == n-1 or not letter.isnumeric()):
                # [x] TODO: handle digits
                # [x] TODO: Calculate for cur
                num = int(''.join(cur))
                cur = []
                if sign == '+':
                    adding = num
                else:
                    adding = - num
                if stack:
                    if isinstance(stack[-1], int):
                        stack[-1] += adding
                    # Handle a new ()
                    else:
                        stack.append(adding)
                else:
                    stack.append(adding)

            # TODO: handle + and -
            if letter == '+':
                sign = '+'
            if letter == '-':
                sign = '-'
            if letter == '(':
                stack.append(sign)
                sign = '+'
            if letter == ')':
                popped = stack.pop()
                tmp_sign = stack.pop()
                if tmp_sign == '+':
                    adding = popped
                else:
                    adding = -popped
                if stack:
                    stack[-1] += adding
                else:
                    stack.append(adding)
            # [x] TODO: handle whitespaces
        return stack[0]


# s = Solution()
# print(s.calculate("1-(5)"))
# print(s.calculate("1 + 1"))
# print(s.calculate(" 2-1 + 2 "))
# print(s.calculate("(1+(4+5+2)-3)+(6+8)"))









