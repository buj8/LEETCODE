class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_len = m + n
        evensized = total_len % 2 == 0
        i1, i2, count = 0, 0, 0
        last, prev = 0, 0
        while count <= total_len // 2:
            prev = last
            count += 1
            if i1 == m or i2 == n:
                if i1 == m:
                    last = nums2[i2]
                    i2 += 1
                else:
                    last = nums1[i1] 
                    i1 += 1
            else:
                if nums1[i1] < nums2[i2]:
                    last = nums1[i1]
                    i1 += 1
                else:
                    last = nums2[i2] 
                    i2 += 1

        if evensized:
            return (last + prev) / 2
        return last