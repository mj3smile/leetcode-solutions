class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        total = sum(nums)
        if total % 2 > 0:
            return False
        
        target = total // 2
        items = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(items + 1)]
        for i in range(items + 1):
            dp[i][0] = True

        for i in range(1, items + 1):
            for t in range(1, target + 1):
                if t >= nums[i - 1]:
                    dp[i][t] = dp[i - 1][t] or dp[i - 1][t - nums[i - 1]]
                else:
                    dp[i][t] = dp[i - 1][t]
        
        return dp[items][target]
    #     return self.canReachTarget(0, target, dict())
        
    # def canReachTarget(self, index, target, cache):
    #     if index == len(self.nums) or target < 0:
    #         return False
    #     if target == 0:
    #         return True
    #     if (index, target) in cache:
    #         return cache[(index, target)]

    #     cache[(index, target)] = self.canReachTarget(index + 1, target, cache) or self.canReachTarget(index + 1, target - self.nums[index], cache)
    #     return cache[(index, target)]