class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        n = len(nums)
        if n == 1:
            return nums[0]
        
        startIndex = 0
        return max(self.maxProfit(startIndex, n - 1, dict()), self.maxProfit(startIndex + 1, n, dict()))
    
    def maxProfit(self, index, end, cache):
        if index >= end:
            return 0
        
        if index in cache:
            return cache[index]
        
        cache[index] = max(self.nums[index] + self.maxProfit(index + 2, end, cache), self.maxProfit(index + 1, end, cache))
        return cache[index]