from typing import List
from collections import defaultdict


class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        children = [set() for _ in range(N)]
        parents = [set() for _ in range(N)]
        not_yet_taken = set(range(N))
        for rel in relations:
            parent, child = rel
            children[parent-1].add(child-1)
            parents[child-1].add(parent-1)

        ans = 1
        # taken_set = set()
        for i in range(N+1):
            taken = set()
            for cand in not_yet_taken:
                if not parents[cand]:
                    taken.add(cand)
                    # taken_set.add(cand)
            for taken_course in taken:
                not_yet_taken.remove(taken_course)
                for child in children[taken_course]:
                    parents[child].remove(taken_course)
            if not not_yet_taken:
                return ans
            ans += 1
        return -1


# s = Solution()
# print(s.minimumSemesters(3, [[1,2],[2,3],[3,1]]))
# print(s.minimumSemesters(3, [[1,3],[2,3]]))

