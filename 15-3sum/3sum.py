class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            if num > 0:
                break
            target = -num
            l, r = i+1, len(nums)-1
            while l < r:
                sumLR = nums[l] + nums[r]
                if sumLR == target:
                    res.append((num, nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l += 1
                    r -= 1 
                elif sumLR < target:
                    l += 1
                else:
                    r -= 1
        return res