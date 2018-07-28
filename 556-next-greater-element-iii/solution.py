class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def smallest_greater(num, arr):
            ret = (10, -1)
            for i in range(len(arr)):
                if ret[0] > arr[i] > num:
                    ret = (arr[i], i)
            return ret


        s = str(n)
        nums = [int(c) for c in s]
        if len(nums) < 2:
            return -1

        smallest_g = -1
        prev = nums[-1]
        pivot = -1
        what_i_will_sort = [prev]
        for i in range(len(nums)-2, -1, -1):
            cur = nums[i]
            if cur < prev:
                smallest_g, smallest_g_i = smallest_greater(cur, what_i_will_sort)
                what_i_will_sort.pop(smallest_g_i)
                what_i_will_sort.append(cur)
                pivot = i
                break
            what_i_will_sort.append(cur)
            prev = cur

        if pivot == -1:
            return -1

        what_i_will_sort.sort()
        ans = []
        for i in range(len(nums)):
            if i == pivot:
                ans.append(smallest_g)
                ans += what_i_will_sort
                final_answer = int(''.join([str(num) for num in ans]))
                if final_answer > 2147483647:
                    return -1
                return final_answer

            ans.append(nums[i])

        return -1

# s = Solution()
# print(s.nextGreaterElement(12))
# print(s.nextGreaterElement(21))
# print(s.nextGreaterElement(5923))
# print(s.nextGreaterElement(1001))
# print(s.nextGreaterElement(1000))
# print(s.nextGreaterElement(5199))
# print(s.nextGreaterElement(230241))
# print(s.nextGreaterElement(12443322))
