class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        BLANK = 0
        DIGIT = 1
        DOT = 2
        E = 3
        SIGN = 4
        OTHER = -1

        states = {
            'start': {BLANK: 'start', DIGIT: 'int', SIGN: 'sign', DOT: 'dotstart'},  # beginning
            'int': {DIGIT: 'int', DOT: 'dot', E: 'e', BLANK: 'space'},  # 3, end
            'dotstart': {DIGIT: 'dotnum'},
            'dot': {DIGIT: 'dotnum', BLANK: 'space', E: 'e'},  # 3., end
            'dotnum': {DIGIT: 'dotnum', E: 'e', BLANK: 'space'},  # 3.60, end
            'e': {DIGIT: 'eint', SIGN: 'esign'},  # 12e
            'eint': {DIGIT: 'eint', BLANK: 'space'},  # 12e1, end
            'esign': {DIGIT: 'esignnum'},  # 12e-
            'esignnum': {DIGIT: 'esignnum', BLANK: 'space'},  # 12e-4, end
            'sign': {DIGIT: 'signnum', DOT: 'dotstart'},  # -
            'signnum': {E: 'e', DIGIT: 'signnum', BLANK: 'space', DOT: 'dot'},  # -5, end
            'space': {BLANK: 'space'} # 12 , end
        }

        cur = 'start'
        for c in s:
            action = OTHER
            if c == ' ':
                action = BLANK
            elif c == '.':
                action = DOT
            elif c == 'e':
                action = E
            elif c == '-' or c == '+':
                action = SIGN
            elif c.isdigit():
                action = DIGIT
            if action in states[cur]:
                cur = states[cur][action]
            else:
                return False
        if cur in ('int', 'dotnum', 'eint', 'esignnum', 'signnum', 'space', 'dot'):
            return True
        return False


# s = Solution()
# print(s.isNumber("46.e3"))
# print(s.isNumber("."))
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false