class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        # [0, 1, 2, 3, 4]
        table = [[i, 0] for i, _ in enumerate(range(len(M)))]
        # 0 and 2 become friends
        # [2, 1, 2, 3, 4] or [0, 1, 0, 3, 4]

        def leader(tab, idx):
            cur_leader = tab[idx][0]
            while tab[cur_leader][0] != cur_leader:
                cur_leader = tab[cur_leader][0]
            return cur_leader

        def unite(tab, i, j):
            if leader(tab, j) == leader(tab, i):
                return
            la = leader(tab, i)
            lb = leader(tab, j)
            if tab[la][1] > tab[lb][1]:
                tab[lb][0] = la
            else:
                tab[la][0] = lb
                if tab[la][1] == tab[lb][1]:
                    tab[lb][1] += 1

        for i, person in enumerate(M):
            for j, relation in enumerate(person):
                if j == i:
                    continue
                if relation == 1:
                    unite(table, i, j)

        s = set()
        for idx, rank in table:
            s.add(leader(table, idx))

        return len(s)


if __name__ == '__main__':
    s = Solution()
    input0 = [[1, 0, 0, 1],
             [0, 1, 0, 1],
             [0, 0, 1, 0],
              [1, 1, 0, 1]]
    print(s.findCircleNum(input0))
    input = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]
    print(s.findCircleNum(input))

    i2 = [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]]
    print(s.findCircleNum(i2))

    i3 = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
          [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
          [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
          [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
          [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
          [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
          [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
          [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
    print(s.findCircleNum(i3))
