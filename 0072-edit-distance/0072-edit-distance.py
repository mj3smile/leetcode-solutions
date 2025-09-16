class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1, self.word2 = word1, word2
        return self.countMinDistance(0, 0, dict())
    
    def countMinDistance(self, w1, w2, cache):
        if w1 == len(self.word1) and w2 == len(self.word2):
            return 0
        
        if w1 == len(self.word1):
            return len(self.word2) - w2
        
        if w2 == len(self.word2):
            return len(self.word1) - w1
        
        if (w1, w2) in cache:
            return cache[(w1, w2)]
        
        result = 0
        if self.word1[w1] == self.word2[w2]:
            result = self.countMinDistance(w1 + 1, w2 + 1, cache)
        else:
            result = 1 + min(
                self.countMinDistance(w1 + 1, w2 + 1, cache),
                self.countMinDistance(w1, w2 + 1, cache),
                self.countMinDistance(w1 + 1, w2, cache)
            )
        
        cache[(w1, w2)] = result
        return result