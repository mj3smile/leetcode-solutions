class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def find_combination(i, total, combination):
            if total == target:
                result.append(combination.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            combination.append(candidates[i])
            find_combination(i, total + candidates[i], combination)
            combination.pop()
            find_combination(i + 1, total, combination)
        
        find_combination(0, 0, [])
        return result