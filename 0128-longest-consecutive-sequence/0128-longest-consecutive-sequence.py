class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = dict()
        
        for n in nums:
            elements[n] = 0
        
        
        result = 0
        for n in nums:
            if elements[n] > 0: continue
            item = n
            seq = 0
            while item in elements:
                if elements[item] > 1:
                    seq += elements[item]
                    break
                elements[item] = 1
                seq += 1
                item += 1

            elements[n] = seq
            result = max(result, seq)
            
        return result
                