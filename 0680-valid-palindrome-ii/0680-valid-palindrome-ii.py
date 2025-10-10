class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left, right = left+1, right-1
        
        if left == right:
            return True

        return self.isPalindrome(s[left:right]) or self.isPalindrome(s[left+1:right+1])
        
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right-1
        return True

