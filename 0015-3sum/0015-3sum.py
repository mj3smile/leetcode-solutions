class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i > 0 and nums[i - 1] == nums[i]: continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]: j += 1
                elif sums > 0:
                    k -= 1
                elif sums < 0:
                    j += 1
            
        return result