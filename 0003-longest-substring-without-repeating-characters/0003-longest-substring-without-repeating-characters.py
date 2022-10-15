class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 1
        substr_char = set(s[l])
        long = 1
        
        while r < len(s):
            if s[r] in substr_char:
                while s[r] in substr_char:
                    substr_char.remove(s[l])
                    l += 1
            
            substr_char.add(s[r])
            long = max(long, r - l + 1)
            r += 1
        
        return long
                
                