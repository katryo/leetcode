class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = [[c for c in s]]

        last_layer = ans[-1]
        while True:
            next_layer = []
            for i in range(len(last_layer)-1):
                if i < len(last_layer)-1 and last_layer[i] == last_layer[i+1][::-1]:
                    next_layer.append(last_layer[:i] + [last_layer[i] + last_layer[i+1]] + last_layer[i+2:])
                if i < len(last_layer)-2 and last_layer[i] == last_layer[i+2][::-1]:
                    next_layer.append(last_layer[:i] + [last_layer[i] + last_layer[i+1] + last_layer[i+2]] + last_layer[i+3:])
            if next_layer == last_layer:
                break
            ans.extend(next_layer)
            last_layer = next_layer
        return ans


# s = Solution()
# print(s.partition("aab"))