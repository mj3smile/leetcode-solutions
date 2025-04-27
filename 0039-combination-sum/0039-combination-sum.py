class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.cache = set()
        self.result = list()

        for i in range(len(self.candidates)):
            self.findCombination(i, [], 0)

        return self.result
    
    def findCombination(self, index, combination, total): 
        length = len(self.candidates)
        if index < 0 or index == length:
            return
        
        if total > self.target:
            return
        
        if total == self.target:
            item = sorted(combination.copy())
            key = tuple(item)
            if key not in self.cache:
                self.result.append(item)
                self.cache.add(key)
            return
        
        total += self.candidates[index]
        combination.append(self.candidates[index])
        self.findCombination(index, combination, total)
        for i in range(index + 1, length):
            self.findCombination(i, combination, total)
        combination.pop()
        