from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        tree = {}

        def add_path(tr, dirs):
            head = dirs[0]
            if len(dirs) == 1:
                tr[head] = '$'
            else:
                if head not in tr:
                    tr[head] = {}
                if tr[head] == '$':
                    return
                add_path(tr[head], dirs[1:])

        path_list = []
        for path in folder:
            dirs = path.split('/')[1:]
            path_list.append(dirs)

        for dirs in path_list:
            add_path(tree, dirs)


        def rec(tr):
            results = []
            for key in tr.keys():
                if tr[key] == '$':
                    results.append('/' + key)
                else:
                    next_results = rec(tr[key])
                    for next_result in next_results:
                        results.append('/' + key + next_result)
            return results

        return rec(tree)


# s = Solution()
# print((s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])))
# print((s.removeSubfolders(["/a","/a/b/c","/a/b/d"])))
# print((s.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])))
