class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        if s1 + s2 == s3:
            return True

        def isMatch(index1, index2, index3, cache):
            if (index1, index2) in cache:
                return cache[(index1, index2)]
            if index1 == len(s1):
                return index2 < len(s2) and s2[index2:] == s3[index3:]
            if index2 == len(s2):
                return index1 < len(s1) and s1[index1:] == s3[index3:] 
            if s1[index1] != s3[index3] and s2[index2] != s3[index3]:
                return False
            result = False
            if s1[index1] == s3[index3]:
                result = result or isMatch(index1 + 1, index2, index3 + 1, cache)
            if s2[index2] == s3[index3]:
                result = result or isMatch(index1, index2 + 1, index3 + 1, cache)
            cache[(index1, index2)] = result
            return result
        
        return isMatch(0, 0, 0, dict())