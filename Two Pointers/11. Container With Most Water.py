class Solution(object):
    def maxArea(self, height):
        maxarea = 0
        right = len(height) - 1
        left = 0
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[right], height[left]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxarea

