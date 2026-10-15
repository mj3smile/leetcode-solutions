class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0
        
        l = 0
        freq = dict()
        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            while freq[nums[r]] > k and l < r:
                freq[nums[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        
        return result