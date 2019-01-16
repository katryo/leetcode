class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        cur_line = []
        middle = []
        for i, word in enumerate(words):
            if sum([len(w) for w in cur_line + [word]]) + len(cur_line) > maxWidth:
                middle.append(cur_line)
                cur_line = [word]
            else:
                cur_line.append(word)
        if cur_line:
            middle.append(cur_line)

        ans = []
        for i, words_line in enumerate(middle):
            if len(words_line) == 1 or i == len(middle)-1:
                last_line = ' '.join(words_line)
                last_line += ' ' * (maxWidth - len(last_line))
                ans.append(last_line)
            else:
                word_spaces = sum([len(w) for w in words_line])
                count_spaces = maxWidth - word_spaces
                div, mod = divmod(count_spaces, len(words_line)-1)
                cur = ''
                for j, word in enumerate(words_line):
                    if j == len(words_line)-1:
                        cur += word
                    elif mod > 0:
                        cur = cur + word + ' ' * (div+1)
                        mod -= 1
                    else:
                        cur = cur + word + ' ' * div
                ans.append(cur)
        return ans


s = Solution()
# ans = s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
ans = s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
# ans = s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"], 20)
for line in ans:
    print(line)