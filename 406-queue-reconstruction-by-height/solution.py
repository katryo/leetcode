from collections import deque
from heapq import heappush

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """


        k_table = [[] for _ in range(len(people))]

        for person in people:
            k = person[1]
            h = person[0]
            heappush(k_table[k], h)

        def insert_ans(dq, h_k):
            counter = 0
            if not dq:
                dq.append(h_k)
                return
            for i, elem in enumerate(dq):
                if elem[1] == h_k[1]:
                    if elem[0] > h_k[0]:
                        dq.insert(i, h_k)
                        return
                    continue
                if counter == h_k[1]:
                    dq.insert(i, h_k)
                    return
                if elem[0] >= h_k[0]:
                    counter += 1
            dq.append(h_k)

        ans = deque()
        for k, hs in enumerate(k_table):
            for h in hs:
                insert_ans(ans, [h, k])
        return list(ans)

    def rq(self, people):
        sorted_people = sorted(people, key=lambda p: (-p[0], p[1]))
        ans = deque()

        for person in sorted_people:
            ans.insert(person[1], person)
        return list(ans)


if __name__ == '__main__':
    i0 = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    s = Solution()
    # print(s.reconstructQueue(i0))
    print(s.rq(i0))
