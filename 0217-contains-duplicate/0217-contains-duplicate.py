class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        items = set()

        for n in nums:
            if n in items:
                return True
            items.add(n)
        return False