class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]

        ans = []
        for i in range(len(input)):
            cur = input[i]
            if cur == '+' or cur == '-' or cur == '*':
                left_nums = self.diffWaysToCompute(input[:i])
                right_nums = self.diffWaysToCompute(input[i+1:])
                for left in left_nums:
                    for right in right_nums:
                        if cur == '+':
                            ans.append(left+right)
                        if cur == '-':
                            ans.append(left-right)
                        if cur == '*':
                            ans.append(left*right)
        return ans


# s = Solution()
# print(s.diffWaysToCompute("2-1-1"))



