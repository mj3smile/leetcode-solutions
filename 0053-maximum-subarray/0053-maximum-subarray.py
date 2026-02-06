class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        allPositive, allNegative = True, True
        total = 0
        maxVal = 0
        for i in range(len(nums)):
            if i == 0:
                maxVal = nums[i]

            allNegative = allNegative and nums[i] < 0
            allPositive = allPositive and nums[i] >= 0
            total += nums[i]
            maxVal = max(maxVal, nums[i])
        
        if allNegative:
            return maxVal
        if allPositive:
            return total
        
        result = 0
        curr = 0
        for i in range(len(nums)):
            if i == 0:
                result = nums[i]
            
            curr += nums[i]
            result = max(result, curr)
            if curr < 0:
                curr = 0
        
        return result