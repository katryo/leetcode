from collections import Counter, defaultdict

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # Trie tree
        self.tree = [{}, Counter()]
        self.letters = []
        
        n = len(sentences)
        
        for i in range(n):
            sentence = sentences[i]
            time = times[i]
            self.add_sentence(sentence, time)
            
        # print(self.tree)
        self.cur = self.tree
    
    def add_sentence(self, sentence, time):
        cur = self.tree
        for letter in sentence:
            if letter not in cur[0]:
                cur[0][letter] = [{}, Counter()]
            counter = cur[0][letter][1]
            counter[sentence] += time
            cur = cur[0][letter]
        
    def input(self, c: str) -> List[str]:
        
        if c == '#': # reset
            word = ''.join(self.letters)
            self.letters = []
            self.add_sentence(word, 1)
            self.cur = self.tree
            return []
        self.letters.append(c)
        
        
        if c in self.cur[0]:
            self.cur = self.cur[0][c]
            cur_counter = self.cur[1]
            cands = []
            for sent, count in cur_counter.items():
                cands.append((count, sent))
            
            cands.sort(key=lambda x: (-x[0], x[1]))
            ans = [cand[1] for cand in cands[:3]]

            return ans
        else:
            self.cur = [{}, Counter()]
            return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
