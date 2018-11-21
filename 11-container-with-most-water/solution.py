class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1

        ans = -1
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right-left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))