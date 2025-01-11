class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()
        cache = set()
        for i in range(len(nums)):
            target = 0 - nums[i]

            left, right = i + 1, len(nums) - 1
            while left < right and left < len(nums):
                total = nums[left] + nums[right]
                if total > target:
                    right -= 1
                    continue
                elif total < target:
                    left += 1
                    continue
                
                c = (nums[i], nums[left], nums[right])
                if c not in cache:
                    result.append([nums[i], nums[left], nums[right]])
                    cache.add(c)
                
                left += 1
        
        return result