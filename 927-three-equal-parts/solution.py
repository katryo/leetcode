class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        ones = sum(A)
        if ones % 3:
            return [-1, -1]

        ones_in_seg = ones // 3
        if ones_in_seg == 0:
            return [0, len(A)-1]

        breaks = []
        total = 0
        for i in range(len(A)):
            if A[i]:
                total += 1
                if total in {1, ones_in_seg+1, ones_in_seg * 2 + 1}:
                    breaks.append(i)
                if total in {ones_in_seg, ones_in_seg * 2, ones_in_seg * 3}:
                    breaks.append(i)

        i1, j1, i2, j2, i3, j3 = breaks
        if A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]:
            z1 = i2-j1-1
            z2 = i3-j2-1
            z3 = len(A)-j3-1

            if z1 < z3 or z2 < z3:
                return [-1, -1]
            return [j1+z3, j2+z3+1]
        else:
            return [-1, -1]




# s = Solution()
# print(s.threeEqualParts([1,1,1,1,1,1]))
# print(s.threeEqualParts([1,1,1,1,0,1,1]))
# print(s.threeEqualParts([0,1,1,1,1,1,1]))
# print(s.threeEqualParts([1,1,0,1,1,1,1]))
# print(s.threeEqualParts([1,1,1,1,1]))
# print(s.threeEqualParts([1,0,1,0,1]))
# print(s.threeEqualParts([1,0,1,1]))
# print(s.threeEqualParts([1,1,0,1]))
# print(s.threeEqualParts([1,1,1]))
# print(s.threeEqualParts([1,1,0]))
# print(s.threeEqualParts([0,1,0]))
# print(s.threeEqualParts([0,1,1]))
# print(s.threeEqualParts([1,0,0]))
# print(s.threeEqualParts([0,0,0]))
# print(s.threeEqualParts([1,1,0,1,1]))
