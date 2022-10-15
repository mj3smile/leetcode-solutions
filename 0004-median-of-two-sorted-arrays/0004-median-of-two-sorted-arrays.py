class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged = []
        
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                merged.append(nums2[j])
                j += 1
                continue
            
            if j == len(nums2):
                merged.append(nums1[i])
                i += 1
                continue
            
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
            
        
        count = len(merged)
        median = (0 + count - 1) // 2
        
        return (merged[median] + merged[median + 1]) / 2 if count % 2 == 0 else merged[median]
        
            
            