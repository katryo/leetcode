class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ones = 0
        twos = 0
        for num in nums:
            add_to_twos = ones & num
            ones ^= num
            twos |= add_to_twos

            common = ones & twos
            mask = ~common
            ones &= mask
            twos &= mask
        return ones
    

s = Solution()
print(s.singleNumber([2,2,3,2]))
print(s.singleNumber([0,1,0,1,0,1,99]))
print(s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
print(s.singleNumber([-2,-2,1]))
print(s.singleNumber([-19,-46,-19,-46,-9,-9,-19,17,17,17,-13,-13,-9,-13,-46,-28]))
