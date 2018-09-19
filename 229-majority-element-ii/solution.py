from collections import Counter

class Solution:
    def majorityElement(self, nums):
        c = Counter()
        for num in nums:
            c[num] += 1
            if len(c) == 3:
                decr = Counter(set(c))
                c -= decr
        ans = [n for n in c if nums.count(n) > len(nums) // 3]

        return ans


    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #
    #     cand1 = -1
    #     count1 = 0
    #     cand2 = -1
    #     count2 = 0
    #     for num in nums:
    #         if num == cand1:
    #             count1 += 1
    #             continue
    #         if num == cand2:
    #             count2 += 1
    #             continue
    #         if count1 == 0:
    #             cand1 = num
    #             count1 += 1
    #             continue
    #         if count2 == 0:
    #             cand2 = num
    #             count2 += 1
    #             continue
    #         count1 -= 1
    #         count2 -= 1
    #
    #     c1 = 0
    #     c2 = 0
    #     for num in nums:
    #         if num == cand1:
    #             c1 += 1
    #             continue
    #         if num == cand2:
    #             c2 += 1
    #     ans = []
    #     if c1 > len(nums) // 3:
    #         ans.append(cand1)
    #     if c2 > len(nums) // 3:
    #         ans.append(cand2)
    #     return ans


s = Solution()
print(s.majorityElement([1,2,2,3,2,1,1,3]))
print(s.majorityElement([-1, -1]))
print(s.majorityElement([1]))
print(s.majorityElement([3]))
print(s.majorityElement([]))
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([3,3, 2,2,2, 1,1,1]))



