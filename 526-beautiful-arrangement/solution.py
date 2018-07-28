class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def helper(stack, arr):
            if not stack:
                return 1
            # stack = [2, 5]
            # e.g. arr == [4, -1, 3, 1, -1]

            ans = 0
            # helper([2, 5], [4, -1, 3, 1, -1]) == helper([2], [4, 5, 3, 1, -1]) + helper([2], [4, -1, 3, 1, -1])
            hand = stack.pop()
            if arr[hand-1] == -1 or arr[hand-1] % hand == 0 or hand % arr[hand-1] == 0:
                for i in range(len(arr)):
                    if arr[i] == -1:
                        if (i+1) % hand == 0 or hand % (i+1) == 0:
                            arr[i] = hand
                            ans += helper(stack, arr)
                            arr[i] = -1
            stack.append(hand)
            return ans

        stack = [i+1 for i in range(N)]
        arr = [-1] * N

        return helper(stack, arr)


# s = Solution()
# print(s.countArrangement(2))
# print(s.countArrangement(3))
# print(s.countArrangement(4))
# print(s.countArrangement(15))


