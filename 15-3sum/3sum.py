class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            if num > 0:
                break
            l, r = i+1, len(nums)-1
            target = -num
            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum == target:
                    triplets.append([num, nums[l], nums[r]])
                    # Avoid repetitions!
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif twoSum < target:
                    l += 1
                else:
                    r -= 1

                
        return triplets