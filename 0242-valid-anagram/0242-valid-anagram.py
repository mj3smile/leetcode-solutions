class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = dict()

        for char in s:
            s_chars[char] = s_chars.get(char, 0) + 1
        
        for char in t:
            if char not in s_chars:
                return False
            
            if s_chars[char] == 1:
                del s_chars[char]
            else:
                s_chars[char] -= 1
        
        return len(s_chars) == 0