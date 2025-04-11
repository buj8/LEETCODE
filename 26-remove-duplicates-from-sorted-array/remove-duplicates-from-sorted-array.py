class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        current = None
        while fast < len(nums):
            if current != nums[fast]:
                nums[slow] = nums[fast]
                current = nums[slow]
                slow += 1
            fast += 1
        
        return slow
