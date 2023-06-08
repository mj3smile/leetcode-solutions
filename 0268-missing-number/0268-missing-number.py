class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index = set(nums)
        
        for i in range(len(nums) + 1):
            if i not in index:
                return i