class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
        next_hi = [0] * n
        next_lo = [0] * n

        stack = []
        for a, i in sorted((a, i) for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                idx = stack.pop()
                next_hi[idx] = i
            stack.append(i)

        stack = []
        for a, i in sorted((-a, i) for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                idx = stack.pop()
                next_lo[idx] = i
            stack.append(i)

        can_move_with_hi = [0] * n
        can_move_with_lo = [0] * n
        can_move_with_hi[n-1] = 1
        can_move_with_lo[n-1] = 1

        for i in range(n-2, -1, -1):
            can_move_with_hi[i] = can_move_with_lo[next_hi[i]]
            can_move_with_lo[i] = can_move_with_hi[next_lo[i]]
        return sum(can_move_with_hi)


# s = Solution()
# print(s.oddEvenJumps([1,2,3,2,1,4,4,5]))
# print(s.oddEvenJumps([2,1,4,4,5]))
# print(s.oddEvenJumps([2,1,4,4,5]))
# print(s.oddEvenJumps([14, 15]))
# print(s.oddEvenJumps([14]))
# print(s.oddEvenJumps([10,13,12,14,15]))
# print(s.oddEvenJumps([2,3,1,1,4]))
# print(s.oddEvenJumps([5,1,3,4,2]))
# print(s.oddEvenJumps([1,4,2]))
