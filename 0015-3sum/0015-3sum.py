class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            total = 0 - nums[i]
            diff = dict()
            for j in range(i + 1, len(nums)):
                if nums[j] in diff:
                    result.append([nums[i], diff[nums[j]], nums[j]])
                    continue
                else:
                    diff[total - nums[j]] = nums[j]
        
        return result