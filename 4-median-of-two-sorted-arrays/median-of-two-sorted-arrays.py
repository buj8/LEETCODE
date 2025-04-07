class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_len = m + n
        evensized = total_len % 2 == 0
        print(f"M = {m}, N = {n}, Even Sized = {evensized}")
        i1, i2, count = 0, 0, 0
        last, prev = 0, 0
        while count <= total_len // 2:
            print(f"\tChecked: {count}")
            prev = last
            count += 1
            if i1 == m or i2 == n:
                if i1 == m:
                    print(f"\t\tNo more values in nums1")
                    last = nums2[i2]
                    i2 += 1
                else:
                    print(f"\t\tNo more values in nums2")
                    last = nums1[i1] 
                    i1 += 1
            else:
                if nums1[i1] < nums2[i2]:
                    print(f"\t\tNums1[{i1}] < Nums2[{i2}]")
                    last = nums1[i1]
                    i1 += 1
                else:
                    last = nums2[i2] 
                    i2 += 1

        if evensized:
            return (last + prev) / 2
        return last