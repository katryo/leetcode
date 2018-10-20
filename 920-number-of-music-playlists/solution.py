# https://leetcode.com/articles/number-of-music-playlists/
# from functools import lru_cache


class Solution:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        table = [[-1] * (N+1) for _ in range(L+1)]

        table[0][0] = 1  # There is one playlist with length 0, #songs is zero
        for k in range(1, N+1):
            table[k][0] = 0

        # @lru_cache(None)
        def num_play_lists(i, j):
            # if i == 0:
            #     return +(j == 0)
            if i < 0 or j < 0:
                return 0
            if table[i][j] != -1:
                return table[i][j]
            # Sing a new song
            ret = num_play_lists(i-1, j-1) * (N-(j-1))

            # Repeat a song
            ret += num_play_lists(i-1, j) * max(j-K, 0)
            ret %= 10 ** 9 + 7
            table[i][j] = ret
            return ret

        return num_play_lists(L, N)


# s = Solution()
# print(s.numMusicPlaylists(3, 3, 1))
# print(s.numMusicPlaylists(2, 3, 0))
# print(s.numMusicPlaylists(2, 3, 1))
# print(s.numMusicPlaylists(20, 20, 15))
