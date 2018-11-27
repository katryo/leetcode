class Solution:
    def longestValidParentheses(self, s):
        opening = {}
        stack = []
        ans = 0
        for i, par in enumerate(s):
            if par == '(':
                stack.append(i)
                if len(stack) not in opening:
                    opening[len(stack)] = i
            else:
                if stack:
                    layer = len(stack)
                    ans = max(ans, i-opening[layer])
                    if layer+1 in opening:
                        del opening[layer+1]
                    stack.pop()
                else:
                    # Reset
                    opening = {}
        if not ans:
            return 0
        return ans + 1

    def longestValidParentheses2(self, s):
        stack = [-1]
        ans = 0
        for i, par in enumerate(s):
            if par == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans


s = Solution()
print(s.longestValidParentheses2("(())()(()(("))
print(s.longestValidParentheses2(")()())"))
print(s.longestValidParentheses2("(()())"))
