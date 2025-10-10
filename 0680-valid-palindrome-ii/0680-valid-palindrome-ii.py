class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left, right = left+1, right-1
        
        if left == right:
            return True
        
        deletion_1 = s[:left] + s[left+1:] if left > 0 else s[left+1:]
        deletion_2 = s[:right] + s[right+1:] if right < len(s)-1 else s[:right]

        return self.isPalindrome(deletion_1) or self.isPalindrome(deletion_2)
        
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right-1
        return True

