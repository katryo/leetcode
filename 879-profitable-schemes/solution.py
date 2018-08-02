class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        # table[g][p] # #schemes can achieve p profit with g gangs where.
        # if p == P then #schemes can achieve P or more profit
        table = [[0] * (P+1) for _ in range(G+1)]
        table[0][0] = 1

        for g_required, p_get in zip(group, profit):
            # We do the scheme and get p_get using g_required gangs
            new_table = [row[:] for row in table]

            for current_p in range(P+1):
                for current_g in range(G+1 - g_required):
                    total_g = current_g + g_required
                    total_p = min(P, current_p + p_get)
                    new_table[total_g][total_p] += table[current_g][current_p]
                    new_table[total_g][total_p] %= MOD
            table = new_table

        ans = 0
        for g in range(G+1):
            ans += table[g][P]
            ans %= MOD
        return ans


s = Solution()
print(s.profitableSchemes(5, 3, [2, 2], [2, 3]))
# print(s.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))
# print(s.profitableSchemes(1, 1, [1,1,1,1,2,2,1,2,1,1],[0,1,0,0,1,1,1,0,2,2]))

# G = 10, P = 5, group = [2,3,5], profit = [6,7,8]