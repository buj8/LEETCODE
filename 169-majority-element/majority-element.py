class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        current_max = (0, -1)
        majority = math.floor(len(nums)/2)
        for num in nums:
            count[num] += 1
            if count[num] > current_max[0]:
                current_max = (count[num], num)
                if current_max[0] > majority:
                    return current_max[1]

        return current_max[1]

