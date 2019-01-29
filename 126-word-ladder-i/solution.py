from collections import defaultdict


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wl = set(wordList)
        layer = {}
        layer[beginWord] = [[beginWord]]

        ans = []
        alphabets = [chr(x) for x in range(ord('a'), ord('z')+1)]

        def next_words(word):
            ans = []
            for i in range(len(word)):
                for c in alphabets:
                    candidate = word[:i] + c + word[i+1:]
                    if candidate in wl:
                        ans.append(candidate)
            return ans

        while layer:
            n_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    ans.extend(layer[word])
                paths = layer[word]
                n_words = next_words(word)
                for n_word in n_words:
                    new_paths = [path + [n_word] for path in paths]
                    n_layer[n_word].extend(new_paths)
            wl -= set(n_layer.keys())
            layer = n_layer
        return ans



# s = Solution()
# print(s.findLadders("a","c",["a","b","c"]))
# print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))




