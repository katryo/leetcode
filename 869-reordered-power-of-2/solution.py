import collections


class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """

        # 1 2 3 4 5 6 7 8 9 0
        # 1, 2, 4, 8, ....

        num_str = str(N)

        def can_make(pot):
            pot_str = str(pot)
            if len(pot_str) != len(num_str):
                return False

            pot_dict = collections.defaultdict(int)
            for pot_char in pot_str:
                pot_dict[pot_char] += 1

            num_str_dict = collections.defaultdict(int)
            for num_char in num_str:
                num_str_dict[num_char] += 1

            for key in pot_dict:
                if pot_dict[key] != num_str_dict[key]:
                    return False
            return True

        power_of_two = 1
        while power_of_two <= 1000000000:
            if can_make(power_of_two):
                return True
            power_of_two *= 2
        return False

s = Solution()
print(s.reorderedPowerOf2(1))
print(s.reorderedPowerOf2(10))
print(s.reorderedPowerOf2(46))
print(s.reorderedPowerOf2(182))
