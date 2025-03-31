class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # First pass: calculate products to the left
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Second pass: multiply by products to the right
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result