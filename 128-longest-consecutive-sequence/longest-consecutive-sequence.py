class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        numset = set(nums)
        maxlen = 0

        for num in numset:
            if num-1 not in numset:
                length = 1
                curr = num + 1
                while curr in numset:
                    length += 1
                    curr += 1
                maxlen = max(length, maxlen)

        return maxlen