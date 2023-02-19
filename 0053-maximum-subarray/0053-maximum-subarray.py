class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curr_sum = 0
        
        for n in nums:
            curr_sum += n
            result = max(curr_sum, result)
            curr_sum = max(curr_sum, 0)
        
        return result