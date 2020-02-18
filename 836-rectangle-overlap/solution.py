class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        def helper(rec):
            x1, y1, x2, y2 = rec
            xs = min(x1, x2)
            xl = max(x1, x2)
            ys = min(y1, y2)
            yl = max(y1, y2)
            return xs, xl, ys, yl

        xs_1, xl_1, ys_1, yl_1 = helper(rec1)
        xs_2, xl_2, ys_2, yl_2 = helper(rec2)

        assert xs_1 <= xl_1
        assert xs_2 <= xl_2

        if self.is_overlap(xs_1, xs_2, xl_1, xl_2):
            if self.is_overlap(ys_1, ys_2, yl_1, yl_2):
                return True
        return False

    def is_overlap(self, a1, b1, a2, b2):
        if a1 == a2 or b1 == b2:
            return False
        assert a1 < a2
        assert b1 < b2

        # A < B
        if a2 <= b1:
            return False
        # B < A
        if b2 <= a1:
            return False
        return True
