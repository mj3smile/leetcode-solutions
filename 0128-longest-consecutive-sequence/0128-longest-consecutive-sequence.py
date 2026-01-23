class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        items = set(nums)
        result = 0

        calculated = set()
        for n in nums:
            if n - 1 in items or n in calculated:
                continue
            
            length = 1
            curr = n
            while curr + 1 in items:
                length += 1
                curr = curr + 1
            
            calculated.add(n)
            result = max(result, length)
        
        return result