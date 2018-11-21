import functools

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        letters = []
        digits = []
        for log in logs:
            elems = log.split(' ')
            if elems[1].isnumeric():
                digits.append(log)
            else:
                letters.append(log)

        def comparator(logstra, logstrb):
            elementsa = logstra.split(' ')
            logsa = elementsa[1:]
            idena = elementsa[0]

            elementsb = logstrb.split(' ')
            logsb = elementsb[1:]
            idenb = elementsb[0]

            if logsa == logsb:
                return idena < idenb

            i = 0
            while i < len(logsa) and i < len(logsb):
                if logsa[i] != logsb[i]:
                    if logsa[i] > logsb[i]:
                        return 1
                    else:
                        return -1
                i += 1
            if len(logsa) > len(logsb):
                return 1
            else:
                return -1

        letters.sort(key=functools.cmp_to_key(comparator))
        return letters + digits


s = Solution()
# print(s.reorderLogFiles(["a mo", "j mo", "5 m w", "g 07", "o 2 0", "t q h"]))
print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))