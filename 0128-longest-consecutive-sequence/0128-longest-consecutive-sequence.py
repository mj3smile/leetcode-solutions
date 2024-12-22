class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = dict()

        for n in nums:
            elements[n] = 0
        
        result = 0
        for n in nums:
            if n - 1 in elements:
                continue
            
            i = n
            while i in elements:
                if elements[i] > 0:
                    break
                    
                elements[n] += 1
                i += 1
            
            result = max(result, elements[n])
        
        return result

