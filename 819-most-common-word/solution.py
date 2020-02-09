from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        # paragraph => words
        cur = []
        word_counter = Counter()
        n = len(paragraph)
        for i in range(n):
            letter = paragraph[i]
            if letter.isalpha():
                cur.append(letter.lower())
            
            if cur and (not letter.isalpha() or i == n-1):
                word = ''.join(cur)
                cur = []
                if word not in banned_set:
                    word_counter[word] += 1
        
        #print(word_counter)
        # word counter
        # {'bob': 2, 'hit': 2}
        word = word_counter.most_common(1)
        # print(word)
        return word[0][0]
        
        
