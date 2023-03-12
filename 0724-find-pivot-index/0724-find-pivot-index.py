class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        result = n
        prefix_l, prefix_r = [0] * (n + 2), [0] * (n + 2)
        
        sum_l, sum_r = 0, 0
        for i in range(len(nums)):
            l, r = i, len(nums) - 1 - i
            sum_l, sum_r = sum_l + nums[l], sum_r + nums[r]
            l, r = l + 1, r + 1
            prefix_l[l], prefix_r[r] = sum_l, sum_r
            if l < r:
                continue
            
            if prefix_l[r - 1] == prefix_r[r + 1]:
                result = min(result, r - 1)
            if prefix_l[l - 1] == prefix_r[l + 1]:
                result = min(result, l - 1)
        
        return result if result < len(nums) else -1