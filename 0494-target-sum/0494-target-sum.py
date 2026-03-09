class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0

        def targetSum(index, total, cache):
            if index == len(nums):
                if total == target:
                    return 1
                return 0
            
            if (index, total) in cache:
                return cache[(index, total)]
            cache[(index, total)] = targetSum(index + 1, total + nums[index], cache) + targetSum(index + 1, total - nums[index], cache)
            return cache[(index, total)]
        
        return targetSum(0, 0, dict())