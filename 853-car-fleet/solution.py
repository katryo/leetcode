class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if not position:
            return 0

        pos_speed_tuples = []
        for i in range(len(position)):
            pos_speed_tuples.append((position[i], speed[i]))
        pos_speed_tuples.sort(reverse=True)

        fleet = pos_speed_tuples[0]
        ans = len(position)
        for pos, sp in pos_speed_tuples[1:]:
            if sp - fleet[1] <= 0:
                fleet = (pos, sp)
                continue

            bump_time = float((fleet[0] - pos)) / float((sp - fleet[1]))

            bump_point = pos + sp * bump_time
            if fleet[0] <= bump_point <= target:
                # fleet does not change
                ans -= 1
            else:
                fleet = (pos, sp)

        return ans

s = Solution()
print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(s.carFleet(10, [2, 4], [3, 2]))
print(s.carFleet(20, [6,2,17], [3,9,2]))
print(s.carFleet(13, [10,2,5,7,4,6,11], [7,5,10,5,9,4,1]))


