class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up
        def robFrom(nums):
            if not nums:
                return 0
            if len(nums) <= 2:
                return max(nums)
        
            counts = [nums[0], nums[1]]
            for i in range(2, len(nums)):
                tmp = counts[1]
                counts[1] = nums[i] + counts[0]
                counts[0] = max(tmp, counts[0])

            return max(counts)
        
        return max(nums[0], robFrom(nums[:-1]), robFrom(nums[1:]))
    
        # top down
        def robFrom(left, right, cache):
            if left > right:
                return 0
            if left in cache:
                return cache[left]
            
            total = nums[left]
            total += max(robFrom(left+2, right, cache), robFrom(left+3, right, cache))
            cache[right] = total
            
            return total
        
        
        first = robFrom(0, len(nums) - 2, dict())
        second = robFrom(1, len(nums) - 1, dict())
        return max(nums[0], first, second)