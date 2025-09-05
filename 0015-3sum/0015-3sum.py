class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = list()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - nums[i]
            subs = dict()
            appeared = set()

            for x in range(i + 1, len(nums)):
                if x > i + 1 and nums[x] == nums[x - 1] and nums[x] in appeared:
                    continue
                
                if nums[x] in subs:
                    appeared.add(nums[x])
                    result.append([nums[i], nums[x], nums[subs[nums[x]]]])
                
                subs[target - nums[x]] = x
        
        return result