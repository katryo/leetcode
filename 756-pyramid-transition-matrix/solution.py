from collections import defaultdict

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """

        # A A B
        # A B B
        colors = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        allowed_set = set(allowed)

        cache = defaultdict(set)

        def is_possible(left, right, top):
            return left + right + top in allowed_set

        def new_bases(base):
            if base in cache:
                return cache[base]
            ret = set()
            # Each color can be represented by a byte from 000 to 101, 0 to 6
            combinations = 7 ** (len(base)-1)
            for i in range(combinations):
                num = i
                new_base = [''] * (len(base)-1)
                is_failure = False
                for j in range(len(base)-1):
                    lsn = num % 7
                    if is_possible(base[j], base[j+1], colors[lsn]):
                        new_base[j] = colors[lsn]
                    else:
                        is_failure = True
                        break
                    num //= 7
                if is_failure:
                    continue
                ret.add(''.join(new_base))
            cache[base] = ret
            return ret

        def can_build(base):
            if len(base) == 1:
                return True
            possible_new_bases = new_bases(base)
            for new_base in possible_new_bases:
                if can_build(new_base):
                    return True
            return False

        return can_build(bottom)


# s = Solution()
# print(s.pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]))
# print(s.pyramidTransition("ABC", ["ABD", "BCE", "DEC", "FFF"]))
