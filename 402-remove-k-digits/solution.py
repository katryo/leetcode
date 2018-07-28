class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        ans = []
        mid_point = -1
        for i, n in enumerate(num):
            broken = False
            while ans and ans[-1] > n:
                ans.pop()
                k -= 1
                if k == 0:
                    mid_point = i
                    broken = True
                    break
            ans.append(n)
            if broken:
                break

        for i in range(k):
            ans.pop()

        if mid_point != -1 and mid_point != len(num)-1:
            ans.extend(num[mid_point+1:])
        while ans and ans[0] == '0':
            ans.pop(0)
        if not ans:
            return '0'
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    num = "1432219"
    k = 3
    print(s.removeKdigits(num, k))

    num = "10"
    k = 2
    print(s.removeKdigits(num, k))

    num = "112"
    k = 1
    print(s.removeKdigits(num, k))
    num = "21"
    k = 1
    print(s.removeKdigits(num, k))
