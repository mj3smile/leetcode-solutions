class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
            
            if nums[r - 1] < nums[r]:
                continue

            increase_by = nums[r - 1] - nums[r] + 1
            nums[r] += increase_by
            result += increase_by
        
        return result    
