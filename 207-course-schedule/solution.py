from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = defaultdict(list)
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        global_visited = set()

        def dfs_has_loop(target, visited):
            if target in visited:
                return True
            visited.add(target)

            global_visited.add(target)

            if target in graph:
                children = graph[target]
                for child in children:
                    if dfs_has_loop(child, visited):
                        return True
            visited.remove(target)
            return False

        for course in graph:
            if course in global_visited:
                continue
            if dfs_has_loop(course, set()):
                return False
        return True


# s = Solution()
# print(s.canFinish(4, [[0, 1], [3, 1], [1, 3], [3, 2]]))
# print(s.canFinish(2, [[1,0], [0,1]]))
# print(s.canFinish(2, [[1,0]]))
# print(s.canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))
