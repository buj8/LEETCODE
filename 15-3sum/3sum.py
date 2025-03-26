class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_set = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                lrsum = nums[l]+nums[r]
                if lrsum == -nums[i]:
                    res_set.add((nums[i], nums[l], nums[r]))
                    r-=1
                elif lrsum > -nums[i]:
                    r-=1
                else:
                    l+=1

        res = list(res_set)
        return res