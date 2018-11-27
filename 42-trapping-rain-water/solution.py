class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and stack[-1][0] <= height[i]:
                hei, idx = stack.pop()
                if stack:
                    prev_height, prev_idx = stack[-1]
                    ans += (min(prev_height, height[i])-hei) * (i - 1 - prev_idx)
            stack.append((height[i], i))
        return ans

    def trap2(self, height):
        if not height:
            return 0
        max_from_left = [-1] * len(height)
        max_from_right = [-1] * len(height)

        max_from_left[0] = height[0]
        for i in range(1, len(height)):
            max_from_left[i] = max(max_from_left[i-1], height[i])

        max_from_right[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            max_from_right[i] = max(max_from_right[i+1], height[i])

        ans = 0
        for i in range(len(height)):
            max_on_both = min(max_from_right[i], max_from_left[i])
            if max_on_both > height[i]:
                ans += max_on_both-height[i]
        return ans

    def trap3(self, height):
        if not height:
            return 0
        leftmax = height[0]
        rightmax = height[len(height)-1]
        ans = 0
        left = 0
        right = len(height)-1
        while left < right:
            if height[left] < height[right]:
                if leftmax <= height[left]:
                    leftmax = height[left]
                else:
                    ans += leftmax-height[left]
                left += 1
            else:
                if rightmax <= height[right]:
                    rightmax = height[right]
                else:
                    ans += rightmax-height[right]
                right -= 1
        return ans



s = Solution()
print(s.trap([2, 1, 0, 3]))
print(s.trap([4,2,3]))
print(s.trap([0,1,0,2,1,0,1,3]))
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


print(s.trap2([2, 1, 0, 3]))
print(s.trap2([4,2,3]))
print(s.trap2([0,1,0,2,1,0,1,3]))
print(s.trap2([0,1,0,2,1,0,1,3,2,1,2,1]))

print(s.trap3([2, 1, 0, 3]))
print(s.trap3([4,2,3]))
print(s.trap3([0,1,0,2,1,0,1,3]))
print(s.trap3([0,1,0,2,1,0,1,3,2,1,2,1]))
