class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 > 0:
            return False
        
        target = total // 2
        def canReachTarget(index, currTotal, cache):
            if currTotal == target:
                return True
            if currTotal > target or index == len(nums):
                return False
            if (index, currTotal) in cache:
                return cache[(index, currTotal)]

            cache[(index, currTotal)] = canReachTarget(index + 1, currTotal, cache) or canReachTarget(index + 1, currTotal + nums[index], cache)
            return cache[(index, currTotal)]
        
        return canReachTarget(0, 0, dict())