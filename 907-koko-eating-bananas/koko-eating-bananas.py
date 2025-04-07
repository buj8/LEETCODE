class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getHours(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/speed)
            return hours

        high = max(piles)
        low = 1

        while low <= high:
            mid = low + (high - low) // 2
            hours = getHours(mid)
            if hours > h:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
