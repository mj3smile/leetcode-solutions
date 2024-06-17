class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
            lchar = s[left].lower()
            if not lchar.isalnum():
                left += 1
                continue
            
            rchar = s[right].lower()
            if not rchar.isalnum():
                right -= 1
                continue
            
            if lchar != rchar:
                return False
            
            left += 1
            right -= 1
        
        return True