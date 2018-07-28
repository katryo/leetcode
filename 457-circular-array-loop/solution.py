class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def next(idx):
            return (idx + nums[idx]) % len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            pslow = i
            pfast = next(pslow)
            npfast = next(pfast)

            while nums[i] * nums[pfast] > 0 and nums[i] * nums[next(pfast)] > 0:
                if pfast == pslow:
                    if next(pslow) == pslow:
                        break
                    return True
                pfast = next(next(pfast))
                pslow = next(pslow)

            j = i
            while nums[j] != 0:
                nums[j] = 0
                nxt = next(j)
                j = nxt

        return False

# You are given an array of positive and negative integers.
# If a number n at an index is positive, then move forward n steps.
# Conversely, if it's negative (-n), move backward n steps.
# Assume the first element of the array is forward next to the last element,
# and the last element is backward next to the first element. Determine if there is a loop in this array.
# A loop starts and ends at a particular index with more than 1 element along the loop.
# The loop must be "forward" or "backward'.


if __name__ == '__main__':
    s = Solution()
    print(s.circularArrayLoop([3, 1, 2]))
    print(s.circularArrayLoop([-1]))
    print(s.circularArrayLoop([2, -1, 1, -2, -2]))
    print(s.circularArrayLoop([-2, 1, -1, -2, -2]))
    print(s.circularArrayLoop([2, -1, 1, 2, 2]))
    print(s.circularArrayLoop([-1, 2]))
