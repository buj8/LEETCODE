class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        maxarea = 0 
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxarea = max(area, maxarea)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxarea