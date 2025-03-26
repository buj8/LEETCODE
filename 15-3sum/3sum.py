class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_set = set()
        nums.sort()

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                sum3 = nums[i]+nums[l]+nums[r]
                if sum3 == 0:
                    res_set.add((nums[i], nums[l], nums[r]))
                    r-=1
                elif sum3 > 0:
                    r-=1
                else:
                    l+=1

        res = list(res_set)
        return res