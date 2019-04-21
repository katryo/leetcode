from typing import List


class StreamChecker:
    def __init__(self, words: List[str]):
        self.tree = {}
        for word in words:
            cur = self.tree
            for c in word:
                if c in cur:
                    cur = cur[c]
                else:
                    cur[c] = {}
                    cur = cur[c]
            cur['END'] = True
        self.pointers = []

    def query(self, letter: str) -> bool:
        next_ps = []
        ans = False
        self.pointers.append(self.tree)
        for p in self.pointers:
            if letter in p:
                if 'END' in p[letter]:
                    ans = True
                next_ps.append(p[letter])
        self.pointers = next_ps
        return ans

# ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query"]
# [[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]

# sc = StreamChecker(["ab","ba","aaab","abab","baa"])
# # sc = StreamChecker(["ba","aaab", "baa"])
# for letter in "aaaaaba":
#     print(sc.query(letter))

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(["cd","f","kl"])
#
# for letter in "abcdefghijkl":
#     print(obj.query(letter))