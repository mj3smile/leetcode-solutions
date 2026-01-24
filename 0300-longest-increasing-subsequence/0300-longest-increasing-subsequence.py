class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.N = len(nums)
        result = 0
        cache = dict()
        for i in range(len(nums)):
            a = self.countIncreasing(i, cache)
            # print(i, a)
            result = max(result, a)
        return result

    def countIncreasing(self, index, cache):
        if index >= self.N:
            return 0
        
        if index in cache:
            return cache[index]
        
        result = 0
        for i in range(index + 1, self.N):
            if self.nums[i] <= self.nums[index]:
                continue
            result = max(result, self.countIncreasing(i, cache))
        
        cache[index] = 1 + result
        return cache[index]