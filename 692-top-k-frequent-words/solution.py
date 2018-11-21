# https://leetcode.com/problems/top-k-frequent-words/solution/

from collections import Counter
from heapq import heappush
from heapq import heappop
from heapq import heapify


class MyCounter:
    def __init__(self, c, w):
        self.count = c
        self.word = w

    def __lt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        else:
            return self.count > other.count


class Solution:
    def topKFrequent(self, words, k):
        counter = Counter(words)
        keys = counter.keys()
        cands = sorted(keys, key=lambda word: (-counter[word], word))
        return cands[:k]

    # def topKFrequent(self, words, k):
    #     counter = Counter(words)
    #     heap = [(-freq, word) for word, freq in counter.items()]
    #     heapify(heap)
    #     return [heappop(heap)[1] for _ in range(k)]

    # def topKFrequent(self, words, k):
    #     """
    #     :type words: List[str]
    #     :type k: int
    #     :rtype: List[str]
    #     """
    #
    #     counter = Counter()
    #     for word in words:
    #         counter[word] += 1
    #
    #     heap = []
    #     for key in counter:
    #         mc = MyCounter(counter[key], key)
    #         heappush(heap, mc)
    #
    #     ans = []
    #     for i in range(k):
    #         ans.append(heappop(heap).word)
    #     return ans


s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
