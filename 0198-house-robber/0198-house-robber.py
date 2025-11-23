class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return self.maxProfit(0, dict())
    
    def maxProfit(self, index, cache):
        if index >= len(self.nums):
            return 0
        
        if index in cache:
            return cache[index]
        
        cache[index] = max(self.nums[index] + self.maxProfit(index + 2, cache), self.maxProfit(index + 1, cache))
        return cache[index]