class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        n = len(height)
        l, r = 0, n-1
        lmax, rmax = 0, 0
        while l < r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)
            current_max = min(lmax, rmax)

            if height[l] < current_max:
                total_water += current_max - height[l]
            if height[r] < current_max:
                total_water += current_max - height[r]

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return total_water