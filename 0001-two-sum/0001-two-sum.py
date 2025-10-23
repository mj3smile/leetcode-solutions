class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        substraction = dict()

        for i in range(len(nums)):
            if nums[i] in substraction:
                return [substraction[nums[i]], i]
            else:
                substraction[target - nums[i]] = i
            