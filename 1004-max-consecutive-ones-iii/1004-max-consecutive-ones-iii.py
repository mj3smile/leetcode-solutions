class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        result = 0
        curr_k = k
        for r in range(len(nums)):
            if nums[r] == 0:
                if k == 0:
                    l = r + 1
                    continue
                
                while curr_k == 0 and curr_k < k:
                    if nums[l] == 0:
                        curr_k += 1
                    l += 1
                
                curr_k -= 1
            
            result = max(result, r - l + 1)
        
        return result

                