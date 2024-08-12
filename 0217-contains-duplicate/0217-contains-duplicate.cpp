class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> numAmount;
        for (int num : nums) {
            if (numAmount[num] >= 1)
                return true;
            numAmount[num]++;
        }
        return false;
    }
};