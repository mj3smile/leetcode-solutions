class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result = len(nums)
        prefix_l, prefix_r = [0] * len(nums), [0] * len(nums)
        
        sum_l, sum_r = 0, 0
        for i in range(len(nums)):
            l, r = i, len(nums) - 1 - i
            sum_l, sum_r = sum_l + nums[l], sum_r + nums[r]
            prefix_l[l], prefix_r[r] = sum_l, sum_r
            if l < r:
                continue
            
            sl, sr = prefix_l[r - 1] if r > 0 else 0, prefix_r[r + 1] if r < len(nums) - 1 else 0
            if sl == sr:
                result = min(result, r)
            sl, sr = prefix_l[l - 1] if l > 0 else 0, prefix_r[l + 1] if l < len(nums) - 1 else 0
            if sl == sr:
                result = min(result, l)
            
        return result if result < len(nums) else -1