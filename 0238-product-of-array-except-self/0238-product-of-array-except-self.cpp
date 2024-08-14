class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);
        
        int left_side = 1;
        for (int i = 0; i < n; i++) {
            answer[i] = left_side;
            left_side *= nums[i];
        }
        
        // Separated from the left side to optimize cache access
        int right_side = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= right_side;
            right_side *= nums[i];
        }
        
        return answer;
    }
};
