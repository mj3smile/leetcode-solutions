class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1.copy()

        i, j, k = 0, 0, 0   # i: index of result arr, j: nums1, k: nums2
        while i < len(nums1) and j < m or k < n:
            if j >= m:
                nums1[i] = nums2[k]
                k += 1
                i += 1
                continue
            
            if k >= n:
                nums1[i] = nums1_copy[j]
                j += 1
                i += 1
                continue
            
            if nums1_copy[j] < nums2[k]:
                nums1[i] = nums1_copy[j]
                j += 1
            else:
                nums1[i] = nums2[k]
                k += 1
            
            i += 1

        