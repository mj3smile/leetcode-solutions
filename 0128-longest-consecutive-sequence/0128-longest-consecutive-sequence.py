class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = dict()
        
        for n in nums:
            sequence[n] = 0
        
        
        result = 0
        for n in nums:
            if sequence[n] > 0: continue
            curr_sequence = 0
            item = n
            while item in sequence:
                if sequence[item] > 1:
                    curr_sequence += sequence[item]
                    break
                sequence[item] = 1
                curr_sequence += 1
                item += 1

            sequence[n] = curr_sequence
            result = max(result, curr_sequence)
            
        return result
                