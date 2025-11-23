class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        total = sum(nums)
        if total % 2 > 0:
            return False
        
        target = total / 2
        reached, numItems = self.canReachTarget(0, target, 0, dict())
        return reached and numItems < len(nums)
    
    def canReachTarget(self, index, target, numItems, cache):
        if index < 0 or index == len(self.nums) or target < 0:
            return False, 0
        
        if target == 0:
            return True, numItems
        
        if (index, target) in cache:
            r, i = cache[(index, target)]
            return r, i
        
        reachedTarget, items = self.canReachTarget(index + 1, target, numItems, cache)
        newTarget = target - self.nums[index]
        if newTarget >= 0:
            reached, i = self.canReachTarget(index + 1, newTarget, numItems + 1, cache)
            if reached:
                reachedTarget, items = reached, i
        
        cache[(index, target)] = (reachedTarget, items)
        return reachedTarget, items