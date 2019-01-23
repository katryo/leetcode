from collections import defaultdict
from heapq import heappush
from heapq import heappop

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList.append(beginWord)
        graph = defaultdict(set)

        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(wordList)):
                if i == j:
                    continue
                diff = 0
                for k in range(len(word)):
                    if word[k] != wordList[j][k]:
                        diff += 1
                if diff == 1:
                    word_j = wordList[j]
                    graph[word].add(word_j)
                    graph[word_j].add(word)

        fronteer = [(0, beginWord, [beginWord])]
        min_path = {}
        ans = []
        while fronteer:
            cost, new_point, path = heappop(fronteer)
            if endWord in min_path and min_path[endWord][0] < cost:
                break
            if new_point == endWord:
                if new_point in min_path and min_path[new_point][0] < cost:
                    continue
                ans.append(path)
            min_path[new_point] = cost, path
            candidates = graph[new_point]
            for cand in candidates:
                if cand not in min_path or min_path[cand][1] == cost+1:
                    heappush(fronteer, (cost+1, cand, path + [cand]))

        return ans


# s = Solution()
# print(s.findLadders("a","c",["a","b","c"]))
# print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))




