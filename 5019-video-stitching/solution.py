from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        maxlen = T
        for clip in clips:
            maxlen = max(clip[1], maxlen)
        table = [float('inf')] * (maxlen+1)
        table[0] = 0

        for i in range(T+1):
            for clip in clips:
                start, end = clip[0], clip[1]
                if end >= i:
                    table[i] = min(table[i], table[start] + 1)
        if table[T] == float('inf'):
            return -1
        return table[T]


# s = Solution()
# print(s.videoStitching([[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]], 5))
# print(s.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))
# print(s.videoStitching([[0,1],[1,2]], 5))
# print(s.videoStitching( [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9))
# print(s.videoStitching([[0,4],[2,8]], 5))



