class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        carry = 0
        for i in range(len(A)-1, -1, -1):
            K, digit = divmod(K, 10)
            total = A[i] + digit + carry
            result = total % 10
            if total >= 10:
                carry = 1
            else:
                carry = 0
            A[i] = result

        def to_array(num):
            ans = []
            while num:
                num, dig = divmod(num, 10)
                ans.append(dig)
            return ans[::-1]

        return to_array(K + carry) + A


# s = Solution()
# print(s.addToArrayForm([9,9,9,9,9,9,9,9,9,9], 1))
# print(s.addToArrayForm([2,1,5], 806))
# print(s.addToArrayForm([2,7,4], 181))
