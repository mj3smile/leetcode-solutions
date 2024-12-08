class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        substractions = dict()

        for i in range(len(nums)):
            if nums[i] in substractions:
                return [substractions[nums[i]], i]
            
            substractions[target - nums[i]] = i