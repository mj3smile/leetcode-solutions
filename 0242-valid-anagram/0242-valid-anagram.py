class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        s_chars = dict()
        for c in s:
            s_chars[c] = s_chars.get(c, 0) + 1
        
        for c in t:
            if c not in s_chars or (c in s_chars and s_chars[c] == 0):
                return False
            
            s_chars[c] -= 1
        
        return True