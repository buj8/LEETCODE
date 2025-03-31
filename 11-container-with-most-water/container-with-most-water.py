class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        mostwater = 0
        while l < r:
            currwater = (r - l) * min(height[l], height[r])
            mostwater = max(mostwater, currwater)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return mostwater
