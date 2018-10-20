from collections import defaultdict
from math import sqrt
from math import floor


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if not deck:
            return False
        table = defaultdict(int)
        for card in deck:
            table[card] += 1

        length = len(deck)

        def primes():
            for i in range(2, length+1):
                if length % i == 0:
                    yield i

        for prime in primes():
            divided = True
            for card in table:
                if table[card] % prime:
                    divided = False
                    break
            if divided:
                return True
        return False



# s = Solution()
# print(s.hasGroupsSizeX([1,1,1,2,2,2,3,3]))
# print(s.hasGroupsSizeX([1,2,3,4,4,3,2,1]))
# print(s.hasGroupsSizeX([1]))
# print(s.hasGroupsSizeX([1,1]))
# print(s.hasGroupsSizeX([1,2,1,2,2,2]))
# print(s.hasGroupsSizeX([0,0,0,0,0,1,1,1,1,1]))
