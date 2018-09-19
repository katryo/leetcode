from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        has_non_zero = False
        for num in nums:
            if num != 0:
                has_non_zero = True
        if not has_non_zero:
            return '0'


        def compare(a, b):
            a = str(a)
            b = str(b)
            if int(a + b) > int(b + a):
                return -1
            if int(a+b) < int(b+a):
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare))
        numstrs = [str(num) for num in nums]
        return ''.join(numstrs)


# if __name__ == '__main__':
#     s = Solution()
#     print(s.largestNumber([121, 12]))
#     print(s.largestNumber([8247, 824]))
#     print(s.largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247]))
#     print(s.largestNumber([39, 10, 11, 1, 100]))
#     print(s.largestNumber([3,30,34,5,9]))
#     print(s.largestNumber([2, 10]))
