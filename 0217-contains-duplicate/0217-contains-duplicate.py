class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        
        for i in nums:
            if i in cache:
                return True
            cache.add(i)
        
        return False