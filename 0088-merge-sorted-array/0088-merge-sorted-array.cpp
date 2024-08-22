class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int len = m + n;
        int p2 = 0;
        vector<int>::iterator it;
        for(int i = m; i < len; i++) {
            nums1[i] = INT_MAX;
        }
        for(it = nums1.begin(); it != nums1.end(); it++) {
            if(p2 < n && nums2[p2] <= *it) {
                it = nums1.insert(it, nums2[p2]);
                nums1.pop_back();
                p2++;
            }
        }
        for(p2; p2 < n; p2++) {
            it = nums1.insert(it, nums2[p2]);
            nums1.pop_back();
        }
    }
};