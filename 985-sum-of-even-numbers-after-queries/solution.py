class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        prev_ans = sum(x for x in A if x % 2 == 0)
        ans = []


        for q in queries:
            val, idx = q[0], q[1]
            cur = A[idx]
            A[idx] += val
            result = A[idx]

            if cur % 2:  # odd
                if result % 2:  # odd
                    pass
                else:
                    prev_ans += result
            else:  # even
                if result % 2:  # odd
                    prev_ans -= cur
                else:  # even
                    prev_ans = prev_ans - cur + result
            ans.append(prev_ans)
        return ans


# s = Solution()
# print(s.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))