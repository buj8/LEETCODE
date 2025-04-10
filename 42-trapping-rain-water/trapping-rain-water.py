class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water = 0
        
        while left < right:
            if max_left < max_right:
                left += 1
                water += max(0, max_left - height[left])
                max_left = max(max_left, height[left])
            else:
                right -= 1
                water += max(0, max_right - height[right])
                max_right = max(max_right, height[right])
        
        return water