class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def minOperations(index1, index2, cache):
            if index2 == len(word2):
                return len(word1) - index1

            if index1 == len(word1):
                return len(word2) - index2
            
            if (index1, index2) in cache:
                return cache[(index1, index2)]
            
            if word1[index1] == word2[index2]:
                cache[(index1, index2)] = minOperations(index1 + 1, index2 + 1, cache)
                return cache[(index1, index2)]
            
            cache[(index1, index2)] = 1 + min(
                minOperations(index1, index2 + 1, cache), # insert
                minOperations(index1 + 1, index2 + 1, cache), # replace
                minOperations(index1 + 1, index2, cache) # delete
            )
            return cache[(index1, index2)]
        
        return minOperations(0, 0, dict())