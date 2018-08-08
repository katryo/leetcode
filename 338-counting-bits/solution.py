class Solution(object):
    # def countBits(self, num):
    #     """
    #     :type num: int
    #     :rtype: List[int]
    #     """
    #     # Case0: LSB is 0
    #     # then +1
    #     # 11010110
    #
    #     # Case1: LSB is 1 and there is some 0
    #     # then - n where n is the least 0 bit's index
    #     # 10101011
    #
    #     # Case2: LSB is 1 and other bits are all 1s
    #     # then => 1
    #     # 11111111
    #
    #     def is_ones_all(number):
    #         while number:
    #             if number & 1 == 0:
    #                 return False
    #             number >>= 1
    #         return True
    #
    #     def ones_righter_than_zero(number):
    #         ret = 0
    #         while number & 1 == 1:
    #             ret += 1
    #             number >>= 1
    #         return ret
    #
    #     ans = [0] * (num+1)
    #     for i in range(num):
    #         bits = bin(i)[2:]
    #         if bits[-1] == '0':
    #             ans[i+1] = ans[i] + 1
    #         else:
    #             if is_ones_all(i):
    #                 ans[i+1] = 1
    #             else:
    #                 ans[i+1] = ans[i] - (ones_righter_than_zero(i) - 1)
    #     return ans

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 1010 : 10
        #  101 : 5
        # countBit(number) = countBit(number/2) if number is even

        ans = [0] * (num+1)

        def countBit(number):
            if number % 2 == 0:
                ans[number] = ans[number//2]
            else:
                ans[number] = ans[number//2]+1

        for i in range(num+1):
            countBit(i)
        return ans


# [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]
# s = Solution()
# print(s.countBits(16))
# print(s.countBits(0))
# print(s.countBits(1))
# print(s.countBits(2))
# print(s.countBits(5))
# print(s.countBits(10))
# print(s.countBits(100))
#
#
# print(s.countBits2(16))
# print(s.countBits2(0))
# print(s.countBits2(1))
# print(s.countBits2(2))
# print(s.countBits2(5))
# print(s.countBits2(10))
# print(s.countBits2(100))
