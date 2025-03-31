class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums = list(set(nums))
        nums.sort()
        l, r = 0, 1
        maxlen = 1
        while l < r and r < len(nums):
            if nums[r] != nums[r-1] + 1:
                l = r
            r += 1
            maxlen = max(maxlen, r-l)
        return maxlen

