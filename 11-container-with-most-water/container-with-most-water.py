class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxarea = 0
        while l < r:
            w = r - l
            if height[l] < height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            maxarea = max(maxarea, h * w)

        return maxarea
