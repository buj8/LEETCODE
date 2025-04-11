class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        
        # IDEA: 
        # - Sort the array
        # - Iterate num by num
        # - For each num, do two pointers
        #   - L = starts as the number after num 
        #   - R = starts as the last num of the array
        # >>> Time complexity -> O(n) * O(n)  = O(n^2)
        # >>> Space complexity -> O(1) (not taking into account the output array)
        print(nums)

        for i, num in enumerate(nums):
            # Avoid repetition
            if i > 0 and nums[i - 1] == num:
                continue
            # 3 positive values won't output 0 (nums is sorted)
            if num > 0:
                break
            # We create our Two Pointer solution
            target = - num
            l, r = i + 1, len(nums)-1
          
            while l < r:
                sumLR = nums[l] + nums[r]
                if sumLR == target:
                    triplets.append([num, nums[l], nums[r]])
                    # Avoid repetition
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sumLR < target:
                    l += 1
                else:
                    r -= 1
                
        return triplets