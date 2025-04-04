class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax, tmax = 0, 0, 0
        total = 0
        while l < r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)
            tmax = min(lmax, rmax)
            if height[l] < height[r]:
                d = max(tmax-height[l], 0)
                l += 1
            else:
                d = max(tmax-height[r], 0)
                r -= 1
            total += d
        return total