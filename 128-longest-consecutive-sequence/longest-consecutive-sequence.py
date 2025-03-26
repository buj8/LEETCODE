class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numset = set(nums)

        max_streak = 0

        for num in numset:
            if num-1 not in numset:
                current_streak = 1
                current_num = num + 1
                while current_num in numset:
                    current_streak += 1
                    current_num += 1
                max_streak = max(current_streak, max_streak)
        
        return max_streak