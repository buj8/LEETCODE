class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        while left <= right:
            # We get our mid point and check if it's the target
            mid = left + (right - right) // 2
            if nums[mid] == target:
                return mid

            # If our subarray is sorted we just do binary search
            if nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            # If it's not sorted, we look for the half that contains the target
            #elif target > nums[right] and 
            else:
                left += 1


        return -1
