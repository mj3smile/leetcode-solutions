class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        curItems = set()

        for right in range(len(s)):
            while s[right] in curItems:
                curItems.remove(s[left])
                left += 1
            
            curItems.add(s[right])
            result = max(result, right - left + 1)
        
        return result