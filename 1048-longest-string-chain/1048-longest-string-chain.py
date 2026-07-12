class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPredecessor(a, b):
            if len(a) + 1 != len(b):
                return False
            
            diff = 0
            j = 0
            for i in range(len(b)):
                if diff > 1:
                    return False
                
                if j == len(a) or a[j] != b[i]:
                    diff += 1
                else:
                    j += 1
                
            return diff == 1
        
        cache = dict()
        def chainLength(index, choosen):
            if index in choosen:
                return 0
            
            if index in cache:
                return cache[index]

            choosen.add(index)
            result = 0
            for i in range(len(words)):
                if i in choosen:
                    continue
                if isPredecessor(words[index], words[i]):
                    result = max(result, chainLength(i, choosen))
            
            cache[index] = 1 + result
            return 1 + result
        
        result = 0
        for i in range(len(words)):
            result = max(result, chainLength(i, set()))
        
        return result