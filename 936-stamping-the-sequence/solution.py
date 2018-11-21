from collections import deque

# https://leetcode.com/articles/stamping-the-sequence/
class Solution:
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        s_width = len(stamp)
        t_width = len(target)

        q = deque()
        done = [False] * t_width
        ans = []
        windows = []

        for i in range(t_width - s_width + 1):
            made, todo = set(), set()

            for j, c in enumerate(stamp):
                c_target = target[i+j]
                if c_target == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            windows.append((made, todo))

            if not todo:
                ans.append(i)
                for j in range(i, i+s_width):
                    if not done[j]:
                        q.append(j)
                        done[j] = True

        while q:
            i = q.popleft()

            for j in range(max(0, i-s_width+1), min(t_width-s_width, i)+1):
                if i in windows[j][1]:
                    windows[j][1].discard(i)
                    if not windows[j][1]:
                        ans.append(j)
                        for m in windows[j][0]:
                            if not done[m]:
                                q.append(m)
                                done[m] = True

        return ans[::-1] if all(done) else []

s = Solution()
print(s.movesToStamp('abc', 'aabc'))
print(s.movesToStamp('abc', 'abababababc'))

