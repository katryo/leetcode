# https://leetcode.com/problems/decode-string/discuss/87563/Share-my-Python-Stack-Simple-Solution-(Easy-to-understand)

class Solution:
    def decodeString(self, s):
        stack = [['', 1]]
        numstr = ''
        for ch in s:
            if ch.isdigit():
                numstr += ch
            if ch.isalpha():
                stack[-1][0] += ch
            if ch == '[':
                stack.append(['', int(numstr)])
                numstr = ''
            if ch == ']':
                text, k = stack.pop()
                stack[-1][0] += text * k
        return stack[0][0]


    # def decodeString(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #
    #     def decode_d(text):
    #         if not text:
    #             return ''
    #         i = 0
    #         digits = ''
    #         while text[i].isdigit():
    #             digits += text[i]
    #             i += 1
    #         k = int(digits)
    #         depth = 0
    #         start = i + 1
    #         while i < len(text):
    #             if text[i] == '[':
    #                 depth += 1
    #             if text[i] == ']':
    #                 depth -= 1
    #                 if depth == 0:
    #                     break
    #             i += 1
    #         ret_str = self.decodeString(text[start:i])
    #         multiplied = ret_str * k
    #         return multiplied + self.decodeString(text[i + 1:])
    #
    #     post = ''
    #     while s and s[-1] != ']':
    #         post = s[-1] + post
    #         s = s[:-1]
    #     pre = ''
    #     while s and not s[0].isdigit():
    #         pre += s[0]
    #         s = s[1:]
    #     return pre + decode_d(s) + post


s = Solution()
print(s.decodeString('3[ab]'))
print(s.decodeString('3[ab]2[cd]'))
print(s.decodeString('2[ab2[cd]]'))
