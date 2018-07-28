import bisect

class ExamRoom(object):
    def __init__(self, N):
        """
        :type N: int
        """
        self.n = N
        self.students = []

    def seat(self):
        """
        :rtype: int
        """
        if not self.students:
            bisect.insort(self.students, 0)
            return 0

        ans_dist = self.students[0]
        ans_pos = 0
        for i, seat in enumerate(self.students):
            if not i:
                continue
            prev = self.students[i-1]
            dist = (seat - prev) // 2
            if dist > ans_dist:
                ans_pos = prev + dist
                ans_dist = dist

        if ans_dist < (self.n - 1) - self.students[-1]:
            ans_pos = self.n - 1

        bisect.insort(self.students, ans_pos)
        return ans_pos

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.students.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# N = 10
# obj = ExamRoom(N)
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# obj.leave(4)
# print(obj.seat())

N = 4
obj = ExamRoom(N)
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
obj.leave(1)
obj.leave(3)
print(obj.seat())
