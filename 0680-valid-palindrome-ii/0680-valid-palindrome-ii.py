class Solution:
    def __init__(self):
        self.s = ""

    def validPalindrome(self, s: str) -> bool:
        self.s = s

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.validWithoutDeletePalindrome(left + 1, right) or self.validWithoutDeletePalindrome(left, right - 1)
            
            left, right = left + 1, right - 1
        
        return True
    
    def validWithoutDeletePalindrome(self, left: int, right: int) -> bool:
        while left < right:
            if self.s[left] != self.s[right]:
                return False
                
            left, right = left + 1, right - 1

        return True