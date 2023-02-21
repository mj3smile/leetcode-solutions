class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        items = dict()
        
        for i in range(len(nums)):
            if nums[i] in items and i - items[nums[i]] <= k:
                return True
            
            items[nums[i]] = i
        
        return False