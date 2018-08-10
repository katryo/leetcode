from collections import defaultdict


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        table = defaultdict(set)
        for left, right, top in allowed:
            table[left, right].add(top)

        # Returns True if the given base can build a pyramid
        def can_build(base):
            if len(base) == 1:
                return True
            upper_rows = build(base, [], 0)
            for row in upper_rows:
                if can_build(row):
                    return True
            return False

        # Returns an array of rows that we can build
        # with the given (under-construction) row one block added
        def build(base, cur_row, idx):
            if idx == len(base)-1:
                return ["".join(cur_row)]

            result_rows = []
            for block in table[base[idx], base[idx+1]]:
                cur_row.append(block)
                built_row = build(base, cur_row, idx+1)
                for row in built_row:
                    result_rows.append(row)
                cur_row.pop()
            return result_rows
        return can_build(bottom)




s = Solution()
print(s.pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]))
print(s.pyramidTransition("ABC", ["ABD", "BCE", "DEC", "FFF"]))
