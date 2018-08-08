class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        current_length = 0

        exited_at = -1
        for i in range(len(S)):
            c = S[i]
            if c.isdigit():
                # c is a digit
                current_length *= int(c)
            else:
                current_length += 1
            if current_length >= K:
                exited_at = i
                break

        for j in range(exited_at, -1, -1):
            c = S[j]
            K %= current_length
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                current_length /= int(c)
            else:
                current_length -= 1


# s = Solution()
# print(s.decodeAtIndex("leet2code3", 10))
# print(s.decodeAtIndex("ha22", 5))
