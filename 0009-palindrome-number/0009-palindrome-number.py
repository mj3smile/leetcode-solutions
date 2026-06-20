class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed = 0
        num = x
        while num > 0:
            reversed = reversed * 10 + (num % 10)
            num = num // 10
        
        return reversed == x