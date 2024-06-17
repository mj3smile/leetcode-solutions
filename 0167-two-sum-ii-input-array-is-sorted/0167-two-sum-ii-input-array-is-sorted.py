class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = dict()
        
        for i, n in enumerate(numbers):
            if target - n in indices:
                return [indices[target-n], i+1]
            indices[n] = i + 1
        
        return []
