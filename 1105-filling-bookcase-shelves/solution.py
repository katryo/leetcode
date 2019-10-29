from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        first = coordinates[0]
        second = coordinates[1]

        if second[0] == first[0]:
            for i in range(2, n):
                if coordinates[i][0] != second[0]:
                    return False
            return True

        angle = (second[1] - first[1]) / (second[0] - first[0])
        y_section = first[1] - angle * first[0]

        for i in range(2, n):
            cur = coordinates[i]
            angle_cur = (cur[1] - first[1]) / (cur[0] - first[0])
            y_section_cur = first[1] - angle_cur * first[0]
            if angle == angle_cur and y_section == y_section_cur:
                continue
            else:
                return False
        return True


# s = Solution()
# print(s.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
# print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
