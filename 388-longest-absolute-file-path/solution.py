class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lines = input.splitlines()

        def remove_tab(text):
            count = 0
            while len(text) > 1 and text.startswith('\t'):
                text = text[1:]
                count += 1
            return text, count

        cur = []
        cur_cnt = -1
        ans = 0
        for i in range(len(lines)):
            txt, cnt = remove_tab(lines[i])
            if cnt > cur_cnt:
                cur.append(txt)
                cur_cnt += 1
            elif cnt == cur_cnt:
                cur.pop()
                cur.append(txt)
            else:
                diff = cur_cnt - cnt
                for j in range(diff):
                    cur.pop()
                cur.pop()
                cur.append(txt)
                cur_cnt = cnt
            path = '/'.join(cur)
            if len(path) > ans and '.' in txt:
                ans = len(path)
        return ans


# s = Solution()
# # print(s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
# print(s.lengthLongestPath("a\n\tb\n\t\tc.txt"))
