class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1, self.s2, self.s3 = s1, s2, s3
        return self.calculateInterleave(0, 0, 0, dict())
    
    def calculateInterleave(self, p1, p2, p3, cache):
        if p3 == len(self.s3) and p1 == len(self.s1) and p2 == len(self.s2):
            return True
        
        if (p1 == len(self.s1) and p2 == len(self.s2)) or p3 == len(self.s3):
            return False
        
        char1 = "" if p1 == len(self.s1) else self.s1[p1]
        char2 = "" if p2 == len(self.s2) else self.s2[p2]
        char3 = self.s3[p3]

        if char3 != char1 and char3 != char2:
            return False
        
        if (p1, p2) in cache:
            return cache[(p1, p2)]
        
        result = True
        if char1 == char2:
            result = result and (self.calculateInterleave(p1 + 1, p2, p3 + 1, cache) or self.calculateInterleave(p1, p2 + 1, p3 + 1, cache))
        elif char1 == char3:
            result = result and self.calculateInterleave(p1 + 1, p2, p3 + 1, cache)
        else:
            result = result and self.calculateInterleave(p1, p2 + 1, p3 + 1, cache)
        
        cache[(p1, p2)] = result
        return result
        