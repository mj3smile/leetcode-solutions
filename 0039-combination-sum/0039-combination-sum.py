class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        cache = set()
        def calculate(combination, itemFreq, total):
            if total > target:
                return
            nonlocal result
            if total == target:
                key = tuple(itemFreq)
                if key in cache:
                    return
                result.append(combination.copy())
                cache.add(key)
                return
            for i in range(len(candidates)):
                combination.append(candidates[i])
                itemFreq[i] += 1
                calculate(combination, itemFreq, total + candidates[i])
                itemFreq[i] -= 1
                combination.pop()
        
        calculate(list(), [0 for _ in range(len(candidates))], 0)
        return result