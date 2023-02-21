class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = 1
        
        prev = -1
        l = 0
        for r in range(1, len(arr)):
            if arr[r] == arr[r - 1]:
                l = r
                prev = -1
                continue
                
            if prev >= 0 and ((arr[r] > arr[r - 1]) == (arr[r - 1] > prev)):
                l = r - 1
                prev = arr[r - 1]
                continue
                            
            result = max(result, r - l + 1)
            prev = arr[r - 1]
            
        return result