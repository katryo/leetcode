import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        s1_table = collections.defaultdict(int)
        needed_set = set()
        for char in s1:
            s1_table[char] += 1
            needed_set.add(char)

        window = s2[:len(s1)]

        for char in window:
            if char in s1_table:
                s1_table[char] -= 1
                if s1_table[char] == 0:
                    needed_set.remove(char)
        if not needed_set:
            return True

        for i in range(len(s2)-len(s1)):
            new_right_idx = i + len(s1)
            deleted_left_idx = i
            new_char = s2[new_right_idx]
            if new_char in s1_table:
                s1_table[new_char] -= 1
                if s1_table[new_char] == 0:
                    needed_set.remove(new_char)

            deleted_char = s2[deleted_left_idx]
            if deleted_char in s1_table:
                s1_table[deleted_char] += 1
                if s1_table[deleted_char] == 1:
                    needed_set.add(deleted_char)
            if not needed_set:
                return True
        return False


# s = Solution()
# print(s.checkInclusion("ab", "eidbaooo"))
# print(s.checkInclusion("ab", "eidboaoo"))
# print(s.checkInclusion("adc", "dcda"))
# print(s.checkInclusion("aa", "baa"))
# print(s.checkInclusion("aa", "aab"))
# print(s.checkInclusion("a", "ab"))
# print(s.checkInclusion("a", "b"))
