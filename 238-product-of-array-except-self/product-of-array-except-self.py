class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        res = [1 for num in nums]
        for i in range(len(nums)):
            res[i] *= left
            res[-i - 1] *= right
            left *= nums[i]
            right *= nums[-i - 1]
        return res