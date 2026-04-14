class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        left = 0
        curSum = 0
        for right in range(len(nums)):
            curSum += nums[right]
            
            # if curSum >= target:
            #     result = min(result, right - left + 1)
            
            while curSum >= target and left < len(nums):
                result = min(result, right - left + 1)
                curSum -= nums[left]
                left += 1
        
        if result == len(nums) + 1:
            return 0
        return result
            