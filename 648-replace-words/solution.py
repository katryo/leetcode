# https://leetcode.com/problems/replace-words/solution/
# https://leetcode.com/problems/replace-words/discuss/105755/Python-Straightforward-with-Explanation-(Prefix-hash-Trie-solutions)

from collections import defaultdict


class Solution(object):
    def replaceWords(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return ' '.join(map(replace, sentence.split()))

    def replaceWords2(self, roots, sentence):
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            cur = trie
            for char in root:
                cur = cur[char]
            cur[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))


s = Solution()
print(s.replaceWords2(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
