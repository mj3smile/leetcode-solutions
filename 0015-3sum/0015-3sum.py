class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            target = 0 - nums[i]
            pairs = dict()

            for j in range(i + 1, len(nums)):
                if nums[j] in pairs:
                    result.append([nums[i], pairs[nums[j]], nums[j]])
                pairs[target - nums[j]] = nums[j]
        
        return result