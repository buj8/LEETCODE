class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_nums = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in checked_nums:
                return [checked_nums[needed], i]
            checked_nums[num] = i