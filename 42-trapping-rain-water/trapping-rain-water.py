class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        maxL, maxR, maxH = 0, 0, 0 
        water = 0

        while l < r:
            curL = height[l]
            curR = height[r]

            maxL = max(maxL, curL)
            maxR = max(maxR, curR)
            maxH = min(maxL, maxR)

            if curL < curR:
                l += 1
                water += max(0, maxH - curL)
            else:
                r -= 1
                water += max(0, maxH - curR)
            
        return water