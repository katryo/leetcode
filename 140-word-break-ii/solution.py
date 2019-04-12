from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return
        res = []

        for word in wordDict:
            if not s.startswith(word):
                continue
            if s == word:
                res.append(word)
                continue
            rest = self.helper(s[len(word):], wordDict, memo)
            for item in rest:
                res.append(word + " " + item)
        memo[s] = res
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaa",
    #                   ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
    print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
