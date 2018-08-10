# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
#
# For 1-byte character, the first bit is a 0, followed by its unicode code.
# For n-bytes character, the first n-bits are all one's,
# the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
# This is how the UTF-8 encoding would work:
#
#    Char. number range  |        UTF-8 octet sequence
#       (hexadecimal)    |              (binary)
#    --------------------+---------------------------------------------
#    0000 0000-0000 007F | 0xxxxxxx
#    0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#    0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#    0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
#
# Note:
# The input is an array of integers.
# Only the least significant 8 bits of each integer is used to store the data.
# This means each integer represents only 1 byte of data.
#
# Example 1:
#
# data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.
#
# Return true.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
# Example 2:
#
# data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.
#
# Return false.
# The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
# The next byte is a continuation byte which starts with 10 and that's correct.
# But the second continuation byte does not start with 10, so it is invalid.


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        if not data:
            return False

        bin_data = [''] * len(data)
        for i in range(len(data)):
            bin_data[i] = bin(data[i])[2:]
            while len(bin_data[i]) < 8:
                bin_data[i] = '0' + bin_data[i]

        def what_byte_char(binary):
            if binary[0] == '0':
                return 1
            cur = 0
            while cur < len(binary) and binary[cur] == '1':
                cur += 1
            if cur < 2:
                return -1
            return cur

        def begins_with_10(binary):
            return binary[0] == '1' and binary[1] == '0'

        # print(bin_data)
        current = 0
        while current < len(bin_data):
            n = what_byte_char(bin_data[current])
            if n == -1:
                return False

            if n == 1:
                current += 1
                continue

            if n > 4:
                return False

            if n > len(bin_data) - current:
                return False

            for i in range(current+1, current+n):
                if not begins_with_10(bin_data[i]):
                    return False
            current += n
        return True


# s = Solution()
# print(s.validUtf8([145]))
# print(s.validUtf8([255]))
# print(s.validUtf8([197, 130, 1]))
# print(s.validUtf8([235, 140, 4]))
# print(s.validUtf8([230,136,145]))
# print(s.validUtf8([250,145,145,145,145]))
# print(s.validUtf8([115,100,102,231,154,132,13,10]))
