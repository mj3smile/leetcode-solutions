class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.N = len(nums)
        result = 0
        self.cache = dict()
        for i in range(len(nums)):
            result = max(result, self.countIncreasing(i))
        return result

    def countIncreasing(self, index):
        if index >= self.N:
            return 0
        
        if index in self.cache:
            return self.cache[index]
        
        result = 0
        for i in range(index + 1, self.N):
            if self.nums[i] <= self.nums[index]:
                continue
            result = max(result, self.countIncreasing(i))
        
        self.cache[index] = 1 + result
        return self.cache[index]