class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        total = sum(nums)
        if total % 2 > 0:
            return False
        
        target = total / 2
        return self.canReachTarget(0, target, dict())
        
    def canReachTarget(self, index, target, cache):
        if index == len(self.nums) or target < 0:
            return False
        if target == 0:
            return True
        if (index, target) in cache:
            return cache[(index, target)]

        cache[(index, target)] = self.canReachTarget(index + 1, target, cache) or self.canReachTarget(index + 1, target - self.nums[index], cache)
        return cache[(index, target)]