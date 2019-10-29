from typing import List
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        ps = defaultdict(set)
        ps[0].add("")
        word_longest = {"":0}
        ans = 1
        n = len(words)
        for i in range(n):
            w = words[i]
            word_longest[w] = word_longest.get(w, 1)
            ps[len(w)].add(w)
            for j in range(len(w)):
                prev_cand = w[:j] + w[j+1:]
                prevset = ps[len(prev_cand)]
                if prev_cand in prevset:
                    word_longest[w] = word_longest.get(prev_cand, 0) + 1
                    ans = max(ans, word_longest[w])

        return ans


s = Solution()
# print(s.longestStrChain(["msnq","klcbjhjm","znui","gy","msntlq","klcbqjhjm","zi","hwhzjgxzd","whzgxzd","zui","rmnqxy","msntzlq","jri","rbmnqxy","gqvbytgny","xh","wxkhyb","gqvbtgy","ctl","klcbqjhbjm","gbgy","klbh","erbmnqxy","mka","gvbtgy","klcbjhj","klbjh","zlnuci","gqvbytgy","mk","whzjgxzd","bgy","wxkhb","xkh","gvbgy","rmnxy","wxkh","msnlq","ct","hwhhzjgxzd","zlnui","klbjhj","jr","jrvi","rmny"]))
print(s.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))
# print(s.longestStrChain(["a","bdca","b","ba","bca","bda", "aaa"]))
# print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))
# print(s.longestStrChain(["a","b","ba","bdca","bdcaa","bdcaa","bdcaax"]))
