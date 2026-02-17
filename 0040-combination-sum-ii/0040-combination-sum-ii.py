class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # freq = list()
        # freqIndex = dict()
        # for n in nums:
        #     if n in freqIndex:
        #         continue
        #     freqIndex[n] = len(freq)
        #     freq.append(0)
        
        result = list()
        cache = set()

        def combination(total, currCombination, selected):
            if total > target:
                return
            
            if total == target:
                key = tuple(selected)
                if key in cache:
                    return
                cache.add(key)
                result.append(currCombination.copy())
                return

            processed = set()
            for i in range(len(candidates)):
                if not selected[i] and candidates[i] not in processed:
                    selected[i] = True
                    currCombination.append(candidates[i])
                    combination(total + candidates[i], currCombination, selected)
                    selected[i] = False
                    currCombination.pop()
                    
                    processed.add(candidates[i])

        combination(0, list(), [False for _ in range(len(candidates))])
        return result