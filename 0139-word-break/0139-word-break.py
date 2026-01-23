class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.wordDict = wordDict
        return self.isMatchWithDict(0, dict())
        
    def isMatchWithDict(self, index, cache):
        if index == len(self.s):
            return True
        if index in cache:
            return cache[index]
        
        result = False
        for w in self.wordDict:
            if w[0] != self.s[index]:
                continue
            wordLen = len(w)
            if index + wordLen > len(self.s):
                continue
            if self.s[index:index+wordLen] != w:
                continue
            result = result or self.isMatchWithDict(index + wordLen, cache)
        
        cache[index] = result
        return cache[index]
