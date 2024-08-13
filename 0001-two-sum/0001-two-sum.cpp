class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> numIndex;
        for(int n = 0; n < size(nums); n++) {
            auto index = numIndex.find(target - nums[n]);
            if (index != numIndex.end()) {
                return std::vector<int>{index->second, n};
            }
            numIndex[nums[n]] = n;
        } 
        return std::vector<int>();
    }
};