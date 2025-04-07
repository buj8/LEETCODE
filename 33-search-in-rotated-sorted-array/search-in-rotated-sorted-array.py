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
            mid = left + (right - left) // 2
            print(f"L:{left}, R:{right}, MID:{mid}")
            if nums[mid] == target:
                return mid

            # If our subarray is sorted we just do binary search
            if nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            # If it's not sorted, we look for the half that contains the target
            else:
                # Left side is sorted
                if nums[left] <= nums[mid]:
                    if target >= nums[left] and target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                # Right side is sorted
                else:
                    if target <= nums[right] and target > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1


        return -1
