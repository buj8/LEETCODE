class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for num in range(low, high+1):
            digits = str(num)
            if len(digits) % 2 == 0:
                digits_l = [int(digits[i]) for i in range(len(digits)//2)]
                digits_r = [int(digits[i]) for i in range(len(digits)//2, len(digits))]
                if sum(digits_l) == sum(digits_r):
                    res += 1
        return res