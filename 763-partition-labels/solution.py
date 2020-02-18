from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        lasts = [-1] * 26

        n = len(S)
        for j in range(n):
            letter = S[j]
            lasts[ord(letter) - ord('a')] = j

        ans = []
        last_div = -1
        max_last = -1
        for i in range(n):
            letter = S[i]
            letter_i = ord(letter) - ord('a')
            max_last = max(max_last, lasts[letter_i])
            if max_last == i:
                ans.append(i - last_div)
                last_div = i
        return ans


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
