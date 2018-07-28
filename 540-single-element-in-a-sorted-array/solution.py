class Solution:

    def rec(self, nums, start, end):
        midi = (start + end) // 2
        if start == midi:
            return nums[midi]

        # 0 1 2 3 4 5 6
        # 1 1 3 3 7 8 8
        #     ^
        if midi % 2 == 0:
            pass
        else:
            midi -= 1

        # Case 1: midi is at left and target is on the right.
        # Case 2: midi is at right and target is in the left
        # Case 3: midi is the target

        # 0 1 2 3 4
        # 1 1 4 8 8
        #     ^


        if nums[midi] != nums[midi+1]:
            # midi is right, so target is in the left including midi.
            return self.rec(nums, start, midi)

        # midi is at left and target is on the right
        return self.rec(nums, midi+2, end)


    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.rec(nums, 0, len(nums)-1)


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2,3,3,4,4,8,8]
    print(s.singleNonDuplicate(nums))
    n2 = [3, 3, 7, 7, 10, 11, 11]

    print(s.singleNonDuplicate(n2))
