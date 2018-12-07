class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        def hour(array):
            return int(array[0] * 10 + array[1])

        def minute(array):
            return int(array[2] * 10 + array[3])

        def is_valid(array):
            assert len(array) == 4
            hours = hour(array)
            if hours > 23:
                return False
            minutes = minute(array)
            if minutes > 59:
                return False
            return True

        def v_a_to_minutes(array):
            return hour(array) * 60 + minute(array)

        self.max_value = (-1, "")

        def backtrack(cur, rest):
            if len(cur) == 4 and is_valid(cur):
                minutes = v_a_to_minutes(cur)
                if self.max_value[0] < minutes:
                    time_str = ''.join([str(num) for num in cur])
                    self.max_value = (minutes, time_str[:2] + ":" + time_str[2:])
            for i in range(len(rest)):
                backtrack(cur + [rest[i]], rest[:i] + rest[i + 1:])

        backtrack([], A)
        return self.max_value[1]

s = Solution()
print(s.largestTimeFromDigits([0,0,0,0]))
# print(s.largestTimeFromDigits([1,2,3,4]))
