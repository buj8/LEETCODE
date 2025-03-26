class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l, r = 0, 1
        currentlen, maxlen = 1, 1
        nums.sort()
        while r < len(nums):
            if nums[l] + 1 == nums[r]:
                r+=1
                l+=1
                currentlen += 1
            elif nums[l] == nums[r]:
                r+=1
                l+=1
            else:
                currentlen = 1
                l=r
                r+=1
            maxlen = max(maxlen, currentlen)

        return maxlen
        