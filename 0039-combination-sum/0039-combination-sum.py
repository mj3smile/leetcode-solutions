class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        cache = set()

        def combination(total, currCombination, freq):
            if total > target:
                return
            if total == target:
                key = tuple(freq)
                if key not in cache:
                    cache.add(key)
                    result.append(currCombination.copy())
                return
            for i in range(len(candidates)):
                freq[i] += 1
                currCombination.append(candidates[i])
                combination(total + candidates[i], currCombination, freq)
                freq[i] -= 1
                currCombination.pop()
        
        combination(0, list(), [0 for _ in range(len(candidates))])
        return result