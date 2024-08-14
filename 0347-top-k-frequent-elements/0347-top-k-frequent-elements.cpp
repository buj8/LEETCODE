class Solution {
public:

    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> amounts;
        for(int num : nums) {
            amounts[num] += 1;
        }

        vector<pair<int, int>> sorted_amounts(amounts.begin(), amounts.end());
        
        auto pair_comparator = [](pair<int, int> a , pair<int, int> b) {
            return a.second > b.second;
        };
        
        sort(sorted_amounts.begin(), sorted_amounts.end(), pair_comparator);

        vector<int> result;
        for(int i = 0; i < k; i++) {
            result.push_back(sorted_amounts[i].first);
        }
        return result;
    }

    
};