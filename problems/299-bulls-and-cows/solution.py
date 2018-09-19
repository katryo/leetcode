from collections import Counter


class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        counter = Counter()
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            s = secret[i]
            g = guess[i]
            if s == g:
                bulls += 1
            else:
                if counter[s] < 0:
                    cows += 1
                if counter[g] > 0:
                    cows += 1
                counter[s] += 1
                counter[g] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'


s = Solution()
print(s.getHint("1807", "7810"))
