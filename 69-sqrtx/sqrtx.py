class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x 

        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            mid_sq = mid * mid
            if mid_sq == x:
                return mid
            elif mid_sq < x:
                low = mid + 1
            else:
                high = mid - 1

        if mid_sq < x:
            return mid
        return high