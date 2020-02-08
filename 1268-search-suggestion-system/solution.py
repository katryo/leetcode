from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = [{}, set()]
        for prod in products:
            cur = trie[0]
            for letter in prod:
                if not letter in cur:
                    cur[letter] = [{}, set()]
                cur[letter][1].add(prod)
                cur = cur[letter][0]

        ans = []
        cur_tree = trie
        len_ans = len(searchWord)
        for letter in searchWord:
            if letter in cur_tree[0]:
                cur_tree = cur_tree[0][letter]
                ans_words = list(cur_tree[1])
                ans_words.sort()
                ans.append(ans_words[:3])
            else:
                while len(ans) < len_ans:
                    ans.append([])
                return ans
        return ans
