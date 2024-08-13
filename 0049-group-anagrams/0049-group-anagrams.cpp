class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> ordered_strs;
        for(int i = 0; i < strs.size(); i++) {
            string sorted_str = strs[i];
            sort(sorted_str.begin(), sorted_str.end());
            ordered_strs[sorted_str].push_back(strs[i]); 
        }
        
        std::vector<vector<string>> result;

        for (auto pair : ordered_strs) {
            result.push_back(pair.second);
        }

        return result;
    }
};