class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Booyer-Moore Majority Vote Algorithm
        count = 1
        candidate = nums[0]
        for i in range(1, len(nums)):
            if candidate == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = nums[i]
                    count = 1
        return candidate

