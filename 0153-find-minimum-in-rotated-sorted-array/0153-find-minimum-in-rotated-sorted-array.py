class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] > nums[-1]:
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return nums[i]
        
        return nums[0]