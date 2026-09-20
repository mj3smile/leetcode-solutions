class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        currChars = set()

        result = 0
        for r in range(len(s)):
            while s[r] in currChars and l < r:
                currChars.remove(s[l])
                l += 1
            
            currChars.add(s[r])
            result = max(result, r - l + 1)
        
        return result