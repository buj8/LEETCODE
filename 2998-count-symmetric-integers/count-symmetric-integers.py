class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for num in range(low, high+1):
            digits = str(num)
            if len(digits) % 2 != 0:
                continue
                
            half = len(digits) // 2
            left_sum = sum(int(digits[i]) for i in range(half))
            right_sum = sum(int(digits[i]) for i in range(half, len(digits)))
            
            if left_sum == right_sum:
                res += 1
                
        return res