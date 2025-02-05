class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleted = 0
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left, right = left + 1, right - 1
                continue
            
            if deleted == 1:
                return False

            if self.validWithoutDeletePalindrome(s[left+1:right+1]):
                deleted += 1
                left += 1
                continue
            
            if self.validWithoutDeletePalindrome(s[left:right]):
                deleted += 1
                right -= 1
                continue
            
            return False
        
        return True
    
    def validWithoutDeletePalindrome(self, s: str) -> bool:
        for left in range(len(s) // 2):
            right = len(s) - left - 1
            if s[left] != s[right]:
                return False

        return True