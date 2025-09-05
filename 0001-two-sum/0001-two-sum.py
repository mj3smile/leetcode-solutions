class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = list()
        subs = dict() # key: result of target-items in nums, value: index of items

        for n in range(len(nums)):
            if nums[n] in subs:
                return [n, subs[nums[n]]]
            
            subs[target - nums[n]] = n
        