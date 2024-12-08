class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        s_word = dict()
        for c in s:
            s_word[c] = s_word.get(c, 0) + 1
        
        for c in t:
            if c not in s_word or (c in s_word and s_word[c] == 0):
                return False
            
            s_word[c] -= 1
        
        return True