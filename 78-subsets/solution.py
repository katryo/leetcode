class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        possible_combinations = 2 ** len(nums)

        answers = []
        for i in range(possible_combinations):
            bitset = bin(i)[2:]
            while len(bitset) < len(nums):
                bitset = "0" + bitset

            answer = []
            for j in range(len(bitset)):
                if bitset[j] == '1':
                    answer.append(nums[j])
            answers.append(answer)
        return answers




