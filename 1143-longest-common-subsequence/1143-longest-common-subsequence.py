class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1, self.text2 = text1, text2
        return self.countCommonSubsequence(0, 0, dict())
    
    def countCommonSubsequence(self, s1, s2, cache):
        if s1 == len(self.text1) or s2 == len(self.text2):
            return 0
        
        if (s1, s2) in cache:
            return cache[(s1, s2)]
        
        result = 0
        if self.text1[s1] == self.text2[s2]:
            result = 1 + self.countCommonSubsequence(s1 + 1, s2 + 1, cache)
        else:
            result = max(self.countCommonSubsequence(s1 + 1, s2, cache), self.countCommonSubsequence(s1, s2 + 1, cache))
        
        cache[(s1, s2)] = result
        return cache[(s1, s2)]