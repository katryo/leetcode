# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
#
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
#
# Could you do this in O(n) runtime?
#
# Example:
#
# Input: [3, 10, 5, 25, 2, 8]
#
# Output: 28
#
# Explanation: The maximum result is 5 ^ 25 = 28.


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #    11
        #  1010
        #   101
        # 11001
        #    10
        #  1000
        # 10010

        # Returns True if there is a pair of prefixes that pfx_a ^ pfx_b > cur
        # pfx ^ paired == cur ^ 1
        def can_improve(pfxs, cur):
            assert cur & 1 == 0
            for pfx in pfxs:
                paired = pfx ^ (cur + 1)
                if paired in pfxs:
                    return True
            return False

        current_max = 0
        for i in reversed(range(32)):
            current_max <<= 1
            prefixes = {num >> i for num in nums}
            if can_improve(prefixes, current_max):
                current_max += 1
        return current_max


# s = Solution()
# print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))


