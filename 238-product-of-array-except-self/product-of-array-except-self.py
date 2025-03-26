class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side = 1
        right_side = 1
        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] *= left_side
            res[-i-1] *= right_side
            left_side *= nums[i]
            right_side *= nums[-i-1]

        return res 