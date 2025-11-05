class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        curItems = set()
        left = 0
        for right in range(len(nums)):
            if curItems and right - left > k:
                curItems.remove(nums[left])
                left += 1

            if nums[right] in curItems:
                return True
            
            curItems.add(nums[right])
        
        return False