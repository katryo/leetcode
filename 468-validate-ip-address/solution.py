class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        2001:0db8:85a3:0000:0000:8a2e:0370:7334: valid
        2001:db8:85a3:0:0:8A2E:0370:7334: valid

        We can omit some leading zeroes before #

        """

        def is_valid_ipv6_val(val):
        #     2001:0db8:85a3::8A2E:0370:7334: invalid, empty
        #     02001:0db8:85a3:0000:0000:8a2e:0370:7334 invalid, extra leading zeroes
        #     2001:0db8:85a3:033:0:8A2E:0370:7334 valid, omitting zeroes
            if val == '':
                return False
            if len(val) > 4:
                return False
            for c in val.lower():
                if c not in '1234567890abcdef':
                    return False
            return True

        def is_valid_ipv4_val(val):
        # IPv4
        # 172.16.254.1: valid
        # 172.16.254.01: invalid, leading zeroes
            if val == '':
                return False
            if val == '0':
                return True
            for c in val:
                if c not in '1234567890':
                    return False
            if val[0] == '0':
                return False
            if 1 <= int(val) <= 255:
                return True
            return False

        # IPv6
        if ':' in IP:
            # Might be IPv6
            vals = IP.split(':')
            if len(vals) != 8:
                return 'Neither'
            for val in vals:
                if not is_valid_ipv6_val(val):
                    return 'Neither'
            return 'IPv6'
        elif '.' in IP:
            # Might be IPv4
            vals = IP.split('.')
            if len(vals) != 4:
                return 'Neither'
            for val in vals:
                if not is_valid_ipv4_val(val):
                    return 'Neither'
            return 'IPv4'
        return 'Neither'


s = Solution()
print(s.validIPAddress("172.16.254.1"))
print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(s.validIPAddress("2001:0db8:85a3:033:0:8A2E:0370:7334"))
print(s.validIPAddress("256.256.256.256"))
print(s.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334"))
print(s.validIPAddress("2001:0db8:85a3::8A2E:0370:7334"))
