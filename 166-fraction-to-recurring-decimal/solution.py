class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        ans = []
        if numerator == 0:
            return '0'
        if numerator == denominator:
            return '1'

        if numerator < 0 and denominator < 0:
            numerator = - numerator
            denominator = - denominator

        if numerator < 0:
            ans.append('-')
            numerator = - numerator
        if denominator < 0:
            ans.append('-')
            denominator = - denominator

        if numerator > denominator:
            quo = numerator // denominator
            numerator = (numerator % denominator) * 10
            if numerator == 0:
                ans.append(str(quo))
                return ''.join(ans)
            ans.append(str(quo) + '.')
        else:
            ans.append('0.')
            numerator *= 10

        counter = 0
        visited = {}
        while numerator:
            if numerator in visited:
                prev = visited[numerator]
                if ans[0] == '-':
                    ans.insert(2 + prev, '(')
                else:
                    ans.insert(1 + prev, '(')
                ans.append(')')
                break
            visited[numerator] = counter
            counter += 1
            if numerator == denominator:
                ans.append('1')
                break
            elif numerator > denominator:
                quo = numerator // denominator
                numerator = (numerator % denominator) * 10
                ans.append(str(quo))
            else:
                numerator *= 10
                ans.append('0')
        output = ''.join(ans)
        return output