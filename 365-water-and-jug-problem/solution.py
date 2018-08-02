class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        if x + y < z:
            return False
        if x == z or y == z or x + y == z:
            return True

        # table[i][j]: tried?
        table = [[0] * (y+1) for _ in range(x+1)]

        def search(X, Y):
            if X == z or Y == z or X+Y == z:
                return True
            # if table[X][Y]:
            #     return False
            # fill x
            if table[x][Y] == 0:
                table[x][Y] = 1
                if search(x, Y):
                    return True

            # fill y
            if table[X][y] == 0:
                table[X][y] = 1
                if search(X, y):
                    return True
            # drop X
            if table[0][Y] == 0:
                table[0][Y] = 1
                if search(0, Y):
                    return True

            # drop Y
            if table[X][0] == 0:
                table[X][0] = 1
                if search(X, 0):
                    return True

            # Pour water from x to y
            if X > 0:
                amount_to_pour = min(y - Y, X)
                if table[X-amount_to_pour][Y+amount_to_pour] == 0:
                    table[X-amount_to_pour][Y+amount_to_pour] = 1
                    if search(X-amount_to_pour, Y+amount_to_pour):
                        return True

            # Pour water from Y to X
            if Y > 0:
                amount_to_pour = min(x - X, Y)
                if table[X+amount_to_pour][Y-amount_to_pour] == 0:
                    table[X+amount_to_pour][Y-amount_to_pour] = 1
                    if search(X+amount_to_pour, Y-amount_to_pour):
                        return True
            table[X][Y] = 1
            return False

        return search(x, y)


s  = Solution()
# print(s.canMeasureWater(1, 2, 3))
# print(s.canMeasureWater(3, 5, 4))
# print(s.canMeasureWater(2, 6, 5))
print(s.canMeasureWater(22003, 31237, 1))