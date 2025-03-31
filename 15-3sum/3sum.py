class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if num == nums[i] - 1:
                continue
            target = -num
            l, r = i+1, len(nums)-1
            while l < r:
                sumLR = nums[l] + nums[r]
                if sumLR == target:
                    res.add((num, nums[l], nums[r]))
                    l += 1 
                elif sumLR < target:
                    l += 1
                else:
                    r -= 1
        return list(res)