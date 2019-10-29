class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for i in range(len(expression)):
            c = expression[i]
            if c == '!':
                stack.append('!')
            elif c == '&':
                stack.append('&')
            elif c == '|':
                stack.append('|')
            elif c == 'f':
                stack.append('f')
            elif c == 't':
                stack.append('t')
            elif c == ')':
                cur = []
                while stack[-1] == 't' or stack[-1] == 'f':
                    cur.append(stack[-1])
                    stack.pop()

                if stack[-1] == '&':
                    stack.pop()
                    if all([cur_c == 't' for cur_c in cur]):
                        stack.append('t')
                    else:
                        stack.append('f')
                elif stack[-1] == '|':
                    stack.pop()
                    if all([cur_c == 'f' for cur_c in cur]):
                        stack.append('f')
                    else:
                        stack.append('t')
                elif stack[-1] == '!':
                    stack.pop()
                    if cur[-1] == 't':
                        stack.append('f')
                    else:
                        stack.append('t')
                else:
                    assert True
        return stack[0] == 't'


if __name__ == '__main__':
    s = Solution()
    print(s.parseBoolExpr("!(&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))))"))
    print(s.parseBoolExpr("&(&(t), |(f,f))"))
    print(s.parseBoolExpr("!(f)"))
    print(s.parseBoolExpr("|(f,t)"))
    print(s.parseBoolExpr("&(t,f)"))
    print(s.parseBoolExpr("|(&(t,f,t),!(t))"))
