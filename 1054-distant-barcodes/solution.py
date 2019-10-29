from typing import List
from collections import defaultdict
from heapq import heapify, heappop, heappush


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)

        d = defaultdict(int)
        for barcode in barcodes:
            d[barcode] += 1

        n_key_list = []
        for key in d:
            n_key_list.append((d[key], key))
        n_key_list.sort(reverse=True)

        ans = [-1] * n
        cur = 0
        for i in range(0, n, 2):
            cur_n, cur_key = n_key_list[cur]
            ans[i] = cur_key
            if cur_n == 1:
                cur += 1
            else:
                n_key_list[cur] = (cur_n-1, cur_key)
        for i in range(1, n, 2):
            cur_n, cur_key = n_key_list[cur]
            ans[i] = cur_key
            if cur_n == 1:
                cur += 1
            else:
                n_key_list[cur] = (cur_n-1, cur_key)
        return ans


# s = Solution()
# print(s.rearrangeBarcodes([1,1,1,1,2,2,3,3]))
