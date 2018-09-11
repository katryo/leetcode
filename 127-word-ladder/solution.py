import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        ans = 1
        left = {beginWord}
        right = {endWord}
        words = set(wordList)

        if endWord not in words:
            return 0
        words.remove(endWord)

        while left:
            ans += 1
            new_left = set()
            for left_word in left:
                for i in range(len(left_word)):
                    for char in string.ascii_lowercase:
                        if char == left_word[i]:
                            continue
                        new_word = left_word[:i] + char + left_word[i+1:]
                        if new_word in right:
                            return ans
                        if new_word in words:
                            new_left.add(new_word)
                            words.remove(new_word)
            left = new_left
            if len(left) > len(right):
                left, right = right, left
        return 0


# s = Solution()
# print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))

