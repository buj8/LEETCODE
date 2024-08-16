class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int total_size = nums1.size() + nums2.size();
        int len = (total_size % 2 == 1) ? ((total_size + 1) / 2) : (1 +(total_size + 1) / 2); 
        int p1 = 0, p2 = 0;
        int prev = 0, curr = 0;

        for (int i = 0; i < len; i++) {
            prev = curr;
            if (p1 < nums1.size() && (p2 >= nums2.size() || nums1[p1] <= nums2[p2])) {
                curr = nums1[p1++];
            } else {
                curr = nums2[p2++];
            }
        }

        if (total_size % 2 == 1) {
            return curr;
        } else {
            return (prev + curr) / 2.0;
        }
    }
};
