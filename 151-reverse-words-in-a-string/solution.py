class Solution:
    # def reverseWords(self, s: str) -> str:
    #     words = s.split()
    #     words.reverse()
    #     return ' '.join(words)

    def reverseWords(self, s: str) -> str:
        n = len(s)
        submit = []
        is_prev_space = False
        cur = []
        for i in range(n-1, -1, -1):
            c = s[i]
            if c == ' ':
                is_prev_space = True
                continue
            if is_prev_space and cur:
                submit.append(''.join(cur[::-1]))
                cur = []
            cur.append(c)
            is_prev_space = False
        if cur:
            submit.append(''.join(cur[::-1]))
        return ' '.join(submit)

#
# s = Solution()
# print(s.reverseWords('the sky is blue'))
# print(s.reverseWords("a good   example"))
# print(s.reverseWords("a good   example"))
# print(s.reverseWords("  hello world!  "))
